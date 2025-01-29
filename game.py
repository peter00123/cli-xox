def check_diagonals(matrix):
    # Check rows
    for row in matrix:
        if len(set(row)) == 1 and row[0] != " ":
            return f"Winner: {row[0]} in row"
    
    # Check columns
    for col in range(3):
        column = [matrix[row][col] for row in range(3)]
        if len(set(column)) == 1 and column[0] != " ":
            print(f"Winner: {column[0]} in column")
    
    # Check main diagonal
    main_diag = [matrix[i][i] for i in range(3)]
    if len(set(main_diag)) == 1 and main_diag[0] != " ":
        print(f"Winner: {main_diag[0]} in main diagonal")
    
    # Check anti diagonal
    anti_diag = [matrix[i][2-i] for i in range(3)]
    if len(set(anti_diag)) == 1 and anti_diag[0] != " ":
        print(f"Winner: {anti_diag[0]} in anti diagonal")
    
    return "No winner"

def start(difficualti):
    print("you are X ")
    print("computer is O")
    print("enter the number, where u want to place the X")
    print(" ")
    print(" ")

    #matrix = [[(i+1)*10 + (j+1) for j in range(3)] for i in range(3)]

    # Print the matrix
    #for row in matrix:
    #    print(row)

    matrix = [
        [11,12,13],
        [11,22,23],
        [11,32,33]
    ]
    
    check_diagonals(matrix)
    


