
difficualti = 0

def intro(difficualti):
    for i in range(3):
        print(" ")
    difficualti = input("choose the difficulti level from 0 to 3, and press enter  enter _e_ for exiting ")
    for i in range(3):
        print("  ")

    if(difficualti == 0):
        print("you have chosen the easy level")
        print("enter _e_ for exiting")
    elif(difficualti == 1):
        print("you have chosen the medium level")
        print("enter _e_ for exiting")
    elif(difficualti == 2):
        print("you have chosen the hard level")
        print("enter _e_ for exiting")
    elif(difficualti == 3):
        print("you have chosen the hard level")
        print("enter _e_ for exiting")
    elif(difficualti == "e"):
        print("you have exited the game")
        exit()
    else:
        intro(difficualti)
    return( difficualti)
    



intro(difficualti)
print(difficualti)
