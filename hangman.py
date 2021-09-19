# Hangman

def hangman(word):
    # Establishes the basic layout of the game
    wrong = 0
    stages = ["",
              "___   ",
              "|  |  ",
              "|  0  ",
              "| /|\ ",
              "|  |  ",
              "| / \ ",
              "|     "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    e = wrong + 1
    print("Welcome to Hangman!")
    print("\n".join(stages[0: e]))
    print(" ".join(board))
    
    # Establishes how to keep the game going
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter: ")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        # WIN or LOSE Scenarios
        if "_" not in board:
            print("You WIN! Player ONE WINS!")
            print(" ".join(board))
            win = True
            break
        if wrong == len(stages) - 1:
            print("\n".join(stages[0:wrong]))
            print("You LOSE! Player TWO WINS! The word was {}.".format(word))
# End of Game Layout

# Introduction to Game
print("Welcome to Hangman!")
option = input("""Before we start the game, press "y" (without quotes) and
press ENTER if you would like to choose your own word for this game.
Other responses will result in this program randomly generating
a word for you from our database: 
""")
if option == "y":
    # Asks players on start of program to enter a word they will use in game
    intro = input("""To start HANGMAN, Player TWO must enter
a word Player ONE must guess for this game: """)
    # Start of Hangman!
    hangman(intro)
else:
    import random # Random generator is imported
    # Random list of words here
    random_words = ["dog", "peleton", "wild", "caboose", "pinch", "relative"]
    # From the list, a random word will be selected for this game
    hangman(random.choice(random_words))
