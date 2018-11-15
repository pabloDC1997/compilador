from lexer import Lexer
from parser1 import Parser

# Aluno: Pablo Dias Couto
# Mat: 20142003301045
f = open("codigo.txt", "r")

if f.mode == "r":
    text_input = f.read()
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser().parse(tokens)
