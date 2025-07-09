import ply.lex as lex
import ply.yacc as yacc


tokens = ['IF', 'WHILE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
          'IDENTIFIER', 'ASSIGN', 'NUMBER', 'EQ', 'LT', 'GT', 
          'LE', 'GE', 'NEQ', 'PLUS', 'MINUS', 'SEMICOLON']


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
    'if': 'IF',
    'while': 'WHILE'
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


def p_program(p):
    '''program : statement_list'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement
                      | '''  
    pass

def p_if(p):
    '''statement : IF LPAREN condition RPAREN block'''
    print("Valid if statement")  

def p_while(p):
    '''statement : WHILE LPAREN condition RPAREN block'''
    print("Valid while statement")  

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


def p_assignment(p):
    '''statement : IDENTIFIER ASSIGN expression SEMICOLON'''
    pass

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    pass


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()


def test_parser():
    input_code = input("Enter your code to check for valid if and while statements:\n")
    result = parser.parse(input_code)
    if result:
        print(result)
    else:
        print("The input code is not valid.")

test_parser()
