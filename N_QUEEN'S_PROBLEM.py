#N QUEEN'S PROBLEM
q = 4 
i = 3 

def is_safe(board, row, col):
    
    for r in range(row):
        if board[r][col] == 'Q':
            return False

    # for x in zip(range(q-1,-1,-1),range(i-1,-1,-1)):
        # print(x)
    # for x in zip(range(q-1,-1,-1),range(0,i+1,1)):
    #     print(x)
    
  
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[r][c] == 'Q':
            return False
    

    for r, c in zip(range(row-1, -1, -1), range(col+1, q)):
        if board[r][c] == 'Q':
            return False
    
    return True


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)] 
    def backtrack(row):
        if row == n:
            
            print_board(board)
            return True
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'  
                if backtrack(row + 1):
                    return True
                board[row][col] = 0  
                
        return False
    
    def print_board(board):
        for row in board:
            print(row)
        print()
    
    backtrack(0)


solve_n_queens(q)