def multiply(*args):
    product = 1
    for arg in args:
        product = product * arg 

    return product

def apply(*args, operator):
    if operator == "*": 
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(3,2,5, operator="*"))   