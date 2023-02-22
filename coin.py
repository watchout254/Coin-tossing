import random

print("\t\t\tAwoooo, Welcome to Dice lucky\n"
      "\t\tPick heads or tails between yourselves.\n"
      "\t\t\t\tRun the program in turns\n")

kando =random.randint(0,1)
print(kando)

if kando == 1:
    print("HEADS you won!!")
else:
    print("TAILS you won!!")