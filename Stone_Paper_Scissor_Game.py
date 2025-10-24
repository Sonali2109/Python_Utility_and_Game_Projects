import random
print("===== Stone-Paper-Scissor Game =====",end="\n\n")
print("Press 1 - Stone","Press 2 - Paper","Press 3 - Scissor", sep="\n")
print("Let's Play...!!", end="\n\n")
user = comp = u_sc = c_sc = d_sc = 0
i = 1
def take_input():
    # This function is used to take input from user...
    global user, comp
    while True:
        # This loop will execute if user given the invalid choice...
        print("Enter your choice:")
        user = int(input())
        if user>3 or user==0:
            print("Re-enter your Choice...")
            continue
        else:
            break
    comp = random.randint(1, 3)
    print("Computer choice:" , comp , sep="\n")
def result():
    # This function is used to declare recent winner...
    global u_sc, c_sc, d_sc
    if user == 1 and comp == 3 or user == 2 and comp == 1 or user == 3 and comp == 2:
        print("You Wins...!!")
        u_sc += 1
    elif user == 3 and comp == 1 or user == 1 and comp == 2 or user == 2 and comp == 3:
        print("Computer Wins...!!")
        c_sc += 1
    else:
        print("Match Draw...")
        d_sc += 1
    print()
def winner():
    # This function is used to declare ultimate winner...
    print("User-Score", "||" , "Comp-Score", "||", "Match Draw")
    print("======================================")
    print("   ", u_sc, "     ||\t ", c_sc, "     ||\t   ", d_sc, end="\n\n")
    if u_sc > c_sc :
        print("Ultimate Winner is YOU...!!")
    elif c_sc > u_sc :
        print("Ultimate Winner is COMPUTER..!!")
    else :
        print("Match Draws... Nobody is Winner...")
while i<=5:
    # This while-loop is to get 5 rounds of game...
    print("Round -", i)
    take_input()
    result()
    i += 1
winner()