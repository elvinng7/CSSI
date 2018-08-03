def get_player_word():
    return raw_input("What word would you like to use: ")


word = get_player_word()

blankSpots = "_" * len(word)

# for letter in word :
#     blankSpots += "_"

word 

print(blankSpots)

def get_player_guess():
    return raw_input("What letter would you like to guess: ")

playerguess = get_player_guess()




correctguesses = 0
guess = ""

# while correctguesses < 5 :
guess = get_player_guess()
for i in range(len(word)) :
    if word[i] == guess:
        print(word)

    # correctguesses += 1
