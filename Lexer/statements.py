class CodeBlock:
    # init :: Int -> None
    def __init__(self, nest_level: int = 0) -> None:
        self.nest_level = nest_level



class regularExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'undefined'

class Add(regularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Add \n\tLeft: {self.left}, Right: {self.right}'

class Add(regularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return f'Subtract \n\tLeft: {self.left}, Right: {self.right}'

class Add(regularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'undefined'
