import pymysql
import sys

db = pymysql.connect("localhost", "root", "***", "Banking")
c = db.cursor()

while 1:
    CustomerName = str(input("Enter Customer Name: "))
    AccountType = str(input("Enter Account Type (C/S): "))
    Gender = str(input("Enter Customer Gender (M/F): "))
    CustomerAddress = str(input("Enter Customer Address (Postcode, City): "))
    query=f"insert into accounts values(NULL,'{CustomerName}','{AccountType}','{Gender}','{CustomerAddress}')"
    c.execute(query)
    db.commit()
    print("")
    repeat_entry = str(input("Would you like to enter another Record? (Y/N): "))
    if repeat_entry == "Y" or repeat_entry == "y":
        1
    elif repeat_entry == "N" or repeat_entry == "n":
        sys.exit()
    else:
        print("")
        print("You didn't enter 'Y' or 'N'!")
    print("")