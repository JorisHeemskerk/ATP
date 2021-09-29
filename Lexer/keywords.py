from tokens import *

keywords = {
    'optellen'          : lambda : Add(),
    'Optellen'          : lambda : Add(),
    'optelt'            : lambda : Add(),
    'Optelt'            : lambda : Add(),
    'opgeteld'          : lambda : Add(),
    'Opgeteld'          : lambda : Add(),


    'aftrekken'         : lambda : Subtract(),
    'Aftrekken'         : lambda : Subtract(),
    'aftrekt'   	    : lambda : Subtract(),
    'Aftrekt'           : lambda : Subtract(),
    'afgetrokken'       : lambda : Subtract(),
    'Afgetrokken'       : lambda : Subtract(),
    'aftrekken'         : lambda : Subtract(),

    'vermenigvuldigen'  : lambda : Multiply(),
    'Vermenigvuldigen'  : lambda : Multiply(),
    'vermenigvuldigt'   : lambda : Multiply(),
    'Vermenigvuldigt'   : lambda : Multiply(),
    'vermenigvuldigd'   : lambda : Multiply(),
    'Vermenigvuldigd'   : lambda : Multiply(),

    'delen'             : lambda : Divide(),
    'Delen'             : lambda : Divide(),
    'deelt'             : lambda : Divide(),
    'Deelt'             : lambda : Divide(),
    'gedeeld'           : lambda : Divide(),
    'Gedeeld'           : lambda : Divide(),

    'gesprek'           : lambda : Function(),
    ''                  : lambda : FunctionEnd()
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),
    # '' : lambda : (),

}