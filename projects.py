# #1 dice rolling
# import random
# while True:
#     choice=input("roll the dice? (y/n):").lower()
#     if choice=="y":
#         die1=random.randint(1,6)
#         die2=random.randint(1,6)
#         print(f'({die1},{die2})')
#     elif choice=="n":
#         print("thanks for playing!")
#         break
#     else:
#         print("invalid choice!")

#2 number guess
# import random
# num_to_guess=random.randint(1,100)
# while True:
#     try:
#         guess=int(input("enter a number between 1 to 100:"))
#         if guess>num_to_guess:
#                 print("low")
#         elif guess<num_to_guess:
#                 print("high")
#         else:
#                 print("congratulaions you find it!")
            
#     except ValueError:
#         print("invalid number!")
    
#3 rock paper scisser
import random
emojies={'r':'🪨','p':'📃','s':'✂️'}
choices=('r','p','s') 

while True:
    user_choice=input("rock,paper,scisser (r/p/s):").lower()
    if user_choice not in choices:
        print("invalid choice!")
        continue

    computer_choice=random.choice(choices)
    
    print(f"you chose {emojies[user_choice]}")
    print(f"computer chose {emojies[computer_choice]}")

    if (
        (user_choice=='r' and computer_choice=='s')or
        (user_choice=='p' and computer_choice=='r')or
        (user_choice=='s' and computer_choice=='p')):
        print('you win')
    elif user_choice==computer_choice:
        print("Tie!")
    else:
        print('you lose')

    asks_user=input("do you play again? (y/n):").lower()
    if asks_user=='n':
        break

        

