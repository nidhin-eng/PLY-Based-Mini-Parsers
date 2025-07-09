import ply.lex as lex
import ply.yacc as yacc

# Lexer
tokens = ['IF', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 
          'EQ', 'LT', 'GT', 'LE', 'GE', 'NEQ', 'PLUS', 'MINUS', 'SEMICOLON', 'COMMA', 'TYPE', 'RETURN']

# Define token patterns
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='  # Assignment operator
t_PLUS = r'\+'
t_MINUS = r'-'
t_SEMICOLON = r';'
t_COMMA = r','

# Comparison operators
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='

# Reserved keywords
reserved = {
    'if': 'IF',
    'int': 'TYPE',
    'void': 'TYPE',
    'float': 'TYPE',
    'return': 'RETURN'
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

# Function definition rule
def p_function_definition(p):
    '''function_definition : TYPE IDENTIFIER LPAREN parameter_list RPAREN block'''
    p[0] = f"Function {p[2]} defined with parameters {p[4]}"

# Parameter list rule
def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                      | parameter
                      | '''
    # Empty production allows no parameters
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Parameter rule
def p_parameter(p):
    '''parameter : TYPE IDENTIFIER'''
    p[0] = (p[1], p[2])  # Return parameter as a tuple of (type, name)

# If statement rule
def p_if(p):
    '''if : IF LPAREN condition RPAREN block'''
    p[0] = "Valid if statement"

# Condition rule for comparisons
def p_condition(p):
    '''condition : expression EQ expression
                 | expression NEQ expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression'''
    pass

# Expression rule for arithmetic and identifiers
def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression'''
    pass

# Assignment rule for statements inside the block
def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    pass

# Return statement rule
def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON'''
    pass

# Block of code with statements
def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    pass

# List of statements within a block
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Statements allowed in the block
def p_statement(p):
    '''statement : assignment
                 | if
                 | return_statement
                 | function_definition'''
    pass

# Handle syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test input for a function definition with an if statement and return
test_code = """
int myFunction(int a, int b) {
    if (a == b) {
        a = a + 1;
    }
    return a;
}
"""

# Run the lexer and parser on the test input
result = parser.parse(test_code)
print(result)
