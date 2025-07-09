import ply.lex as lex
import ply.yacc as yacc


tokens = ['IF', 'ELSE', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 
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
    'if': 'IF',
    'else': 'ELSE'
}


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t




t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()


def p_ifelse(p):
    '''ifelse : IF LPAREN condition RPAREN block else_part'''
    p[0] = "Valid if-else statement"

def p_else_part(p):
    '''else_part : ELSE block
                 | empty'''
    pass

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
                  | IDENTIFIER PLUS NUMBER
                  | IDENTIFIER MINUS NUMBER'''
    pass


def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON'''
    pass

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    pass

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    pass

def p_statement(p):
    '''statement : assignment
                 | ifelse'''
    pass

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()


def test_parser():
    input_code = input("Enter your code to check if it's a valid if-else statement:\n")
    result = parser.parse(input_code)
    if result:
        print(result)
    else:
        print("The input code is not valid.")


test_parser()
