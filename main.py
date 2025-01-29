

from game import start

while (exit != True):
    for i in range(3):
        print(" ")
    difficualti = input("choose the difficulti level from 0 to 3, and press enter  enter _e_ for exiting ")
    for i in range(3):
        print("  ")

    if(difficualti == "0"):
        print("enter _e_ for exiting")
        print("you have chosen the easy level")
        for i in range(3):
            print(" ")
        exit = True
    elif(difficualti == "1"):
        print("enter _e_ for exiting")
        print("you have chosen the medium level")
        for i in range(3):
            print(" ")
        exit = True
    elif(difficualti == "2"):
        print("enter _e_ for exiting")
        print("you have chosen the hard level")
        for i in range(3):
            print(" ")
        exit = True
    elif(difficualti == "3"):
        print("enter _e_ for exiting")
        print("you have chosen the hard level")
        for i in range(3):
            print(" ")
        exit = True
    elif(difficualti == "e"):
        print("you have exited the game")
        for i in range(3):
            print(" ")
        exit = True
        exit()

print(difficualti)



start(difficualti)
