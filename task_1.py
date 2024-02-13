def add(num1,num2):             #function to perform addition
    return num1+num2
def sub(num1,num2):             #function to perform substraction
    return num1-num2
def mul(num1,num2):             #function to perform multiplication
    return num1*num2
def div(num1,num2):             #function to perform division
    return num1/num2
print("Select the operation")   #Display the operations
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice=input("Enter your choice (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        try:
            number1=float(input("Enter the first number: "))     #to take input from user
            number2=float(input("Enter the second number: "))   #to take input from user
        except ValueError:
            print("Invalid input. Enter a number")
            continue
        #To enter the choices
        if choice=='1':
            print("Addition result")
            print(number1,"+",number2,"=",add(number1,number2))
        elif choice=='2':
            print("Substraction result")
            print(number1,"-",number2,"=",sub(number1,number2))
        elif choice=='3':
            print("Multiplication result")
            print(number1,"*",number2,"=",mul(number1,number2))
        elif choice=='4':
            print("Division result")
            print(number1,"/",number2,"=",div(number1,number2))
        next_calculation=input("Are you want to do next calculation? (yes/no)")
        if next_calculation=="no":
            break
    else:
        print("Invalid input")
