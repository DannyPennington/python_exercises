from random import randint
import sys

def dice():
    return randint(1,6)

dice_one = dice()

dice_throw = str(input("Throw the dice by pressing enter "))

if dice_throw == "":
    print (dice_one)
else:
    print ("You did not throw the dice")
    sys.exit()

print("")

dice_turn = str(input("Would you like to throw again? (Y/N): "))

while dice_turn == "Y" or dice_turn == "y":
    dice_two = dice()
    print (dice_two)
    print ("")
    dice_turn = str(input("Would you like to throw again? (Y/N): "))
    if dice_turn == "N" or dice_turn == "n":
        sys.exit()
else:
    print("")
    print("You didn't enter 'Y' or 'N'!")
    print("")
    dice_turn = str(input("Would you like to throw again? (Y/N): "))