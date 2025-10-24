import random , time
print("===== Quiz Game =====",end="\n\n")
print("Quiz Starts...!!", end="\n\n")
ls = ["+","-","x","/","<",">"]
player_num = i = que = 1
time1 = time2 = res = 0

def cal(opr,op1,op2):
    global res
    if opr == "+":
        res = op1 + op2
    elif opr == "-":
        res = op1 - op2
    elif opr == "x":
        res = op1 * op2
    elif opr == "/":
        res = op1 / op2
    elif opr == "<":
        res = int(op1 < op2)
    elif opr == ">":
        res = int(op1 > op2)
    return res
begin = time.perf_counter()
while player_num<=2:
    while que <= 5:
        print("\nPlayer", player_num, " ")
        op1 = random.randint(0, 9)
        op2 = random.randint(0, 9)
        opr = random.choice(ls)
        print(que, "Question := ", op1, opr, op2)
        res = cal(opr, op1, op2)
        print("Answer = ", end=" ")
        ans = int(input())
        if ans == res:
            print("Correct Answer..!")
            que += 1
        else:
            print("Wrong Answer...!")
        end = time.perf_counter()
        if player_num == 1:
            time1 = end - begin
        elif player_num == 2 :
            time2 = end - begin
    player_num += 1
    que = 1
    print()

print("\n\nHere's the result.......")
print("\n===================================")
time.sleep(3)
#print("/n/nPlayer 1: ", time1, end= " ")
#print("Player 2: ", time2)
if time1 > time2:
    print("\nPlayer 1 Wins...!")
elif time2 > time1:
    print("\nPlayer 2 Wins...!")
print("\n===================================")