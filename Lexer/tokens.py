class Token:
    def __init__(self):
        self.line_nr = 0
        self.char_nr = 0
    
    def __str__(self):
        return "undefined"




class BooleanExpression(Token):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "BooleanExpression"

class LesserEqual(BooleanExpression):
    def result(self):
        return self.left <= self.right

    def __str__(self):
        return "LesserEqual"

class GreaterEqual(BooleanExpression):
    def result(self):
        return self.left >= self.right

    def __str__(self):
        return "GreaterEqual"

class LesserThen(BooleanExpression):
    def result(self):
        return self.left > self.right

    def __str__(self):
        return "LesserThen"

class GreaterThen(BooleanExpression):
    def result(self):
        return self.left > self.right

    def __str__(self):
        return "GreaterThen"

class Add(Token):
    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right

    def __str__(self):
        return "Add"

class Subtract(Token):
    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right

    def __str__(self):
        return "Subtract"

class Variable(Token):
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return ("Variable " + self.name)