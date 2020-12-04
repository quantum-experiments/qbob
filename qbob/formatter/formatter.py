import abc

from typing import Union
from antlr4 import InputStream, FileStream, CommonTokenStream, ParseTreeWalker

from qbob.formatter.QSharpParser import QSharpParser
from qbob.formatter.QSharpLexer import QSharpLexer
from qbob.formatter.QSharpListener import QSharpListener


class Formatter(abc.ABC):

    @property
    @abc.abstractmethod
    def lexer_cls(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def parser_cls(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def listener_cls(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def parser_entry_fn(self):
        raise NotImplementedError

    def _format_input_stream(self, input_stream: Union[InputStream, FileStream]):
        lexer = self.lexer_cls(input_stream)
        stream = CommonTokenStream(lexer)
        parser = self.parser_cls(stream)
        tree = getattr(parser, self.parser_entry_fn)()
        listener = self.listener_cls()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.value

    def format_file(self, file_name: str):
        input_stream = FileStream(file_name)
        return self._format_input_stream(input_stream)

    def format_input(self, data: str):
        input_stream = InputStream(data)
        return self._format_input_stream(input_stream)


class QSharpFormatter(Formatter):
    lexer_cls = QSharpLexer
    parser_cls = QSharpParser
    listener_cls = QSharpListener
    parser_entry_fn = "target"
