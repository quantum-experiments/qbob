"""Define a representation of a typed token in Q# code."""

class Token:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def __getitem__(self, key: int) -> 'Token':
        assert self.type.endswith("[]")
        return Token(f"{self.name}[{key}]", self.type[:-2])
