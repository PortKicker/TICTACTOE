
print('\n'*100)

print('Let\'s play Tic Tac Toe!' + '\n'*3) 

def player_input():

    marker = '' 

    while marker != 'X' and marker != 'O':
     
          marker = input('Player one, would you like to be X\'s or O\'s: ').upper()
     
          if marker == 'X':
             return ('X', 'O')
          else:
             return ('O','X') 

player_one , player_two = player_input() 



print('\n'*100)

def display_board(board):
    
    print('\n'*10) 

    print('Here is the board map.')

    print('1'+'|'+'2'+'|'+'3')
    print('-----')
    print('4'+'|'+'5'+'|'+'6')
    print('-----')
    print('7'+'|'+'8'+'|'+'9')

    print('\n'*2)


    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])


 

def win_check(board, mark):
         

        return((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark))



def space_check(board, position):
    
    return board[position] == ' '


def player_choice(board):

    position = 0  

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position): 
        position = int(input('Choose your next position: (1-9) : ')) 
    
    
    
    return position

def replay():

    return input('Do you want to play again? Yes or No : ').lower() == 'y'
    
    
game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

test_board = ['#','X','O','X','O','X','O','X','O','X']

while True:

    display_board(game_board)    
    
    # Player One 
    print(f'Player 1, it is your turn ( {player_one}\'s )')
    choose = player_choice(game_board)
    if space_check(game_board, choose) == True:
         game_board[choose] = player_one
         display_board(game_board)    
    
    if win_check(game_board, player_one) == True:
        print('Player 1 is the winner!!!\n')
        
        if replay() == True:
            game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
            continue
        else:
            break
    
    if ' ' not in game_board:
        print('Both Players have come to a tie!!!\n')
        if replay() == True:
            game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        else:
            break



    # Player Two
    print(f'Player 2, it is your turn ( {player_two}\'s )')
    choose = player_choice(game_board)
    
    if space_check(game_board, choose) == True:
         game_board[choose] = player_two
         display_board(game_board)
    
    if win_check(game_board, player_two) == True:
        print('Player 2 is the winner!!!\n')
        
        if replay() == True:
            game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        else:
            break
      
    if ' ' not in game_board:
        print('Both Players have come to a tie!!!\n')
        if replay() == True:
            game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            continue
        else:
            break



    continue


     
