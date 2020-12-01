import sys
from antlr4 import *
from QSharpLexer import QSharpLexer
from QSharpParser import QSharpParser

class QSharpListener(ParseTreeListener):
    def enterKey(self, ctx):
        pass

    def enterValue(self, ctx):
        pass   

    def exitKey(self, ctx):         
        print("Oh, a key!") 

    def exitValue(self, ctx):         
        print("Oh, a value!") 

    def visitTerminal(self, node):
        print(node.symbol.text)

if __name__ == '__main__':
    input_stream = FileStream(sys.argv[1])
    lexer = QSharpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QSharpParser(stream)
    tree = parser.namespace()
    printer = QSharpListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
