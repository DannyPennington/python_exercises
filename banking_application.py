import pymysql
import sys

db = pymysql.connect("localhost", "root", "city2939", "Banking")
c = db.cursor()


def show_accounts(query):
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print (row[0],"-",row[1],"-",row[2],"-",row[3],"-",row[4])

def account_open():
    CustomerName = str(input("Enter your Name: "))
    AccountType = str(input("Enter the Account Type you wish to open (C/S): "))
    Gender = str(input("Enter your Gender (M/F): "))
    CustomerAddress = str(input("Enter your Address (Postcode, City): "))
    query = f"insert into accounts values(NULL,'{CustomerName}','{AccountType}','{Gender}','{CustomerAddress}')"
    c.execute(query)
    db.commit()
    print("")
    while 1:
        repeat_entry = str(input("Would you like to open another account? (Y/N): "))
        if repeat_entry == "Y" or repeat_entry == "y":
            CustomerName = str(input("Enter your Name: "))
            AccountType = str(input("Enter the Account Type you wish to open (C/S): "))
            Gender = str(input("Enter your Gender (M/F): "))
            CustomerAddress = str(input("Enter your Address (Postcode, City): "))
            query = f"insert into accounts values(NULL,'{CustomerName}','{AccountType}','{Gender}','{CustomerAddress}')"
            c.execute(query)
            db.commit()
            print("")
        elif repeat_entry == "N" or repeat_entry == "n":
            break
        else:
            print("")
            print("You didn't enter 'Y' or 'N'!")
            1
            print ("")


while 1:
    print("")
    print("1. Open a New Account \n2. Deposit \n3. Withdraw \n4. Reports \n5. Exit")
    print("")
    customer_choice = int(input("Enter Choice: "))

    if customer_choice == 1:
        print ("")
        account_open()

    if customer_choice == 2:
        print ("")
        deposit = float(input("How much money would you like to deposit?: "))

    if customer_choice == 3:
        print("")
        withdraw = float(input("How much money would you like to withdraw?: "))

    if customer_choice == 4:
        print("")
        print ("""1. Show all Accounts \n2. Show all Current Accounts \n3. Show all Saving Accounts \n4. Show all Male Accounts 
5. Show all Female Accounts \n6. Bank Statement for Specific Account \n7. Exit to Main Menu""")
        print ("")
        report = int(input("Which report would you like to see?: "))
        if report == 1:
            show_accounts("select * from accounts")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 2:
            show_accounts("select * from accounts where AccountType='C'")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 3:
            show_accounts("select * from accounts where AccountType='S'")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 4:
            show_accounts("select * from accounts where Gender='M'")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 5:
            show_accounts("select * from accounts where Gender='F'")
            print("")
            input("Press Enter to go back to the main menu")
        #if report == 6:

        if report == 7:
            1

    if customer_choice == 5:
        sys.exit()

