from random import randrange

def display_board(board):
    """Display the Tic-Tac-Toe board"""
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def enter_move(board):
    """Get the user's move and update the board"""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue
            
            # Convert number to row and column indices
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if board[row][col] in ['X', 'O']:
                print("This square is already occupied! Choose another one.")
                continue
            
            board[row][col] = 'O'
            break
        except ValueError:
            print("Please enter a valid number!")

def make_list_of_free_fields(board):
    """Return a list of free squares"""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    """Check if the specified player has won"""
    # Check rows
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True
    
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    return False

def draw_move(board):
    """Make computer's move"""
    free_fields = make_list_of_free_fields(board)
    
    if free_fields:
        # Choose a random free field
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    """Main game function"""
    # Initialize the board with numbers 1-9
    board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]
    
    # Computer makes first move in the center
    board[1][1] = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', computer is 'X'")
    print("Computer goes first in the center.")
    
    # Main game loop
    while True:
        display_board(board)
        
        # Check if computer won
        if victory_for(board, 'X'):
            print("Computer wins!")
            break
        
        # Check if it's a tie
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            display_board(board)
            print("It's a tie!")
            break
        
        # User's move
        enter_move(board)
        display_board(board)
        
        # Check if user won
        if victory_for(board, 'O'):
            print("You win! Congratulations!")
            break
        
        # Check if it's a tie after user's move
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            display_board(board)
            print("It's a tie!")
            break
        
        # Computer's move
        print("Computer's turn...")
        draw_move(board)

if __name__ == "__main__":
    main()