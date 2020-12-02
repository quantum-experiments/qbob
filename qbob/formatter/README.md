# Q# Formatter

This is a Python3 implementation of a Q# parser based on the [QsFmt](http://www.github.com/samarsha/qsfmt) formatter. This implementation uses the same grammar but does not generate an Abstract Syntax Tree. Instead, we use a Listener that formats the code straight from the generated Parse Tree.

## Parser and Lexer

The Parser and Lexer used for this formatter are generated using [ANTLR4](http://www.antlr4.org), a parser generator. ANTLR4 supports generating parsers in many different languages. Here, we have generated the code in Python3.

The grammar is defined in the following files:

- QSharpLexer.g4

- QSharpParser.g4

These are based on the grammar built by Sarah Marshall for the F#-based [QsFmt](http://www.github.com/samarsha/qsfmt) formatter. Note that whenever you make changes to these files, you have to make sure to re-generate the lexer and parser and possibly modify the listener to be compatible with said changes.

To read more about what Lexers and Parsers are and how they work, I would recommend checking out this [blog post](https://ruslanspivak.com/lsbasi-part7/).

### Code generation

Most of the code in this module is auto-generated using `antlr4`. To generate a new Parser and Lexer, make sure [antlr4](http://www.antlr4.org) is installed on your system.

To install `antlr4` using `conda`, run

```bash
conda install -c conda-force antlr4
```

To install the `antlr4` runtime for Python 3, run

```bash
conda install -c carta antlr4-python3-runtime
```

Finally, to generate the code, run

```bash
antlr4 -Dlanguage=Python3 QSharpLexer.g4
antlr4 -Dlanguage=Python3 QSharpParser.g4
```

This will create the following files:

- QsharpLexer.py
- QsharpLexer.interp
- QsharpLexer.tokens
- QsharpParser.py
- QsharpParser.interp
- QsharpParser.tokens
- QsharpParserListener.py
