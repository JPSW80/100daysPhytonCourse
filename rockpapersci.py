import  random

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
game_images = [rock, paper, scissors]

user_selection = int(input("Welcome player! Are you ready to loose??Let's go. Type: 0  for Rock, 1 for Paper and  2 for Scissors: " ))
print(game_images[user_selection])


# if user_selection==0:
#   print (game_images[0])
# elif user_selection==1:
#   print(game_images[1])
# else:
#   print(game_images[2])
  
pc_selection=random.randint(0,2)
print(f"My choise is: {game_images[pc_selection]}")

if user_selection>=3 or user_selection<0:
  print("You lose! You MUST choose a valid number.")
elif user_selection==pc_selection:
  print("It's a draw. Let's play again, I MUST win the game!!!!")
elif user_selection==0 and pc_selection==2:
  print('Dam! You win!')
elif user_selection==1 and pc_selection==0:
  print('Dam! You win!')
elif user_selection==2 and pc_selection==1:
  print('Dam! You win!')
else:
  print("Sucker! I knew I would beat you! I am the king of the world!!")