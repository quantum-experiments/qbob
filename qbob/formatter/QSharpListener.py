import sys
from antlr4 import *
from antlr4.tree import Tree
from qbob.formatter.QSharpLexer import QSharpLexer
from qbob.formatter.QSharpParser import QSharpParser, ParserRuleContext

TAB = "    "

def get_level(node, level = -1):
    if node is None:
        return level
    return get_level(node.parentCtx, level=level + 1)

class QSharpListener(ParseTreeListener):
    """Listener for QSharp Parse tree that formats Q# code
    """
    def __init__(self, debug: bool = False, *args, **kwargs):
        self.indentation = 0
        self.value = ""
        self.newline = False
        self.n = 0
        self.debug = debug
        super().__init__(*args, **kwargs)

    def visitTerminal(self, node):
        """Visit terminal node and add formatted output to the listener's value

        :param node: The Node
        :type node: Node
        """

        # Check if the node is part of parent context of a given type
        def in_context(ctx_type):
            return isinstance(node.parentCtx, ctx_type)

        # Pre and post fix strings to prepend and append
        pre = post = ""

        # Some vars to keep track of node number in its tree level
        tree_nodes = [n for n in node.parentCtx.children if isinstance(n, Tree.TerminalNodeImpl)]
        node_index = tree_nodes.index(node)
        first_node = node_index == 0
        last_node = node_index == len(tree_nodes) - 1

        # Nodes with newlines
        if first_node:
            if in_context(QSharpParser.CallableDeclarationContext):
                self.indentation += 1
                indent = TAB * self.indentation
                pre += "\n" + indent
        
            elif in_context(QSharpParser.ScopeContext):
                pre += " "
                self.indentation += 1
                indent = TAB * self.indentation
                post += "\n" + indent

            elif in_context(QSharpParser.ReturnStatementContext):
                indent = TAB * self.indentation
                pre += "\n" + indent

        elif last_node:
            if in_context(QSharpParser.ScopeContext) or in_context(QSharpParser.NamespaceContext):
                self.indentation -= 1
                indent = TAB * self.indentation
                pre += "\n" + indent

        # Nodes with spaces
        if in_context(QSharpParser.NamespaceContext):
            if first_node:
                post += " "
            if node_index == len(tree_nodes) - 2:
                pre += " "

        elif in_context(QSharpParser.CallableDeclarationContext):
            if first_node:
                post += " "

        elif in_context(QSharpParser.ParameterTupleContext):
            if first_node:
                pre += " "
            if last_node:
                post += " "

        elif in_context(QSharpParser.Type_ruleContext):
            if first_node:
                pre += " "

        elif in_context(QSharpParser.LetStatementContext):
            if first_node:
                post += " "
            if node.symbol.text == "=":
                pre += " "
                post += " "

        elif in_context(QSharpParser.ReturnStatementContext):
            if first_node:
                post += " "

        self.value += f"{pre}{node.symbol.text}{post}"

    def enterEveryRule(self, ctx: ParserRuleContext):
        if self.debug:
            print(f"{self.n}:{type(ctx)}")
            self.n += 1

    def exitEveryRule(self, ctx: ParserRuleContext):
        if self.debug:
            self.value += "]"


if __name__ == '__main__':
    input_stream = FileStream(sys.argv[1])
    lexer = QSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QSharpParser(stream)
    tree = parser.namespace()
    printer = QSharpListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
