'''
0=snake
1=water
2=gun
'''

import random

a=['snake', 'water', 'gun']
com=random.choice(a)
user=input("Enter your choice (snake, water, gun): ").lower()
print(f"Computer selected: {com}")
print(f"You selected: {user}")
if user==com:
    print(f"Both selected {user}. It's a tie!")

else:
   if com=="snake" and user=="water":
        print("you lose! Snake drinks water.")

   elif  com=="snake" and user=="gun":
        print("You win! Gun kills snake.") 

   elif com=="water" and user=="snake":
        print("you win! Water damages gun.")   

   elif com=="water" and user=="gun":
        print("you lose! Gun kills snake.")   

   elif com=="gun" and user=="snake":
        print("you lose! Snake damages gun.")

   elif com=="gun" and user=="water":
        print("you win! Water damages gun.")

   else:
      print("Invalid input! Please choose snake, water, or gun.")                   


          