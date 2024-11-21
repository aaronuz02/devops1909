
def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def load_game():
    print("\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
    game_name = int(input("Please choose a game to play:"))
    while game_name < 1 or game_name > 3:
        print("the input suppose to be a number between 1 to 3")
        game_name = int(input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
    game_difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
    while game_difficulty < 1 or game_difficulty > 5:
        print("the input suppose to be a number between 1 to 5")
        game_difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
    return game_name, game_difficulty

