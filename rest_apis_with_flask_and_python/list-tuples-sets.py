#like an array, keep the order, you can manipulate it, you can append
list = ["Bob", "Rolf", "Anne"]
#tuple is like a constant
tuple = ("Element", "Of", "Tuple")
#like an abject, can't add duplicates, they don't have order, is not always guaranted, useful in few escenarios, you can add but with add, not append
set = {"Bob", "Rolf", "Anne"}

print(list)
#to access to lists and tuples you use suscript notation
print(list[0])
print(list[1])
print(list[2])
print(tuple[0])
print(tuple[1])
print(tuple[2])
#trying this gets an error 
# print(set[0])
# print(set[1])
# print(set[2])

#list always keeps the order
#for i in range(0,10):
    #print(list)

#set not always keeps the order, event doing this doesn't work, it seems happens in few cases
#for i in range(0, 10000):
#xa     print(set)

#assigning to list
list[0] = "Vince"
list[2] = 'Lombardi'
print(list)

#appending to list
list.append("Smith")
print(list)

#you can't append to list because is like a constant
#tuple.append("not appendable")
print(tuple)

#removing to list
list.remove("Vince")
print(list)

#adding to set, adding not ensures the order, append yes
set.add("Peter")
print(set)