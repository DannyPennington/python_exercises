def add (x,y):
    return(x + y)

def subtract (x,y):
    return(x - y)

def multiply (x,y):
    return( x * y)

def divide (x,y):
    return(x / y)

loop = 1
while 1:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    op = input("enter operator (+, -, *, /): ")

    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(subtract(num1, num2))
    elif op == "*":
        print(multiply(num1, num2))
    elif op == "/":
        if num2!=0:
            print(divide(num1, num2))
        else:
            print("can't divide by 0!")
            continue
    else:
        print("Enter valid Operator! (+, -, *, /)")
        continue
 
    while loop == 1:
        retry = input("Do you want to do another calculation (y/n)? ")
        retry.lower()
        if retry == "y":
            break
        elif retry == "n":
            exit("Thanks for using the calculator")
        else:
            print("Enter y or n! ")
