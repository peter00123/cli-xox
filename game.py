def iteration(matrix,row,col,count):
    matrix[1][2]="x"
        

    if(count==1):
        exit()
    
    count+1
    check_diagonals(matrix,row,col,count)



def check_diagonals(matrix,row,col,count):
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

    for row in matrix:
        print(row)
    
    iteration(matrix,row,col,count)

def start(difficualti):
    print("you are X ")
    print("computer is O")
    print("enter the number, where u want to place the X")
    
    print(difficualti)


    matrix = []
    for i in range(difficualti):  # Outer loop for rows
        row = []
        for j in range(difficualti):  # Inner loop for columns
            row.append(str((i+1)*10 + (j+1)))  # Compute value
        matrix.append(row)  # Append row to matrix

    #print(matrix)

    """matrix = [[(i+1)*10 + (j+1) for j in range(3)] for i in range(3)]"""
    
    

    """matrix = [
        [11,12,13],
        [11,22,23],
        [11,32,33]
    ]"""
    col = row
    count = 0
    check_diagonals(matrix,row,col,count)
    


