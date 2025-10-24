import random , time
print("*******************  Typing Master  *******************\n")
print("GAME BEGINS...!!", end="\n\n")
time.sleep(5)
player_num = i = que = 1
time1 = time2 = res = 0
begin = time.perf_counter()
while player_num<=2:
    print("Player-", player_num, " Press 'ENTER' to Start...",sep="",end="  ")
    input()
    while que <= 3:
        print("\nPlayer", player_num, " ")
        num = random.randint(1111111111,999999999999)
        print(que, "Question := ", num)
        print("Answer = ", end=" ")
        ans = int(input())
        if ans == num:
            print("Correct Answer..!")
            que += 1
        else:
            print("Invalid Answer...","Try Again...!")
        end = time.perf_counter()
        if player_num == 1:
            time1 = end - begin
        elif player_num == 2 :
            time2 = end - begin
    player_num += 1
    que = 1
    if player_num == 2:
        print("\n\nNext Player Chance...")
    print()

print("==========================================\n")
print("RESULT IS...",end=" ")
time.sleep(3)
if int(time1) < int(time2):
    print("PLAYER-1 WINS...!")
elif int(time2) < int(time1):
    print("PLAYER-2 WINS...!")
print("\n==========================================")
print("\nPlayer 1 took : ", int(time1),"seconds to complete the task.")
print("Player 2 took : ", int(time2),"seconds to complete the task.")
print("\n==========================================")
print("\nTHANK YOU...!")