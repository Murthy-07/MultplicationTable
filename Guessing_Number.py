import random

number =random.randint(1,100)
guess=0

while guess!=number:
    guess=int(input("Enter a number: "))
    
    if guess<number:
        print("Too Low")
    elif guess>number:
        print("Too High")
    else:
        print("Congratulations Guessed Well Buddy!!!!")