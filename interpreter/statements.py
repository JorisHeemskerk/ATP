class RegularExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'undefined'
        

class CodeBlock:
    # init :: Int -> None
    def __init__(self, nest_level: int = 0) -> None:
        self.expression = []
        self.nest_level = nest_level

    # add_regular_expression :: RegularExpression -> CodeBlock
    def add_regular_expression(self, expression: RegularExpression):
        self.expression.append(expression)
        return self

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Yet to be added'




class Add(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Add \n\tLeft: {self.left}, Right: {self.right}'

class Subtract(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Subtract \n\tLeft: {self.left}, Right: {self.right}'

class Multiply(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Multiply \n\tLeft: {self.left}, Right: {self.right}'
        
class Devide(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Devide \n\tLeft: {self.left}, Right: {self.right}'