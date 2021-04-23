from Nodes import primitiveValue, functionValue

def createValue(type, value):
    if type == "Function":
        return functionValue.FunctionValue(value)
    
    return primitiveValue.PrimitiveValue(value)