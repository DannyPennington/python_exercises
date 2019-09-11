def add (x,y):
    print (x + y)

def subtract (x,y):
    print (x - y)

def multiply (x,y):
    print ( x * y)

def divide (x,y):
    print (x / y)

loop = 1
while 1:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    op = input("enter operator (+, -, *, /): ")

    if op == "+":
        add(num1, num2)
    elif op == "-":
        subtract(num1, num2)
    elif op == "*":
        multiply(num1, num2)
    elif op == "/":
        if num2!=0:
            divide(num1, num2)
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
