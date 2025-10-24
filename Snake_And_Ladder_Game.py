import random

print("<====== Snake & Ladder ======>")
tot_players = int(input("Enter Numbers of Players : "))
player_c = tot_players
i = 0
ls = []
win_ls = []
print("Enter Names: ")
while i < tot_players :
    ls.append(input())
    i = i+1
curr_player = 0
scores = [0] * tot_players

def ladder_chance():
    global curr_player

    if scores[curr_player] == 1:
        print("Woooo.. You got Ladder at 1.. Move up at 38")
        scores[curr_player] = 38
    elif scores[curr_player] == 4:
        print("Woooo.. You got Ladder at 4.. Move up at 14")
        scores[curr_player] = 14
    elif scores[curr_player] == 8:
        print("Woooo.. You got Ladder at 8.. Move up at 30")
        scores[curr_player] = 30
    elif scores[curr_player] == 21:
        print("Woooo.. You got Ladder at 21.. Move up at 42")
        scores[curr_player] = 42
    elif scores[curr_player] == 28:
        print("Woooo.. You got Ladder at 28.. Move up at 76")
        scores[curr_player] = 76
    elif scores[curr_player] == 50:
        print("Woooo.. You got Ladder at 50.. Move up at 67")
        scores[curr_player] = 67
    elif scores[curr_player] == 71:
        print("Woooo.. You got Ladder at 71.. Move up at 92")
        scores[curr_player] = 92
    elif scores[curr_player] == 88:
        print("Woooo.. You got Ladder at 88.. Move up at 99")
        scores[curr_player] = 99

def snake_loss():
    global curr_player

    if scores[curr_player] == 32:
        print("Oops.. You are bitten by snake.. Fall down at 10")
        scores[curr_player] = 10
    elif scores[curr_player] == 34:
        print("Oops.. You are bitten by snake.. Fall down at 6")
        scores[curr_player] = 6
    elif scores[curr_player] == 48:
        print("Oops.. You are bitten by snake.. Fall down at 26")
        scores[curr_player] = 26
    elif scores[curr_player] == 62:
        print("Oops.. You are bitten by snake.. Fall down at 18")
        scores[curr_player] = 18
    elif scores[curr_player] == 88:
        print("Oops.. You are bitten by snake.. Fall down at 24")
        scores[curr_player] = 24
    elif scores[curr_player] == 95:
        print("Oops.. You are bitten by snake.. Fall down at 56")
        scores[curr_player] = 56
    elif scores[curr_player] == 97:
        print("Oops.. You are bitten by snake.. Fall down at 78")
        scores[curr_player] = 78

def score_board(win_pl):
    global win_ls
    win_ls.append(win_pl)

won = False
while True:
    print("\nPlayer", ls[curr_player], "Play Your Turn")
    input("Press ENTER to roll the dice")
    roll = random.randint(1, 6)
    print("You Rolled :", roll)
    scores[curr_player] = scores[curr_player] + roll

    ladder_chance()
    snake_loss()

    if scores[curr_player] > 100:
        scores[curr_player] = scores[curr_player] - roll
    elif scores[curr_player] == 100:
        print("\n\nPlayer", ls[curr_player], "is Winner....!")
        print(scores)
        score_board(ls[curr_player])
        won = True
        ls.pop(curr_player)
        scores.pop(curr_player)
        tot_players = tot_players - 1

    if roll == 6 and won == False:
        print("\nRepeat your turn")
        continue
    else:
        if won == True and tot_players == 1:
            score_board(ls[0])
            print("\nOOPS....All your Opponent Wins....")
            if curr_player >= tot_players:
                print("Player", ls[curr_player-1], "Lost...")
            else:
                print("Player", ls[curr_player], "is Losser....!")
            break
        if won == True:
            won = False
            if curr_player+1 == tot_players +1:
                curr_player = 0
            elif curr_player +1 != tot_players+1:
                curr_player = curr_player
            continue
        else:
            print(scores)
            curr_player = curr_player + 1
            if curr_player == tot_players:
                print("Round Complete\n\n")
                curr_player = 0
                won = False

print("\n\n<====== SCOREBOARD ======>")
i = 1
for j in win_ls:
    print(i , j, sep = " ==> ")
    i += 1