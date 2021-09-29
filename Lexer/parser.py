from typing import List,  Tuple
import tokens as tok
import statements as stat

# parser :: [Token] -> CodeBlock -> ([Token], CodeBlock)
def parser(token_list : List[tok.Token], code : stat.CodeBlock) -> Tuple[List[tok.Token], stat.CodeBlock]:
    
    if len(token_list) == 0:
        return None, code
