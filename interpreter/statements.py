class Expression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Expression'

class RegularExpression(Expression):
    # __init__ :: Int -> Int -> None
    def __init__(self, left : int, right: int) -> None:
        self.left = left
        self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'RegularExpression'

class BooleanExpression(Expression):
    # __init__ :: Boolean -> Boolean -> None
    def __init__(self, left : bool, right: bool) -> None:
        self.left = left
        self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'BooleanExpression'



class Add(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mAdd \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class Subtract(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mSubtract \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class Multiply(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mMultiply \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)
        
class Divide(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mDivide \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)



class LesserEqual(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mLesserEqual \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class GreaterEqual(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mGreaterEqual \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class LesserThen(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mLesserThen \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class GreaterThen(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mGreaterThen \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)

class EqualTo(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mEqualTo \n\t\033[0;34mLeft:\n\t\t\033[37m{self.left}\n\t\033[34mRight:\n\t\t\033[37m{self.right}'.expandtabs(2)



class Statement:
    # __init__ :: Expression -> CodeBlock -> CodeBlock -> None
    def __init__(self, condition: Expression, left_code_block, right_code_block) -> None:
        self.condition = condition
        self.left_code_block = left_code_block
        self.right_code_block = right_code_block

    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'\033[1;32mif\n\t\033[0;37m{self.condition}\n\t\t\033[0;34mLeft:\n\t\t\t\033[37m{self.left_code_block}\n\t\t\033[34mRight:\n\t\t\t\033[37m{self.right_code_block}'.expandtabs(2)



class CodeBlock:
    # __init__ :: Int -> None
    def __init__(self, nest_level: int = 0) -> None:
        self.expressions = []
        self.nest_level = nest_level

    # add_expression :: Expression -> CodeBlock
    def add_expression(self, expression: Expression):
        self.expressions.append(expression)
        return self

    # add_expression :: Statement -> CodeBlock
    def add_statement(self, statement: Statement):
        self.expressions.append(statement)
        return self

    # __str__ :: None -> String
    def __str__(self) -> str:
        nstr = repeatStr("   ", self.nest_level)
        statestr = ''.join(map(lambda st: nstr + str(st) + "\n", self.expressions))
        return "\033[1;4;33mBegin Block:\n\033[0;37m" + statestr + repeatStr("   ", self.nest_level - 1) + "\033[1;4;33mEnd Block\033[0;37m"

#repeatStr :: String -> Integer -> String
def repeatStr(s : str, i : int):
    if (i <= 0):
        return ""
    return s + repeatStr(s, i - 1)