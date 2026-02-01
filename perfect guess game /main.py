import random

b=random.randint(1,100)
guess=0
while b>0:
    guess=guess+1
    a=int(input("Enter your guess between 1 to 100: "))
    if a<b:
        print("Your guess is too low")
    elif a>b:
        print("Your guess is too high")
    else:
        print(f"Congratulations! You guessed the number {b} in {guess} attempts.")    

