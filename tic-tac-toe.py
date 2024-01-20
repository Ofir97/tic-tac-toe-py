def display_board(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 1, you will be {player1}. Player 2, you will be {player2}.')
    return player1, player2


# return True if position is available, False if not.
def check_position(board, position):
    return board[position] == ' '


def place_mark(board, player_mark, is_player1):
    acceptable_choice = range(1, 10)
    position = 0
    is_position_available = False
    user_msg = (f"{'Player 1' + f' ({player_mark})' if is_player1 else 'Player 2' + f' ({player_mark})'},"
                f" please choose a position to place your mark on the board (1-9): ")
    while position not in acceptable_choice or not is_position_available:
        position = input(user_msg)
        if position.isdigit():
            position = int(position)
            is_position_available = check_position(board, position - 1)
    board[position - 1] = player_mark


def check_win(board, marker):
    return (board[0] == board[1] == board[2] == marker or
            board[3] == board[4] == board[5] == marker or
            board[6] == board[7] == board[8] == marker or
            board[0] == board[3] == board[6] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[0] == board[4] == board[8] == marker or
            board[2] == board[4] == board[6] == marker)


def check_tie(board):
    return ' ' not in board


# returns True if game is over, returns False if to continue.
def start_round(board, player_mark, is_player1):
    place_mark(board, player_mark, is_player1)
    display_board(board)
    if check_win(board, player_mark):
        if is_player1:
            print(f'Player 1 ({player_mark}) wins!')
        else:
            print(f'Player 2 ({player_mark}) wins!')
        return True
    elif check_tie(board):
        print("It's a tie.")
        return True
    return False


def display_greeting():
    print('Welcome to Tic Tac Toe!')
    print('-----------------------')


def replay_game():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input('Play again? Enter Y/N: ').upper()

    return choice == 'Y'


def end_game():
    print('Thank you for playing, see you next time.')


def start_game():
    board = [' '] * 9
    player1_mark, player2_mark = player_input()
    is_over = False
    while not is_over:
        is_over = start_round(board, player1_mark, True)
        if is_over:
            break
        is_over = start_round(board, player2_mark, False)


display_greeting()
start_game()
while replay_game():
    start_game()
end_game()
