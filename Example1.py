from random import randint
import os

os.system("clear")

dice1 = randint(1,6)
dice2 = randint(1,6)

print(f"dice 1: {dice1}")
print(f"dice 2: {dice2}")

if (dice1 == dice2):
    print(f"you win")
else:
    print(f"you lose")

os.system("pause")