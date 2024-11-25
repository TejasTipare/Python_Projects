import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
a=random.choice(game)
b=input("0 for stone, 1 for paper , 2 for scissors\n")
if b=='0':
    print(rock)
    if a=='rock':
        print(f"Computer chose: \n{rock} \n play again ")
    elif a=='paper':
        print(f"Computer chose: \n{paper}\n you lose")
    else:
        print(f"Computer chose: \n{scissors}\n you win")
if b=='1':
    print(paper)
    if a=='rock':
        print(f"Computer chose: \n{rock}\n you win ")
    elif a=='paper':
        print(f"Computer chose: \n{paper}\n play again ")
    else:
        print(f"Computer chose: \n{scissors}\n you lose ")
if b=='2':
    print(scissors)
    if a=='rock':
        print(f"Computer chose: \n{rock}\nyou lose ")
    elif a=='paper':
        print(f"Computer chose: \n{paper}\nyou win ")
    else:
        print(f"Computer chose: \n{scissors}\nplay again ")
elif b >= '3' or b < '0':
    print("You typed an invalid number. You lose!")


#Another logic
'''game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")'''