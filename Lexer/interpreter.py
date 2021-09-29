from lexer import read_file, lexer

code = read_file('code.g')

token_list = lexer(code)

########## print lexer output ##########
# print('lexer output: ')
# for token in token_list: print(token)
########################################