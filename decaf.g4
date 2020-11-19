grammar decaf;

// PARSER RULES

program : 'class' 'Program' '{' (declaration)* '}' EOF;

declaration : structDeclaration | varDeclaration | methoDeclaration;
varDeclaration : varType ID ';' | varType ID '[' NUM ']' ';';
structDeclaration : 'struct' ID '{' (varDeclaration)* '}';
varType : 'int' | 'char' | 'boolean' | 'struct' ID | structDeclaration | 'void';
methoDeclaration : methodType ID '(' (parameter)* ')' block;
methodType : 'int' | 'char' | 'boolean'| 'void';
parameter : parametertype ID | parametertype ID '[' ']';
parametertype : 'int' | 'char' | 'boolean';
block: '{' (varDeclaration)* (statement)* '}';
statement : 'if' '(' expression ')' if_block = block ('else' else_block = block)? #ifstmt
| 'while' '(' expression ')' condition = block #whilestmt
| 'return' (expression)? ';' #returnstmt
| methodCall ';' #methodstmt
| block #blockstmt
| left = location '=' right = expression ';' #locationstmt
| (expression)? ';'#expressionstmt
;
location : (ID | ID '[' expression ']') ('.' location)?;

expression : location #locexpr
| methodCall #methodexpr
| literal #literalexpr
// | expression p_arith_op expression #p_arithexpr
// | expression op expression #opexpr
| '-' expression #minusexpr
| '!' expression #factoexpr
| '(' expression ')' #corchexpr
| left = expression p_arith_op right = expression #p_arith_op_expr
| left = expression arith_op right = expression #arith_op_expr
| left = expression rel_op right = expression #rel_op_expr
| left = expression eq_op right = expression #eq_op_expr
| left = expression cond_op right = expression #cond_op_expr
;
methodCall : ID '(' (arg)* ')';
arg : expression;
// op : p_arith_op | arith_op | rel_op | eq_op | cond_op;
p_arith_op:  '*' | '/'| '%';
arith_op : '+' | '-';
rel_op : '<' | '>' | '<=' | '>=';
eq_op : '==' | '!=';
cond_op : '&&' | '||';
literal : int_Literal | char_Literal | bool_Literal;
int_Literal : NUM;
char_Literal : CHAR ;
bool_Literal : 'true' | 'false';


// LEXER RULES

fragment DIGIT: [0-9];

fragment LETTER: [a-z] | [A-Z];
NUM: DIGIT (DIGIT)*;
ID: LETTER (LETTER | DIGIT)*;
CHAR: '\''LETTER'\'';
BLANK: [ \t\r\n\f]+ -> skip ;



