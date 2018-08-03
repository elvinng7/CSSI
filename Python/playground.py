#!/usr/bin/python

print("Hello, World")


#num = int(input("Enter a number: "))

#if num >= 0:
#    print("This is a nonnegative")
#elif num < 0:
#    print("This is a negative number")

#i = 0

 #while < 3:
    #num = int(input("Enter a number: "))
    #if num >= 0:
        #print("This is a nonnegative")
    #elif num < 0:
        #print("This is a negative number")

#to command all of them out you can do command 4 slash
#i = i + 1

#i += 1

#greeting = "Hello and welcome to my home!"
#for letter in greeting:
#    print(letter.lower())

#for i in range(5, 10, -1):
#my_name = "Rachel"
#friend1 = "Jess"
#friend2 = "Julia"
#friend3 = "Ciera"
#friend4 = "Matthew"

#print(
#"My name is " + my_name + " and my friends are " + friend1 + " and " + friend2 + " and " + friend3 + " and " + friend4
#)

#print(
#"My name is " + my_name + " and my friends are " + friend1 + " and " + friend2 + " and " + friend3 + " and " + friend4
#)



def greetSecretAgent(first_name, last_name):
    print("%s, %s, %s." % (last_name, first_name, last_name))

if greetSecretAgent("a", "b") is None and greetSecretAgent("c", "d" ) is not None:
    print("ahhhhhh what is going on")

greetSecretAgent("Rachael", "Mellon")
greetSecretAgent("James", "Bond")
greetSecretAgent("Just", "Q")

def greetSecretAgent(first_name, last_name):
    return "%s, %s, %s." % (last_name, first_name, last_name)

greeting = greetSecretAgent("julia", "cordero")
print(greeting)
