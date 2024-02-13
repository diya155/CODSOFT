import string
import random
lenght=int(input("Enter the password lenght: "))        #To take the password lenght
print("Choose the characters for the password")
print("1.Digits")
print("2.Letters")
print("3.Special Characters")
print("4.Exit")
character_list=""
while(True):
    choice=int(input("Enter a number: "))               #To enter choice
    if(choice==1):
        character_list+=string.ascii_letters
    elif(choice==2):
        character_list+=string.digits
    elif(choice==3):
        character_list+=string.punctuation
    elif(choice==4):
        break
    else:
        print("Enter a valid choice")
password=[]
for i in range(lenght):
    randomchar=random.choice(character_list)
    password.append(randomchar)
print("The random password is "+"".join(password))
