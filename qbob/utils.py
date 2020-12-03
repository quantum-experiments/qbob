"""Define general utility functions for Q#."""

from qbob.qbob import Token

def Equals(a: Token, b: Token) -> Token:
    return Token(f"({a} == {b})", "Bool")