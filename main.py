

from game import start

while (exit != True):
    for i in range(3):
        print(" ")
    size = int(input("choose the number of box "))
    for i in range(3):
        print("  ")

    if(size == 0):
        print("enter _e_ for exiting")
        print("you have chosen the easy level")
        for i in range(3):
            print(" ")
        exit = True
    elif(size == 1):
        print("enter _e_ for exiting")
        print("you have chosen the medium level")
        for i in range(3):
            print(" ")
        exit = True
    elif(size == 2):
        print("enter _e_ for exiting")
        print("you have chosen the hard level")
        for i in range(3):
            print(" ")
        exit = True
    elif(size == 3):
        print("enter _e_ for exiting")
        print("you have chosen the hard level")
        for i in range(3):
            print(" ")
        exit = True
    elif(size == "e"):
        print("you have exited the game")
        for i in range(3):
            print(" ")
        exit = True
        exit()

print(size)



start(size)
