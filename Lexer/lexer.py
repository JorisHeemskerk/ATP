from typing import List
import re
from keywords import keywords
from name_database import name_database
from tokens import *

def lexer(code : List[str], token_list : List[Token] = []):
    word, *code_rest = code
    if word in keywords:
        token_list.append(keywords.get(word)())
    elif word[0] == '\"' and word[-1] == '\"':
        token_list.append(String(word))
    elif word.isdecimal():
        token_list.append(Int(int(word)))
    elif word == "groter" and code_rest[0] == "dan":
        token_list.append(GreaterThen())
    elif word == "groter" and code_rest[0] == "dan" and code_rest[1] == "of" and code_rest[2] == "gelijk":
        token_list.append(GreaterEqual())
    elif word == "groter" and code_rest[0] == "dan":
        token_list.append(LesserEqual())
    elif word == "kleiner" and code_rest[0] == "dan" and code_rest[1] == "of" and code_rest[2] == "gelijk":
        token_list.append(LesserEqual())
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
