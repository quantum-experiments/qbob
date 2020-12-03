import sys
from antlr4 import *
from antlr4.tree import Tree
from qbob.formatter.QSharpLexer import QSharpLexer
from qbob.formatter.QSharpParser import QSharpParser, ParserRuleContext

TAB = "    "
NEWLINE = "\n"

def get_level(node, level = -1):
    if node is None:
        return level
    return get_level(node.parentCtx, level=level + 1)

class QSharpListener(ParseTreeListener):
    """Listener for QSharp Parse tree that formats Q# code
    """
    def __init__(self, debug: bool = False, *args, **kwargs):
        self.indentation = 0
        self._value = ""
        self.newline = False
        self.n = 0
        self.in_namespace = False
        self.debug = debug
        super().__init__(*args, **kwargs)

    @property
    def value(self):
        return self._value.rstrip(NEWLINE)

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
        if first_node and not last_node:
            if in_context(QSharpParser.CallableDeclarationContext) and self.in_namespace:
                # define an operation or function within a namespace
                self.indentation += 1
                pre += NEWLINE
        
            elif in_context(QSharpParser.ScopeContext):
                # start a scope {
                pre += " "
                self.indentation += 1
                post += NEWLINE

        elif last_node:
            if in_context(QSharpParser.ScopeContext):
                # finish a scope }
                self.indentation -= 1
                post += NEWLINE
            
            elif in_context(QSharpParser.NamespaceContext):
                # finish a namespace }
                self.indentation -= 1
            
            elif in_context(QSharpParser.ExpressionStatementContext) or \
                in_context(QSharpParser.MutableStatementContext) or \
                in_context(QSharpParser.SetStatementContext) or \
                in_context(QSharpParser.ReturnStatementContext) or \
                in_context(QSharpParser.LetStatementContext):
                # end an expression ;
                post += NEWLINE

            elif in_context(QSharpParser.UntilStatementContext):
                # new line and indent before "fixup"
                # pre += NEWLINE + TAB * self.indentation
                pre += NEWLINE

        # Nodes with spaces
        if in_context(QSharpParser.NamespaceContext):
            # space after the namespace token
            if first_node:
                post += " "
            if node.symbol.text == ":":
                # space before the colon :
                pre += " "
            elif node.symbol.text == "{":
                pre += " "

        elif in_context(QSharpParser.CallableDeclarationContext):
            # space after "operation" or "function" tokens
            if first_node:
                post += " "
            if node.symbol.text == ":":
                post += " "

        elif in_context(QSharpParser.NamedItemContext):
            # Space around colon in func or op signature
            if node.symbol.text == ":":
                pre += " "
                post += " "

        elif in_context(QSharpParser.ParameterTupleContext):
            # Before and after parens
            if first_node: #(
                pre += " "
            elif last_node: #)
                post += " "
            elif node.symbol.text == ",":
                # comma inside tuple
                post += " "

        elif in_context(QSharpParser.ArrayExpressionContext):
            # comma inside list
            if node.symbol.text == ",":
                post += " "

        elif in_context(QSharpParser.IfStatementContext):
            # Before and after parens
            if first_node: #if
                # pre += NEWLINE + TAB * self.indentation
                pre += NEWLINE
                post += " "

        elif in_context(QSharpParser.CallExpressionContext):
            # Comma inside call expression
            if node.symbol.text == ",":
                post += " "

        elif in_context(QSharpParser.LetStatementContext) or \
            in_context(QSharpParser.MutableStatementContext) or \
            in_context(QSharpParser.SetStatementContext):
            # Spaces in let statement
            if first_node:
                post += " "
            if node.symbol.text == "=":
                pre += " "
                post += " "

        elif in_context(QSharpParser.ReturnStatementContext):
            # Space after return token
            if first_node:
                post += " "

        elif in_context(QSharpParser.UsingStatementContext) or \
            in_context(QSharpParser.UntilStatementContext) or \
            in_context(QSharpParser.EqualsExpressionContext):

            if node.symbol.text in ["=", "=="]:
                pre += " "
                post += " "
            # Space before paren (
            elif first_node:
                post += " "

        elif in_context(QSharpParser.ApplyStatementContext):
            if first_node:
                pre += " "
                self._value = self._value.rstrip("\n")

        # If the statement starts with a new line, add indentation
        if pre.endswith(NEWLINE):
            pre += TAB * self.indentation
        # If the previous statement ended with a new line, insert 
        # indentation before current statement
        elif self._value.endswith(NEWLINE):
            pre = TAB * self.indentation + pre

        self._value += f"{pre}{node.symbol.text}{post}"

    def enterEveryRule(self, ctx: ParserRuleContext):
        if isinstance(ctx, QSharpParser.NamespaceContext):
            self.in_namespace = True
        if self.debug:
            print(f"{self.n}:{type(ctx)}")
            self._value += f"{self.n}["
            self.n += 1

    def exitEveryRule(self, ctx: ParserRuleContext):
        if isinstance(ctx, QSharpParser.NamespaceContext):
            self.in_namespace = False
        if self.debug:
            self._value += "]"


if __name__ == '__main__':
    input_stream = FileStream(sys.argv[1])
    lexer = QSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QSharpParser(stream)
    tree = parser.target()
    printer = QSharpListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
