import ply.lex as lex
import ply.yacc as yacc


tokens = ['IF', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 
          'EQ', 'LT', 'GT', 'LE', 'GE', 'NEQ', 'PLUS', 'MINUS', 'SEMICOLON']


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_SEMICOLON = r';'


t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='


reserved = {
    'if': 'IF'
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t


def t_COMMENT(t):
    r'//.*'
    pass  


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()


precedence = (
    ('left', 'PLUS', 'MINUS'), 
    ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'),  
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
    p[0] = "Valid condition"

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression'''
    p[0] = "Valid expression"

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    p[0] = "Valid assignment"

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = "Valid block"

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement
                      | '''  
    if len(p) == 1:
        p[0] = "Empty statement list"
    elif len(p) == 2:
        p[0] = "Valid statement list with one statement"
    else:
        p[0] = "Valid statement list"

def p_statement(p):
    '''statement : assignment
                 | if'''
    p[0] = "Valid statement"

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (line {p.lineno})")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()


def parse_input():
    while True:
        print("\nEnter code to check syntax (or type 'exit' to quit):")
        try:
            user_input = input()
        except EOFError:
            print("\nExiting.")
            break

        if user_input.lower() == 'exit':
            print("Exiting.")
            break

        try:
            result = parser.parse(user_input)
            if result:
                print(f"Parse result: {result}")
            else:
                print("No syntax errors found.")
        except Exception as e:
            print(f"Error: {e}")


parse_input()
