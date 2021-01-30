import random
print("Guess the number game")
number =random.randrange(1,50)
attempts=1

guess=int(input("Enter the number mbetween 1 to 50 "))

while guess!=number:
    if guess<number:
        print("Your guess is LOW")
        guess=int(input("Enter the number mbetween 1 to 50 "))
        attempts+=1
    else:
        print("Your guess is HIGH")
        guess=int(input("Enter the number mbetween 1 to 50 "))
        attempts+=1

print()
print("CONGRAULATIONS you guessed right number in ",attempts," attempts")
print("THANKS FOR PLAYING")