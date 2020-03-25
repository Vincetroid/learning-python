# ** 
# 1. collect named arguments into a dictionary (function definition)
# 2. can be use in a function call to unpack a dictionary into keyword arguments

# Case 1. Passing key value pairs and kwargs take care of destructure every key value pair. At the end puts everything in a dictionary  (sort of object)
#1st use
# def named(**kwargs):
#     print(kwargs)

# named(name="Bob", age=25)


# Case 2. Printing only the values. Now I understand, using **something means: please destructure this into every value pair inside a dictionary
# def named(name, age):
#     print(name, age)

# details = {"name": "Bob", "age":25}

#2nd use
# named(**details)


# Case 3. 
# def named(**kwargs):
#     print(kwargs)

# details = {"name": "Bob", "age": 25}

# #2nd use
# named(**details)

# # Case 4
# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="Bob", age=25)


# Case 5
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
