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

#Write your code below this line 👇

game = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors!")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choose >= 3 or choose < 0:
  print("Invalid number!")
else:  
  print(game[choose])
  comp = random.randint(0,2)
  print(f"Computer choose: {comp}")
  print(game[comp])


  if choose == 0 and comp ==2:
    print("You Win!")
  elif comp == 0 and choose ==2:
    print("You Lose!")
  elif comp > choose:
    print("You Lose!")
  elif comp < choose:
    print("You Win!")
  elif comp == choose: 
    print("DRAW!")

  