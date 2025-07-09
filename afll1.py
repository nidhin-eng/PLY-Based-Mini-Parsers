import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = ['IF', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 
          'EQ', 'LT', 'GT', 'LE', 'GE', 'NEQ', 'PLUS', 'MINUS', 'SEMICOLON']

# Define token patterns
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='  # Assignment operator
t_PLUS = r'\+'
t_MINUS = r'-'
t_SEMICOLON = r';'

# Comparison operators
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='

# Reserved keywords
reserved = {
    'if': 'IF'
}

# Identifier rule
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved keywords
    return t

# Number rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert to an integer
    return t

# Ignore single-line comments (e.g., // comment)
def t_COMMENT(t):
    r'//.*'
    pass  # Ignore comments

# Track newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parser

# Define precedence of operators
precedence = (
    ('left', 'PLUS', 'MINUS'),  # Addition and subtraction
    ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'),  # Comparison operators
)

def p_if(p):
    '''if : IF LPAREN condition RPAREN block'''
    p[0] = "Valid if statement"

def p_condition(p):
    '''condition : expression EQ expression
                 | expression NEQ expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression'''
    pass

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression'''
    pass

# Assignment rule for the block
def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    pass

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement
                      | '''  # This allows an empty block (no statements)
    pass

def p_statement(p):
    '''statement : assignment
                 | if'''
    pass

# Handle syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test input for a C++ style if statement
test_code = """
if (x == 10) {
    x = x + 1;
}
"""

# Run the lexer and parser on the test input
result = parser.parse(test_code)
print(result)