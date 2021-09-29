from lexer import read_file, lexer
from my_parser import parser
import statements as stat

code = read_file('code.g')

token_list = lexer(code)

########## print lexer output ##########
# print('lexer output: ')
# for token in token_list: print(token)
########################################

trash, code_block, trash = parser(token_list, stat.CodeBlock())

########## print parser output ##########
print('parser output: ')
print(code_block)
#########################################