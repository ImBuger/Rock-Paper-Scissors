import random
import sys
import time

print("""
WELCOME TO ROCK-PAPER-SCİSSORS GAME

1-ROCK
2-PAPER
3-SCİSSORS
'Q'-QUİT
""")

gameList = ["rock", "paper", "scissors"]
GamerScore = 0
CPUscore = 0
end = True


while end == True:

    num = random.randint(0, 2)
    enemy = gameList[num]

    choose = input(">>>")

    if(choose == "1"): #rock
        print("-ROCK!")
        if(enemy == "rock"):
            print("\t\tROCK!-")
            print("You",GamerScore , "-","PC", CPUscore)
            print("bruh!")

        elif(enemy == "paper"):
            print("\t\tPAPER!-")
            CPUscore += 1
            print("You", GamerScore, "-", "PC", CPUscore)

        elif(enemy == "scissors"):
            print("\t\tSCİSSORS!-")
            GamerScore += 1
            print("You", GamerScore, "-", "PC", CPUscore)

    if(choose == "2"): #paper
        print("-PAPER!")
        if (enemy == "rock"):
            print("\t\tROCK!-")
            GamerScore += 1
            print("You", GamerScore, "-", "PC", CPUscore)
        elif (enemy == "paper"):
            print("\t\tPAPER!-")
            print("bruh")
            print("You", GamerScore, "-", "PC", CPUscore)

        elif (enemy == "scissors"):
            print("\t\tSCİSSORS!-")
            CPUscore += 1
            print("You", GamerScore, "-", "PC", CPUscore)

    if(choose == "3"): #scissors
        print("-SCİSSORS!")
        if (enemy == "rock"):
            print("\t\tROCK!-")
            CPUscore += 1
            print("You", GamerScore, "-", "PC", CPUscore)

        elif (enemy == "paper"):
            print("\t\tPAPER!-")
            GamerScore += 1
            print("You", GamerScore, "-", "PC", CPUscore)

        elif (enemy == "scissors"):
            print("\t\tSCİSSORS!-")
            print("bruh")
            print(print("You",GamerScore , "-","PC", CPUscore), "-", CPUscore)

    if (CPUscore == 3):
        print("Computer Won!")
        end = False
    if (GamerScore == 3):
        print("Congratulations! You Won!")
        end = False
    if (choose.isnumeric() == False):
        chs1 = choose.lower()
        if(chs1 == "q"):
            print("Good Game...")
            time.sleep(1)
            sys.exit()
