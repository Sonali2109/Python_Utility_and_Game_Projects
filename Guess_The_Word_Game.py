import random
print("====== Guess The Word ======")
ls = ["planet","sun","oyster","pearl","queen","temperature","rise","elephant"]
que = 1
j = i = flag = flag1 = won = 0
word = random.choice(ls)
l = len(word)
set_alpha = list(word)
dash = []
while que<=10:
    print("Chance - ",que)
    while i<l:
        dash.append(" _ ")
        i+=1
    print("".join(dash))
    print()
    print("\nGuess the Word or type '*' if u get the word ==>")
    guess = input()
    if guess == "*":
        print("Enter Word = ")
        g_word = input()
        if g_word == word:
            print("You Won")
            won = 1
            break
        else:
            print("OOPS..! Wrong Guess....")
            que += 2
            j = flag = 0
            continue
    else:
        while j < l:
            if set_alpha[j] == guess:
                dash[j] = guess
                flag = 1
            j += 1
    if flag == 1:
        print("".join(dash))
    else :
        print("Incorrect...")
        j = flag = 0
        que += 1
        continue
    que += 1
    flag = j = 0
    for d in dash:
        if d != " _ ":
            flag1 = 1
        else:
            flag1 = 0
    if flag1 == 1:
        print("You WON.....!")
        break
    if won == 1:
        break
    print()
