from typing import List
import re
from keywords import keywords
from name_database import name_database
from tokens import *

def list_to_string(code : List[str], code_string : str = '') -> str:
    if code != []:
        return list_to_string (code[1:], code_string + ' ' + code[0])
    return code_string


def contains(code : List[str], substring : str) -> bool:
    # code_string : str = ' '.join([word for word in code])
    code_string = list_to_string(code)
    code_string = code_string.lower()
    if code_string.find(substring) == 1:
        return True
    return False


def lexer(code : List[str], token_list : List[Token] = []) -> List[Token]:
    endline = False

    word, *code_rest = code
    lower_word = word.lower()

    try:
        if word[-1] == '.':
            word = word[:-1]
            endline = True
    except:
        pass

    if lower_word in keywords:
        token_list.append(keywords.get(word)())
    elif word[0] == '\"' and word[-1] == '\"':
        token_list.append(String(word))
    elif word[0] == '\'' and word[-1] == '\'':
        token_list.append(FunctionName(word))
    elif word.isdecimal():
        token_list.append(Int(int(word)))

    elif contains(code, "niet waar"):
        token_list.append(Boolean(False))
        code_rest = code_rest[1:]
    elif contains(code, "gelijk aan"):
        token_list.append(GreaterEqual())
        code_rest = code_rest[1:]
    elif contains(code, "groter dan of gelijk aan"):
        token_list.append(GreaterEqual())
        code_rest = code_rest[4:]
    elif contains(code, "groter dan"):
        token_list.append(GreaterThen())
        code_rest = code_rest[1:]
    elif contains(code, "kleiner dan of gelijk aan"):
        token_list.append(LesserEqual())
        code_rest = code_rest[4:]
    elif contains(code, "kleiner dan"):
        token_list.append(LesserEqual())
        code_rest = code_rest[1:]
    elif word in name_database:
        token_list.append(Variable(word))
        
    if endline:
        token_list.append(EndLine())

    if code_rest != []:
        return lexer(code_rest, token_list)
    else:
        return token_list



with open('code.g', 'r') as file:
    code = file.read()
code = re.split(', |\n| ', code)

token_list = lexer(code)
for token in token_list: print(token)
