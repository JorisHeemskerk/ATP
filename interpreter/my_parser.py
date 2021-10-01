from typing import List, Tuple
import tokens as tok
import statements as stat
import sys

def find_expression(rest : List[tok.Token], prev_tokens : List[tok.Token] = []) -> Tuple[stat.Expression, List[tok.Token], List[tok.Token]]:
    token = prev_tokens[-1]
    if isinstance(token, tok.GreaterEqual):
        return stat.GreaterEqual(prev_tokens[-2], rest[0]), rest[1:], prev_tokens
    elif isinstance(token, tok.GreaterThen):
        return stat.GreaterThen(prev_tokens[-2], rest[0]), rest[1:], prev_tokens
    elif isinstance(token, tok.LesserEqual):
        return stat.LesserEqual(prev_tokens[-2], rest[0]), rest[1:], prev_tokens
    elif isinstance(token, tok.LesserThen):
        return stat.LesserThen(prev_tokens[-2], rest[0]), rest[1:], prev_tokens
    elif isinstance(token, tok.EqualTo):
        return stat.EqualTo(prev_tokens[-2], rest[0]), rest[1:], prev_tokens

    elif isinstance(token, tok.Add):
        return stat.Add(prev_tokens[-3], prev_tokens[-2]), rest, prev_tokens
    elif isinstance(token, tok.Subtract):
        return stat.Subtract(prev_tokens[-3], prev_tokens[-2]), rest, prev_tokens
    elif isinstance(token, tok.Multiply):
        return stat.Multiply(prev_tokens[-3], prev_tokens[-2]), rest, prev_tokens
    elif isinstance(token, tok.Divide):
        return stat.Divide(prev_tokens[-3], prev_tokens[-2]), rest, prev_tokens
    else:
        return None, rest, prev_tokens


def find_statement(rest : List[tok.Token], prev_tokens : List[tok.Token] = []) ->stat.Statement:
    condition, rest, prev_tokens = find_expression(rest, prev_tokens)
    if condition == None:
        sys.exit('\033[1;31mFatal error: \033[0;31mEén van je if-statements heeft geen conditie, sukkel.\033[37m')
    rest, left_code_block, prev_tokens = parser(rest, stat.CodeBlock(), prev_tokens)
    rest, right_code_block, prev_tokens = parser(rest, stat.CodeBlock(), prev_tokens)
    
    return stat.Statement(condition, left_code_block, right_code_block)




# parser :: [Token] -> CodeBlock -> [Token] -> ([Token], CodeBlock)
def parser(token_list : List[tok.Token], code : stat.CodeBlock, prev_tokens : List[tok.Token] = []) -> Tuple[List[tok.Token], stat.CodeBlock, List[tok.Token]]:
    
    if len(token_list) == 0:
        return None, code, None

    token, *rest = token_list
    prev_tokens.append(token)

    # if isinstance(token, tok.If):
    #     return parser(
    #         rest[4:], 
    #         code.add_statement(
    #             stat.Statement(
    #                 stat.EqualTo(prev_tokens[-2], rest[0]),
    #                 stat.CodeBlock(code.nest_level+1),
    #                 stat.CodeBlock(code.nest_level+1)
    #             )
    #         ),
    #         prev_tokens
    #     )

    if isinstance(token, tok.If):
        find_statement(rest, code, prev_tokens)
    else:
        return parser(rest, code, prev_tokens)