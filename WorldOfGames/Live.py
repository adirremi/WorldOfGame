def welcome(name):
    print('Hello ' + name + " and welcome to the World of Games(WoG).\n Here you can find many cool games to play.")
    return


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have toguess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_choose = input('pls choose number between 1-3   ')
    game_choose = int(game_choose)
    if game_choose > 3 and game_choose < 1:
        raise ValueError('No way, it just 1,2,3')

    print("Please choose game difficulty from 1 to 5:")
    level_select = input('pls choose number between 1-5   ')
    level_select = int(level_select)
    if level_select > 5 and level_select < 1:
        raise ValueError('No way, it just 1,2,3')
    return [game_choose, level_select]
