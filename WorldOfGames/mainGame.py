from Live import load_game, welcome
from GuessGame import play as playGuess
from memoGame import play as playMemoGame
from CurrencyRouletteGame import play as playCurrency
from Score import add_score






print(welcome("Guy"))
startgame = load_game()
level_select = startgame[1]
playgame = startgame[0]

if playgame == 1:
    game = playMemoGame(level_select)
elif playgame == 2:
    game = playGuess(level_select)
elif playgame == 3:
    game = playCurrency(level_select)
if game == True:
    print("you win!")
    nickname = input("pls enter your nickname for ranking list   ")
    add_score(level_select, nickname)

else:
    print("oh you lose maybe next time!")





