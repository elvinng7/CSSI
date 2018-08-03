class Car(object):
    def __init__ (self, name, color, weight, wheels):
        self.name = name
        self.color = color
        self.weight = weight
        self.wheels = wheels

    def color_car(self):
        print ("The color of this car is " + self.color)
    # def __init__ (self, wheels):
    #     self.wheels = wheels

my_car1 = Car("Honda", "green", "180", "4")

print(my_car1.name)

my_car1.color_car()

print(my_car1.color)
