from typing import List
import re
from keywords import keywords
from name_database import name_database
from tokens import *

def lexer(code : List[str], token_list : List[Token] = []):
    word, *code_rest = code
    if word in keywords:
        token_list.append(keywords.get(word, "fuck")())
    elif word in name_database:
        token_list.append(Variable(word))
        
    if code_rest != []:
        return lexer(code_rest, token_list)
    else:
        return token_list



with open('code.g', 'r') as file:
    code = file.read()
code = re.split(', |\.\n| |\.', code)

token_list = lexer(code)
for token in token_list:
    print(token.__str__())
print(token_list[0].request_name())