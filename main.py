import random
user_choice=input("Choose your weapon[Rock,Paper,Scissor]:")
computer_choice= random.choice(['rock','paper','scissor'])

user_choice=user_choice.lower()

print("Computer Choice:",computer_choice)
print("User Choice:",user_choice)

if(user_choice=="rock" and computer_choice=="rock"):
  print("Draw")
elif(user_choice=="rock" and computer_choice=="paper"):
  print("Computer won")
elif(user_choice=="rock" and computer_choice=="scissor"):
  print("User Won")
elif(user_choice=="paper" and computer_choice=="rock"):
  print("User won")
elif(user_choice=="paper" and computer_choice=="Paper"):
  print("Draw")
elif(user_choice=="paper" and computer_choice=="scissor"):
  print("Computer won")
elif(user_choice=="scissor" and computer_choice=="rock"):
  print("Computer won")
elif(user_choice=="scissor" and computer_choice=="paper"):
  print("User won")
elif(user_choice=="scissor" and computer_choice=="scissor"):
  print("Draw")
else:
  print("Invalid input")