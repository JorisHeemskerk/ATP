from typing import List, Tuple
import tokens as tok
import statements as stat

# parser :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parser(token_list : List[tok.Token], code : stat.CodeBlock, prev_tokens : List[tok.Token] = []) -> Tuple[List[tok.Token], stat.CodeBlock, List[tok.Token]]:
    
    if len(token_list) == 0:
        return None, code, None

    token, *rest = token_list
    prev_tokens.append(token)

    if isinstance(token, tok.Add):
        return parser(rest, code.add_regular_expression(stat.Add(prev_tokens[-3], prev_tokens[-2]), prev_tokens))
    else:
        return parser(rest, code, prev_tokens)