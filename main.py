import random
your_choice=input("Choose your weapon[Rock,Paper,Scissor]:")
computer_choice= random.choice(['rock','paper','scissor'])

your_choice=your_choice.lower()

print("Computer Choice is : ",computer_choice)
print("Your Choice is : ",your_choice)

if(your_choice=="rock" and computer_choice=="rock"):
  print("Draw")
elif(your_choice=="rock" and computer_choice=="paper"):
  print("Computer won")
elif(your_choice=="rock" and computer_choice=="scissor"):
  print("User Won")
elif(your_choice=="paper" and computer_choice=="rock"):
  print("User won")
elif(your_choice=="paper" and computer_choice=="Paper"):
  print("Draw")
elif(your_choice=="paper" and computer_choice=="scissor"):
  print("Computer won")
elif(your_choice=="scissor" and computer_choice=="rock"):
  print("Computer won")
elif(your_choice=="scissor" and computer_choice=="paper"):
  print("User won")
elif(your_choice=="scissor" and computer_choice=="scissor"):
  print("Draw")
else:
  print("Invalid input")
