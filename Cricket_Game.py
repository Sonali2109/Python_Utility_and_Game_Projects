import time, random

team1 = {1: {"score":[], "out_how":"NOT OUT"} ,2: {"score":[], "out_how":"NOT OUT"} ,3: {"score":[], "out_how":"NOT OUT"}}
team2 = {1: {"score":[], "out_how":"NOT OUT"} ,2: {"score":[], "out_how":"NOT OUT"} ,3: {"score":[], "out_how":"NOT OUT"}}
total_teams = 0
toss_pos = ["HEADS", "TAILS"]
toss_decision = ["BAT", "BOWL"]
pos = [0, 0, 1, 1, 1, 2, 2, 4, 4, 6, "WIDE", "NO BALL", "OUT"]
out_how = ["CATCH", "RUN OUT", "STUMPED", "BOLD", "LBW"]

print("Its toss time...")
time.sleep(3)
bat_bowl = random.choice(toss_decision)
batting_team = bowling_team = 0
if bat_bowl == "BAT":
    batting_team = 1
    print("TEAM1 decides to" , bat_bowl)
    bowling_team = 2
    print("TEAM2 have to BOWL")
elif bat_bowl == "BOWL" :
    batting_team = 2
    print("TEAM1 decides to", bat_bowl)
    bowling_team = 1
    print("TEAM2 have to BAT")

team1_score = 0
team1_extras = 0
team2_score = 0
team2_extras = 0
ball_no = 1
i = 1
print()
while total_teams < 2:
    if batting_team == 1:
        print("\nNOW, TEAM1 is Batting...!")
        print("TEAM2 is Balling...!")
    else:
        print("\nNOW, TEAM2 is Batting...!")
        print("TEAM1 is Balling...!")
    while i<=3:
        print("\nTEAM-",batting_team,"PLAYER NO.",i)
        while ball_no <= 5:
            if batting_team == 1:
                print()
                input("Press ENTER when BATSMAN is ready...")
                run = random.choice(pos)
                print("Ball : ", ball_no, "and Run is", run)
                if run == "OUT":
                    team1[i]["out_how"] = random.choice(out_how)
                    ball_no = ball_no + 1
                    break
                elif run == "WIDE" or run == "NO BALL":
                    team1_extras = team1_extras + 1
                    team1_score = team1_score + 1
                    continue
                else:
                    team1[i]["score"].append(run)
                    team1_score = team1_score + run
                    ball_no = ball_no + 1

            elif batting_team == 2:
                print()
                input("Press ENTER when BATSMAN is ready...")
                run = random.choice(pos)
                print("Ball : ", ball_no, "and Run is", run)
                if run == "OUT":
                    team2[i]["out_how"] = random.choice(out_how)
                    ball_no = ball_no + 1
                    break
                elif run == "WIDE" or run == "NO BALL":
                    team2_extras = team2_extras + 1
                    team2_score = team2_score + 1
                    continue
                else:
                    team2[i]["score"].append(run)
                    team2_score = team2_score + run
                    ball_no = ball_no + 1
        i = i + 1
        ball_no = 1
    if batting_team == 1:
        batting_team = 2
    elif batting_team == 2:
        batting_team = 1
    i = 1
    total_teams = total_teams + 1

print()
print("THE RESULT IS.....",end="\n\n")
time.sleep(5)
print("TEAM1 ======>" ,team1,sep="\n")
print("TEAM1 SCORE : ", team1_score)
print("TEAM1 EXTRAS : ", team1_extras)
print("TEAM2 ======>" ,team2,sep="\n")
print("TEAM2 SCORE : ", team2_score)
print("TEAM2 EXTRAS : ", team2_extras)