#Magic methods. Are magic because are called automatically but can be called manually as well. For example bob.__str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #when you want to turn your object into a string
    def __str__(self):
        return f"{self.name}, {self.age} years old."

    #print an unambiguos representation of an object so that you can recreate an object 
    def __repr__(self):
        return f"<'{self.name}', {self.age}>"

    #note: these methods are extra, you can 

bob = Person("Bob", 35)
print(bob)