#list comprehensions enable you to implement loops in one line
#i would name it like comprehensive lists because it's more descriptive

#example 1
numbers = [4, 6, 8]
doubled = [item * 2 for item in numbers]
print(doubled)

#example 2. doesn't work
# friends = ["Samantha, Vince, Sam, Luis, Sofia"]
# start_with_s = [friend for friend in friends if friend.startswith("S")]
# print(start_with_s)