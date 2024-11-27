import numpy as np
from math import floor

display = np.array([" " for x in range(9)]).reshape(3,3) #store the 'TicTacToe' diagram.
input_display = np.array([str(x) for x in range(9)]).reshape(3,3) #store the 'Input' diagram.

seen = [] #list, to checks if the 'user' is a duplicate or not.
turnVal = 0 #value that allows alternating between 'x' or 'o' turn.
win = False #if win remains False after the while-loop, it must be a draw.
while turnVal < 9:
    #display 'TicTacToe' and 'Input' diagrams.
    print('~~~~~ TicTacToe ~~~~~')
    print(display)
    print("")
    print(input_display)

    #to alternate between 'x' or 'o' turn, using odd or even function. (first turn is 'x')
    turn = 'x' if turnVal % 2 == 0 else 'o'

    #input index given by the player
    user = int(input('Choose an index: '))
    row = floor(user / 3) #example: 2/3 = 0.66 --> floor(0.66) = 0
    column = user % 3 #example: 4%3 = 1 and 0%3 = 0

    if user not in seen and 0 <= user <= 8:  #if the 'user' isn't a duplicate and it's value is within range.
        seen.append(user)
        display[row][column] = turn #to change the selected index to 'x' or 'o' depending on which player 'turn'.
        turnVal += 1
    elif user <= 8: #display an error if the 'user' is a duplicate.
        print(f'Index {user} have been taken.')
        print('')
        continue
    else: #display an error if the 'user' isn't within range.
        print(f'Index {user} is none existence.')
        print('')
        continue

    print('')

    if [display[0][0], display[1][1], display[2][2]].count(turn) == 3: #if the TicTacToe diagram does '3 in-a-row' diagonally.
        win = True
        break
    elif [display[0][2], display[1][1], display[2][0]].count(turn) == 3: #if the TicTacToe diagram does '3 in-a-row' diagonally. (The other diagonal)
        win = True
        break

    for i in range(3):
        if list(display[i]).count(turn) == 3: break #if the TicTacToe diagram does '3 in-a-row' horizontally.
        elif [display[0][i], display[1][i], display[2][i]].count(turn) == 3: break #if the TicTacToe diagram does '3 in-a-row' vertically.
    else: continue
    win = True
    break

print(display)
if win: print(f'{turn.upper()} is the WINNER!') #if there was a winner.
else: print('It is a DRAW!') #if the wasn't a winner, then it's a draw.
