import random
'''
1 for rok
-1 for paper
0 for scissors

'''

computer = random.choice([-1, 1, 0])
youchoice = input("Enter your choice :")
gamedic = {"r": 1, "p": -1, "s": 0}
computerdic = {-1: "Paper", 1: "Rok", 0: "Scissors"}
you = gamedic[youchoice]

print(
    f"you choice {computerdic[you]} \n computer choice {computerdic[computer]}")

if (computer == you):
    print("March draw!")
else:
    if (computer == 1 and you == -1):
        print("You win! ")
    elif (computer == 1 and you == 0):
        print("You lose! ")
    elif (computer == -1 and you == 1):
        print("You lose! ")
    elif (computer == -1 and you == 0):
        print("You win! ")
    elif (computer == 0 and you == 1):
        print("You win! ")
    elif (computer == 0 and you == -1):
        print("You lose! ")
    else:
        print("kuch gadbad he")
