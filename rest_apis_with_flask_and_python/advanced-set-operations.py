#difference
friends = {"Bob", "Anne", "Rolf"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

#union
two_fruits = {"Orange", "Tangerine"}
one_fruit = {"Apple"}
shake = two_fruits.union(one_fruit)
print(shake)

#intersection
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)