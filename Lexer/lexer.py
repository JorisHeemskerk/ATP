from os import truncate
from typing import List
import re


keywords = {
    'bob' : lambda : Add(4,2),
    'optellen' : lambda : Add(3,6)
}

class Token:
    def __init__(self):
        self.line_nr = 0
        self.char_nr = 0
    
    def __str__(self):
        return "undefined"

class Add(Token):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Add"



def lexer(code : list[str], token_list : list[Token]):
    word, *code_rest = code
    if(word in keywords):
        print(keywords.get(word, "fuck")())
        token_list.append(keywords.get(word, "fuck")())
        

    if(code_rest != []):
        lexer(code_rest, token_list)
    else:
        print("F")
        return token_list











with open('code.g', 'r') as file:
    code = file.read()
code = re.split(', |\.\n| |\.', code)

# token_list = List[str]
token_list = lexer(code, [])
print(token_list)