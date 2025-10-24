import random
print("===== Dice Game =====",end="\n\n")
no_pl = int(input("How many Players do you want ?"))
print("Let's Play...!!", end="\n\n")
j = num = win = 1
def repeat(player):
    # This function gives another chance to roll dice and check whether that player wins or not...
    global dice, win
    print("\n*********************","Again Chance to roll...!", sep="\n")
    input("Press 'ENTER' to roll the dice :  ")
    dice = random.randint(1, 6)
    print("Player", player , ":", dice)
    print("*********************",end="\n\n")
    if dice == 6:
        print("Player",player,"Wins...!!!")
        win += 1
def take_input():
    # This function is used to take input from user...
    global num
    i=1
    while True:
        print("Round-", i ," :== ",end="\n\n",sep="")
        while num<=no_pl:
            input("Press 'ENTER' to roll the dice :  ")
            user = random.randint(1, 6)
            print("Player", num, ":", user)
            if user == 6:
                repeat(num)
                if win == 2:
                    break
            num += 1
        if win == 2:
            break
        num = 1
        i += 1
        print()
take_input()