import random
print("===== Simple 1 Card Game =====",end="\n\n")
#no_pl = int(input("How many Players do you want ?"))
print("Let's Play...!!", end="\n\n")
num = 1
prev_score = player_score1 = player_score2 = 0

def cal_result(curr_score,num):
    #This function is used to calculate score and result of each round of each player, respectively...
    global prev_score, player_score1, player_score2
    if curr_score == prev_score + 1:
        print("\nPlayer", num , "Wins..!!!")
        if num == 1:
            #This- function is used to calculate score of each player at each round
            player_score1 += num
            print("Player", num, "Score : ", player_score1)
        elif num == 2:
            player_score2 += num
            print("Player", num, "Score : ", player_score2)
    else:
        prev_score = curr_score

def take_input():
    # This function is used to take input from user...
    global num , player_score1 , player_score2, prev_score
    i=1
    while True:
        print("Round-", i ," :== ",end="\n\n",sep="")
        while num<=2:
            input("Press 'ENTER' to generate alphabet :  ")
            curr_score = random.randint(65, 90)
            print("Player", num, ":", chr(curr_score))
            cal_result(curr_score,num)
            if player_score1 or player_score2 == 4:
                break
            num += 1
        if player_score1 or player_score2 == 100:
            break
        num = 1
        i += 1
        print()
take_input()