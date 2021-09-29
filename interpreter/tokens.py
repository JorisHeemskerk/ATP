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



class If(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'If'

class Then(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Then'

class Else(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Else'



class LesserEqual(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'LesserEqual'

class GreaterEqual(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'GreaterEqual'

class LesserThen(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'LesserThen'

class GreaterThen(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'GreaterThen'

class Equals(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Equals'



class Add(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Add'

class Subtract(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Subtract'

class Multiply(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return 'Multiply'

class Divide(Token):
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
        return ('Boolean: ' + str(self.value))



class Return(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('Return')

class EndLine(Token):
    # __str__ :: None -> String
    def __str__(self) -> str:
        return ('EndLine')