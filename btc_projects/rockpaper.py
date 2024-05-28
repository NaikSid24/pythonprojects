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

#Write your code below this line 👇
import random
selection_list = [rock,paper,scissors]
user_selec = 0
user_selec= int(input("What do you Chose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_selec == 0:
    print(selection_list[0])
elif user_selec == 1:
    print(selection_list[1])
elif user_selec == 2:
    print(selection_list[2])

random_number = random.randint(0,len(selection_list)-1)
print("Computer chose:")
print(selection_list[random_number])
#user selects rock
if user_selec == 0:
    if user_selec == 0 and random_number == 1:
        print("You lose")
    elif user_selec == 0 and random_number == 2:
        print("You won")
    else:
        print("Its a tie")
if user_selec == 1:
    if user_selec == 1 and random_number == 0:
        print("You won")
    elif user_selec == 1 and random_number == 2:
        print("You lose")
    else:
        print("Its a tie")
#user selects scissors
if user_selec ==2:
    if user_selec == 2 and random_number == 0:
        print("You lose")
    elif user_selec == 2 and random_number == 1:
        print("You won")
    else:
        print("Its a tie")
