from typing import List, Tuple
import tokens as tok
import statements as stat

# parser :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parser(token_list : List[tok.Token], code : stat.CodeBlock, prev_tokens : List[tok.Token] = []) -> Tuple[List[tok.Token], stat.CodeBlock, List[tok.Token]]:
    
    if len(token_list) == 0:
        return None, code, None

    token, *rest = token_list
    prev_tokens.append(token)

    if isinstance(token, tok.If):
        return parser(
            rest[4:], 
            code.add_statement(
                stat.Statement(
                    stat.EqualTo(prev_tokens[-2], rest[0]),
                    stat.CodeBlock(code.nest_level+1),
                    stat.CodeBlock(code.nest_level+1)
                )
            ),
            prev_tokens
        )

    elif isinstance(token, tok.GreaterEqual):
        return parser(rest[1:], code.add_expression(stat.GreaterEqual(prev_tokens[-2], rest[0])), prev_tokens)
    elif isinstance(token, tok.GreaterThen):
        return parser(rest[1:], code.add_expression(stat.GreaterThen(prev_tokens[-2], rest[0])), prev_tokens)
    elif isinstance(token, tok.LesserEqual):
        return parser(rest[1:], code.add_expression(stat.LesserEqual(prev_tokens[-2], rest[0])), prev_tokens)
    elif isinstance(token, tok.LesserThen):
        return parser(rest[1:], code.add_expression(stat.LesserThen(prev_tokens[-2], rest[0])), prev_tokens)
    elif isinstance(token, tok.EqualTo):
        return parser(rest[1:], code.add_expression(stat.EqualTo(prev_tokens[-2], rest[0])), prev_tokens)

    elif isinstance(token, tok.Add):
        return parser(rest, code.add_expression(stat.Add(prev_tokens[-3], prev_tokens[-2])), prev_tokens)
    elif isinstance(token, tok.Subtract):
        return parser(rest, code.add_expression(stat.Subtract(prev_tokens[-3], prev_tokens[-2])), prev_tokens)
    elif isinstance(token, tok.Multiply):
        return parser(rest, code.add_expression(stat.Multiply(prev_tokens[-3], prev_tokens[-2])), prev_tokens)
    elif isinstance(token, tok.Divide):
        return parser(rest, code.add_expression(stat.Divide(prev_tokens[-3], prev_tokens[-2])), prev_tokens)
    else:
        return parser(rest, code, prev_tokens)