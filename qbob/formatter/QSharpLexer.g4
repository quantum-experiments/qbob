lexer grammar QSharpLexer;

// Keywords

Adj : 'Adj';
AdjointFunctor : 'Adjoint';
AdjointGenerator : 'adjoint';
And : 'and';
Apply : 'apply';
As : 'as';
Auto : 'auto';
BigInt : 'BigInt';
Body : 'body';
Bool : 'Bool';
Borrowing : 'borrowing';
ControlledFunctor : 'Controlled';
ControlledGenerator : 'controlled';
Ctl : 'Ctl';
Distribute : 'distribute';
Double : 'Double';
Elif : 'elif';
Else : 'else';
Fail : 'fail';
BFalse : 'false';
Fixup : 'fixup';
For : 'for';
Function : 'function';
If : 'if';
In : 'in';
Int : 'Int';
Internal : 'internal';
Intrinsic : 'intrinsic';
Invert : 'invert';
Is : 'is';
Let : 'let';
Mutable : 'mutable';
Namespace : 'namespace';
New : 'new';
Newtype : 'newtype';
Not : 'not';
One : 'One';
Open : 'open';
Operation : 'operation';
Or : 'or';
Pauli : 'Pauli';
PauliI : 'PauliI';
PauliX : 'PauliX';
PauliY : 'PauliY';
PauliZ : 'PauliZ';
Qubit : 'Qubit';
Range : 'Range';
Repeat : 'repeat';
Result : 'Result';
Return : 'return';
Self : 'self';
Set : 'set';
String : 'String';
BTrue : 'true';
Unit : 'Unit';
Until : 'until';
Using : 'using';
While : 'while';
Within : 'within';
Zero : 'Zero';

// Operators

AndEqual : 'and=';
ArrowLeft : '<-';
ArrowRight : '->';
Asterisk : '*';
AsteriskEqual : '*=';
At : '@';
Bang : '!';
BraceLeft : '{' -> pushMode(DEFAULT_MODE);
BraceRight : '}';
BracketLeft : '[';
BracketRight : ']';
Caret : '^';
CaretEqual : '^=';
Colon : ':';
Comma : ',';
DollarQuote : '$"' -> pushMode(INTERPOLATED);
Dot : '.';
DoubleColon : '::';
DoubleDot : '..';
DoubleEqual : '==';
DoubleQuote : '"' -> pushMode(STRING);
Ellipsis : '...';
Equal : '=';
FatArrowRight : '=>';
Greater : '>';
GreaterEqual : '>=';
Less : '<';
LessEqual : '<=';
Minus : '-';
MinusEqual : '-=';
NotEqual : '!=';
OrEqual : 'or=';
ParenLeft : '(';
ParenRight : ')';
Percent : '%';
PercentEqual : '%=';
Pipe : '|';
Plus : '+';
PlusEqual : '+=';
Question : '?';
Semicolon : ';';
Slash : '/';
SlashEqual : '/=';
TripleAmpersand : '&&&';
TripleAmpersandEqual : '&&&=';
TripleCaret : '^^^';
TripleCaretEqual : '^^^=';
TripleGreater : '>>>';
TripleGreaterEqual : '>>>=';
TripleLess : '<<<';
TripleLessEqual : '<<<=';
TriplePipe : '|||';
TriplePipeEqual : '|||=';
TripleTilde : '~~~';
Underscore : '_';
With : 'w/';
WithEqual : 'w/=';

// Literals

fragment Digit : [0-9];

IntegerLiteral
    : Digit+
    | ('0x' | '0X') [0-9a-fA-F]+
    | ('0o' | '0O') [0-7]+
    | ('0b' | '0B') [0-1]+
    ;

BigIntegerLiteral : IntegerLiteral ('L' | 'l');

DoubleLiteral
    : Digit+ '.' Digit+
    | '.' Digit+
    // "n.." should be interpreted as an integer range, not the double "n." followed by a dot.
    | Digit+ '.' { InputStream.LA(1) != '.' }?
    | Digit+ ('e' | 'E') Digit+
    ;

Identifier : IdentifierStart IdentifierContinuation*;

IdentifierStart
    : Underscore
    | [\p{Letter}]
    | [\p{Letter_Number}]
    ;

IdentifierContinuation
    : [\p{Connector_Punctuation}]
    | [\p{Decimal_Number}]
    | [\p{Format}]
    | [\p{Letter}]
    | [\p{Letter_Number}]
    | [\p{Nonspacing_Mark}]
    | [\p{Spacing_Mark}]
    ;

TypeParameter : '\'' Identifier;

Whitespace : (' ' | '\n' | '\r' | '\t')+ -> channel(HIDDEN);

Comment : '//' ~('\n' | '\r')* -> channel(HIDDEN);

Invalid : . -> channel(HIDDEN);

// Strings

mode STRING;

StringEscape : '\\' .;

StringText : ~('"' | '\\')+;

StringDoubleQuote : '"' -> popMode;

mode INTERPOLATED;

InterpStringEscape : '\\' .;

InterpBraceLeft : '{' -> pushMode(DEFAULT_MODE);

InterpStringText : ~('\\' | '"' | '{')+;

InterpDoubleQuote : '"' -> popMode;
