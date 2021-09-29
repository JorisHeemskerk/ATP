import tokens as tok

keywords = {
    'optellen'          : lambda : tok.Add(),
    'optelt'            : lambda : tok.Add(),
    'opgeteld'          : lambda : tok.Add(),


    'aftrekken'         : lambda : tok.Subtract(),
    'aftrekt'   	    : lambda : tok.Subtract(),
    'afgetrokken'       : lambda : tok.Subtract(),

    'vermenigvuldigen'  : lambda : tok.Multiply(),
    'vermenigvuldigt'   : lambda : tok.Multiply(),
    'vermenigvuldigd'   : lambda : tok.Multiply(),

    'delen'             : lambda : tok.Divide(),
    'deelt'             : lambda : tok.Divide(),
    'gedeeld'           : lambda : tok.Divide(),

    'als'               : lambda : tok.If(),
    'dan'               : lambda : tok.Then(),
    'anders'            : lambda : tok.Else(),

    'retourneert'       : lambda : tok.Return(),

    'gesprek'           : lambda : tok.FunctionStart(),
    'tussen'            : lambda : tok.FunctionParamaterListIdentifier(),
    'over'              : lambda : tok.FunctionNameIdentifier(),
    ''                  : lambda : tok.FunctionEnd()
}