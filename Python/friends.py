for x in range(1, 11):
    print(x)


def mystery2(b):
    return b * 2


#def mystery(word, number):
#    number = number * 2  #number is "hehe"
#    word = word.upper()  #word is 2
#    return word * numbermove # Error triend to multiply string from string

# print(mystery("2", "he"))





myName = "Ciera"
friend1 = "Jess"
friend2 = "Julia"
friend3 = "Ciera"
friend4 = "Matthew"
friend5 = "William"
friend6 = "Logan"
friend7 = "Katy"
friends =["Matthew", "Rachel", "Julia", "Jess", "William", "Logan", "Katy",]

friends.append("Areeta")
friends.insert(1, "brian")
friends.remove("Rachel")


print("My name is %s and I have %s friends"
    % (myName, len(friends)))

print("My friends are: ")

for friend in friends:
    print(friend)

for i in range(len(friends)):
    if i == 0:
        print(friends[0]),
    else:
        print("and" + friends{1})


#print("My name is %s" % myName)

#print(friends[0])
#print(friends[3])
#print
