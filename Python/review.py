# help.("asasd" .split)
#
# #stringformating
#
# >>> first_name = "Logan"
# >>> last_name = "Chadderdon"
# >>> age = 26
#
# >>> greeting = first_name + "" + last_name + " is " + age + " years old "
#
# TypeError: cannot concatenate 'str' and 'int' objects
#
# >>> greeting = first_name + "" + last_name + " is " + str(age) + " years old "
#
#
#
# #percent s (%s) is a format place holder
#
# >>>greeting2 = "%s %s is %s years old" % ("val1", "val2", "val3")
# #output is val1 val2 is val3 years old
#
# >>> "%s %s is %s years old" % (first_name, last_name, age)
#




#classes
#allmethodsare functions attached to a class
#self is object at which passes through the method
#the init method is what inializes an object with properties. It puts properties onto an object.
class Player(object):           #we are creating the type of object
    def __init__(self, name):   #we are giving the object some properties #name is going to be object
        self.name = name
    def war_cry(self): #self is an object and it is a player. #self will be the object you call the method on. the player that is crying.
        print("%s says ahhhhh!" % (self.name))

class Game(object):   #game is a class #this is a blueprint
"""
Represents a game with players
"""
    def __init__ (self, players):
        self.players = players
"""
Initializes the new game with players
"""
    def __str__(self):   #stir stands for string. the purpose is to return a string representation of a class.
        num_players = len(self.players)
        return "There are %s s players" % (num_players)



    def add_player(self, players):
        self.players.append(player)

    def print_state(self):
        num_players = len(self.players) #what type is self.players? it is a list.
        print("There are %s players in this game" % (num_players))
my_player1 = Player("Mario")        #
my_player2 = Player("Kratos")        #instances of a class
my_player3 = Player("Link")          #instance of the blueprint

print(my_player1.name)
print(my_player2.name)
print(my_player3.name)


my_player1.war_cry()

print(self.players)




###functions

def is_multiple_of(number, divisor):
    if number % divisor == 0 :
        return True
    else:
        return False

result = is_multiple_of(25, 5)
