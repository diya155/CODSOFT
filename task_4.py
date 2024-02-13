import random
choices=["Rock", "Paper", "Scissors"]
def validate_input(choice):                 #for validation of user choice
    return choice.capitalize() in choices
while True:
    user_choice=input("Choose between Rock, Paper, or Scissors: ").capitalize()       #Taking user's choice
    if validate_input(user_choice):
        break
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
computer_choice=random.choice(choices)            #To generate computer's choice
print("You chose:", user_choice)                  #To display user's choice
print("Computer chose:", computer_choice)         #To display computer's choice
if user_choice==computer_choice:                  #Tie
    print("Tie")
elif (user_choice=="Rock" and computer_choice=="Scissors") or \
     (user_choice=="Paper" and computer_choice =="Rock") or \
     (user_choice=="Scissors" and computer_choice=="Paper"):        #Winning conditions
    print("You win")
else:
    print("Computer wins")
