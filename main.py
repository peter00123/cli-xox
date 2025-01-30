

from game import start
withs = ["1","2"]

while (exit != True):
    for i in range(3):
        print(" ")
    print("         welcome")
    print(" ")
    print("         enter ")
    print("         1.play with pc ")
    print("         2.play with friend ")
    pwith = str(input("          "))
    
    if pwith in withs:
        exit = True

    if(pwith == "e"):
        print("         you have exited the game")
        for i in range(3):
            print(" ")
        exit()
    else:
        print("          enter e to exit the game")

    
exit = False
while (exit != True):
    sizes = ["5","7"]
    for i in range(3):
        print(" ")
    print("         welcome")
    size = str(input("         choose the number of box (3,5) "))
    
    if size in sizes:
        exit = True

    if(size == "e"):
        print("         you have exited the game")
        for i in range(3):
            print(" ")
        exit()
    else:
        print("          enter e to exit the game")
        
size = int(size)
#print(size)


print(f"            playing with {pwith} in {size} table")

start(size,pwith)
