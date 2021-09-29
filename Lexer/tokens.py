class Token:
    def __init__(self) -> None:
        self.line_nr = 0
        self.char_nr = 0
    
    def __str__(self) -> str:
        return 'undefined'



class FunctionStart(Token):
    def __str__(self) -> str:
        return 'FunctionStart'

class FunctionParamaterListIdentifier(Token):
    def __str__(self) -> str:
        return 'FunctionParamaterListIdentifier'

class FunctionNameIdentifier(Token):
    def __str__(self) -> str:
        return 'FunctionNameIdentifier'

class FunctionName(Token):
    def __init__(self, value : str) -> None:
        self.value = value

    def __str__(self) -> str:
        return 'FunctionName: ' + self.value

class FunctionEnd(Token):
    def __str__(self) -> str:
        return 'FunctionEnd'



class BooleanExpression(Token):
    # def __init__(self, left = 0, right = 0):
    #     self.left = left
    #     self.right = right

    def __str__(self) -> str:
        return 'BooleanExpression'

class LesserEqual(BooleanExpression):
    def __str__(self) -> str:
        return 'LesserEqual'

class GreaterEqual(BooleanExpression):
    def __str__(self) -> str:
        return 'GreaterEqual'

class LesserThen(BooleanExpression):
    def __str__(self) -> str:
        return 'LesserThen'

class GreaterThen(BooleanExpression):
    def __str__(self) -> str:
        return 'GreaterThen'





class RegularExpression(Token):
    # def __init__(self, left = 0, right = 0):
    #     self.left = left
    #     self.right = right

    def __str__(self) -> str:
        return 'RegularExpression'

class Add(Token):
    def __str__(self) -> str:
        return 'Add'

class Subtract(Token):
    def __str__(self) -> str:
        return 'Subtract'

class Multiply(Token):
    def __str__(self) -> str:
        return 'Multiply'

class Divide(Token):
    def __str__(self) -> str:
        return 'Divide'






class Variable(Token):
    def __init__(self, name : str, value = 0) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return ('Variable ' + self.name)




class Int(Token):
    def __init__(self, value : int) -> None:
        self.value = value

    def __str__(self) -> str:
        return ('Int ' + str(self.value))

class String(Token):
    def __init__(self, value : str) -> None:
        self.value = value

    def __str__(self) -> str:
        return ('String ' + self.value)