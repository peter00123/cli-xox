

def end(winr):
    print(f"winner is {winr}")
    exit()

def inserter(matrix,row,col,count,used,player,size):


    for row in matrix:
        print(row)
    if(count==1):
        exit()

    if(player=="x"):
        insert = str(input("enter where do u want to insert "+player+"    "))

    else:
        insert = str(input("enter where do u want to insert "+player+"    "))



    a = int(insert[0] )
    b = int(insert[1])
    val = matrix[a-1][b-1]
    if val in used:
        print("already used")
        inserter(matrix,row,col,count,used,player,size)
    else:

        used.append(val)
        matrix[a-1][b-1]=player


        count+1
        if(player=="x"):
            player = "o"
        else:
            player = "x"
    
        print(used)
        print(val)

        
        checker(matrix,row,col,count,used,player,size)



def checker(matrix,row,col,count,used,player,size):
    # Check rows
    for row in matrix:
        if len(set(row)) == 1 and row[0] != " ":
            return f"Winner: {row[0]} in row"
            winr = row[0]
            end(winr)
            
    
    # Check columns
    for col in range(size):
        column = [matrix[row][col] for row in range(size)]
        if len(set(column)) == 1 and column[0] != " ":
            print(f"Winner: {column[0]} in column")
            winr = column[0]
            end(winr)
            
    
    # Check main diagonal
    main_diag = [matrix[i][i] for i in range(size)]
    if len(set(main_diag)) == 1 and main_diag[0] != " ":
        print(f"Winner: {main_diag[0]} in main diagonal")
        winr = main_diag[0]
        end(winr)
            
    
    # Check anti diagonal
    anti_diag = [matrix[i][2-i] for i in range(size)]
    if len(set(anti_diag)) == 1 and anti_diag[0] != " ":
        print(f"Winner: {anti_diag[0]} in anti diagonal")
        winr = anti_diag[0]
        end(winr)


    
    inserter(matrix,row,col,count,used,player,size)

def start(size):
    size-1
    print("you are X ")
    print("computer is O")
    print("enter the number, where u want to place the X or O")
    
    print(size)


    matrix = []
    for i in range(size):  # Outer loop for rows
        row = []
        for j in range(size):  # Inner loop for columns
            row.append(str((i+1)*10 + (j+1)))  # Compute value
        matrix.append(row)  # Append row to matrix

    #print(matrix)

    """matrix = [[(i+1)*10 + (j+1) for j in range(3)] for i in range(3)]"""
    
    used = []

    """matrix = [
        [11,12,13],
        [11,22,23],
        [11,32,33]
    ]"""
    col = row
    count = 0
    player = "x"
    inserter(matrix,row,col,count,used,player,size)
    


