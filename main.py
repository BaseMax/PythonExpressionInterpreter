from lexer import Lexer
from parser import Parser

while True:
	text = input("calc > ")
	lexer = Lexer(text)
	tokens = lexer.generate_tokens()
	print(list(tokens))
	parser = Parser(tokens)
	tree = parser.parse()
	print(tree)
