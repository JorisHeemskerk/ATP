class Token:
    def __init__(self):
        self.line_nr = 0
        self.char_nr = 0
    
    def __str__(self):
        return "undefined"

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

    def request_name(self):
        return self.name

    def __str__(self):
        return "Variable"