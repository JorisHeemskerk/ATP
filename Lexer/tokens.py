class Token:
    def __init__(self):
        self.line_nr = 0
        self.char_nr = 0
    
    def __str__(self):
        return "undefined"

class Function(Token):
    def __str__(self):
        return "Function"
class FunctionEnd(Token):
    def __str__(self):
        return "FunctionEnd"


class BooleanExpression(Token):
    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right

    def solve_sides(self):
        try:
            self.left = self.left.calculate()
        except Exception:
            pass
        try:
            self.right = self.right.calculate()
        except Exception:
            pass

    def __str__(self):
        return "BooleanExpression"

class LesserEqual(BooleanExpression):
    def calculate(self):
        self.solve_sides()
        return self.left <= self.right

    def __str__(self):
        return "LesserEqual"

class GreaterEqual(BooleanExpression):
    def calculate(self):
        self.solve_sides()
        return self.left >= self.right

    def __str__(self):
        return "GreaterEqual"

class LesserThen(BooleanExpression):
    def calculate(self):
        self.solve_sides()
        return self.left > self.right

    def __str__(self):
        return "LesserThen"

class GreaterThen(BooleanExpression):
    def calculate(self):
        self.solve_sides()
        return self.left > self.right

    def __str__(self):
        return "GreaterThen"





class RegularExpression(Token):
    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right

    def solve_sides(self):
        try:
            self.left = self.left.calculate()
        except Exception:
            pass
        try:
            self.right = self.right.calculate()
        except Exception:
            pass

    def __str__(self):
        return "RegularExpression"

class Add(Token):
    def calculate(self):
        self.solve_sides()
        return self.left + self.right
    
    def __str__(self):
        return "Add"

class Subtract(Token):
    def calculate(self):
        self.solve_sides()
        return self.left - self.right

    def __str__(self):
        return "Subtract"

class Multiply(Token):
    def calculate(self):
        self.solve_sides()
        return self.left * self.right

    def __str__(self):
        return "Multiply"

class Divide(Token):
    def calculate(self):
        self.solve_sides()
        return self.left / self.right

    def __str__(self):
        return "Divide"






class Variable(Token):
    def __init__(self, name : str, value = 0):
        self.name = name
        self.value = value

    def __str__(self):
        return ("Variable " + self.name)




class Int(Token):
    def __init__(self, value : int):
        self.value = value

    def __str__(self):
        return ("Int " + str(self.value))

class String(Token):
    def __init__(self, value : str):
        self.value = value

    def __str__(self):
        return ("String " + self.value)