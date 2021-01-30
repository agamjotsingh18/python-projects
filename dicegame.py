import random
print("WELCOME")
print("ROLL THE DICE GAME")
print("rolling the dice 1st time")
number=random.randrange(1,6)
print("Your number is ",number)
rolled=1
again=input("Do you want to roll dice again ")

while again=='yes':
    number=random.randrange(1,6)
    print("Your number is ",number)
    rolled+=1
    again=input("Do you want to roll dice again ")

print("Thanks for rolling. You rolled ",rolled, " times")
