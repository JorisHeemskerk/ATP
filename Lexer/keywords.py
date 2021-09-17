from tokens import *

keywords = {
    'optellen' : lambda : Add(),
    'aftrekken' : lambda : Subtract(),
    'vermenigvuldigen' : lambda : Multiply(),
    'delen' : lambda : Divide(),
    'gesprek' : lambda : Function(),
    '' : lambda : FunctionEnd()
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),

}