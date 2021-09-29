from tokens import *

keywords = {
    'optellen'          : lambda : Add(),
    'optelt'            : lambda : Add(),
    'opgeteld'          : lambda : Add(),


    'aftrekken'         : lambda : Subtract(),
    'aftrekt'   	    : lambda : Subtract(),
    'afgetrokken'       : lambda : Subtract(),

    'vermenigvuldigen'  : lambda : Multiply(),
    'vermenigvuldigt'   : lambda : Multiply(),
    'vermenigvuldigd'   : lambda : Multiply(),

    'delen'             : lambda : Divide(),
    'deelt'             : lambda : Divide(),
    'gedeeld'           : lambda : Divide(),

    'als'               : lambda : IfStart(),
    'dan'               : lambda : IfThen(),
    'anders'            : lambda : Else(),

    'retourneert'       : lambda : Return(),

    'gesprek'           : lambda : FunctionStart(),
    'tussen'            : lambda : FunctionParamaterListIdentifier(),
    'over'              : lambda : FunctionNameIdentifier(),
    ''                  : lambda : FunctionEnd(),
    
    'waar'              : lambda : Boolean(True),
    'onwaar'            : lambda : Boolean(False),
    # ''            : lambda : (),

}