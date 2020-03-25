def multiply(*args):
    product = 1
    for arg in args:
        product = product * arg 

    return product

result = multiply(1, 3, 5, 7)
print(result)


#example 2
#define add function with 2 arguments n1 and n2
def add(n1, n2):
    return n1 + n2

#define a list (array) of 2 numbers called nums
nums = [3, 5]

#use add function passing nums as variable and causing a destructuring
print(add(*nums))

