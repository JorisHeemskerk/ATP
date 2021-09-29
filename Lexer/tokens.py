class Token:
    # __init__ :: None -> None
    def __init__(self) -> None:
        self.line_nr = 0
        self.char_nr = 0

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'undefined'



class FunctionStart(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'FunctionStart'

class FunctionParamaterListIdentifier(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'FunctionParamaterListIdentifier'

class FunctionNameIdentifier(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'FunctionNameIdentifier'

class FunctionName(Token):
    # __init__ :: String -> None
    def __init__(self, value : str) -> None:
        self.value = value

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'FunctionName: ' + self.value

class FunctionEnd(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'FunctionEnd'



class IfStart(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'IfStart'

class IfThen(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'IfThen'

class Else(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Else'



class BooleanExpression(Token):
    # def __init__(self, left = 0, right = 0):
    #     self.left = left
    #     self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'BooleanExpression'

class LesserEqual(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'LesserEqual'

class GreaterEqual(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'GreaterEqual'

class LesserThen(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'LesserThen'

class GreaterThen(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'GreaterThen'

class Equals(BooleanExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Equals'





class RegularExpression(Token):
    # def __init__(self, left = 0, right = 0):
    #     self.left = left
    #     self.right = right

    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'RegularExpression'

class Add(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Add'

class Subtract(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Subtract'

class Multiply(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Multiply'

class Divide(RegularExpression):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Divide'






class Variable(Token):
    # __init__ :: String -> Int -> None
    def __init__(self, name : str, value = 0) -> None:
        self.name = name
        self.value = value

    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('Variable: ' + self.name)

class Int(Token):
    # __init__ :: Int -> None
    def __init__(self, value : int) -> None:
        self.value = value

    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('Int: ' + str(self.value))

class String(Token):
    # __init__ :: String -> None
    def __init__(self, value : str) -> None:
        self.value = value

    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('String: ' + self.value)

class Boolean(Token):
    # __init__ :: Boolean -> None
    def __init__(self, value : bool) -> None:
        self.value = value

    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('Boolean: ' + self.value)



class Return(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('Return')

class EndLine(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('EndLine')