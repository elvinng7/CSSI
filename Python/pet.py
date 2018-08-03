dog = {
    "name": "Doggy McDogface",
    "breed": "Terrier",
    "age" : 2,
    "hungry" : True,
    "sleepy" : False,
}

class Dog(object):
    def __init__(self, name, age, hungry, sleepy):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.needs_a_walk = True
        self.is_sleepy = True

    def feed(self):
        self.is_hungry = False
        print("nomnomnom")

    def walk(self):
        if self.needs_a_walk and not self.is_sleepy:
           self.needs_a_walk = True
           self.is_sleepy = False
           print("walkwlakwalk")
    def sleep(self):
        if self.is_sleepy == True :
           self.is_sleepy = False
           self.is_hungry = True
           print("zzzzzzzz")
    def __str__(self) :
        return ("%s who is %s" % (dog1.name, dog1.age))

    def play(self) :
        print("%s is playing with %s" % (self.name, other_dog.name)


dog1 = Dog("Doggy McDogface", 2)
dog2 = Dog("Buster", 1)



print(dog1)
# print('%s is %s years old' % (dog1.name, dog1.))


print(type(dog1))

print(dog1)
