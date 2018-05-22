import pymysql
import sys

db = pymysql.connect("localhost", "root", "city2939", "Banking")
c = db.cursor()

def show_accounts(query):
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print (row[0],"-",row[1],"-",row[2])

def account_open():
    CustomerName = str(input("Enter your Name: "))
    AccountType = str(input("Enter the Account Type you wish to open (C/S): "))
    Gender = str(input("Enter your Gender (M/F): "))
    CustomerAddress = str(input("Enter your Address (Postcode, City): "))
    query = f"select concat('{AccountType}','{Gender}',lpad(COALESCE(max(substr(AccountNumber,3,3))+1,'001'),3,'0')) as new from accounts where AccountNumber like ('{AccountType}%')"
    c.execute(query)
    account_number = c.fetchone()
    query_one = f"insert into accounts values('{account_number[0]}','{CustomerName}','{CustomerAddress}')"
    c.execute(query_one)
    db.commit()
    print("")
    print("Your Account Number is",account_number[0],"- Please keep this safe!")
    print("")
    while 1:
        repeat_entry = str(input("Would you like to open another account? (Y/N): "))
        print("")
        if repeat_entry == "Y" or repeat_entry == "y":
            CustomerName = str(input("Enter your Name: "))
            AccountType = str(input("Enter the Account Type you wish to open (C/S): "))
            Gender = str(input("Enter your Gender (M/F): "))
            CustomerAddress = str(input("Enter your Address (Postcode, City): "))
            query = f"select concat('{AccountType}','{Gender}',lpad(COALESCE(max(substr(AccountNumber,3,3))+1,'001'),3,'0')) as new from accounts where AccountNumber like ('{AccountType}%')"
            c.execute(query)
            account_number = c.fetchone()
            query_one = f"insert into accounts values('{account_number[0]}','{CustomerName}','{CustomerAddress}')"
            c.execute(query_one)
            db.commit()
            print("")
            print("Your Account Number is", account_number[0], "- Please keep this safe!")
            print("")
        elif repeat_entry == "N" or repeat_entry == "n":
            break
        else:
            print("")
            print("You didn't enter 'Y' or 'N'!")
            1
            print ("")

def balance(account_number):
    query1= f"select sum(amount) from deposits where accountnumber='{account_number}'"
    query2= f"select sum(amount) from withdrawals where accountnumber='{account_number}'"
    c.execute(query1)
    deposit = c.fetchone()
    c.execute(query2)
    withdrawal = c.fetchone()
    balance = deposit[0]-withdrawal[0]
    return balance

def balancecheck(account_number):
    query1 = f"select amount from deposits where accountnumber='{account_number}'"
    query2 = f"select amount from withdrawals where accountnumber='{account_number}'"
    ab = c.execute(query1)
    abc = c.execute(query2)
    if ab == 0 or abc == 0:
        return "Unknown"

def customername(account_number):
    query = f"select CustomerName from accounts where accountnumber='{account_number}'"
    abc = c.execute(query)
    row = c.fetchone()
    if abc == 0:
        return "Unknown"
    else:
        return row[0]

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
        account_number = str(input("Please enter your Account Number: "))
        print("")
        if customername(account_number)!="Unknown":
            print ("Welcome to the Bank of Jay,",customername(account_number))
            if balancecheck(account_number) == "Unknown":
                query = f"insert into deposits values('{account_number}','0','09-05-2018')"
                query1 = f"insert into withdrawals values('{account_number}','0','09-05-2018')"
                c.execute(query)
                c.execute(query1)
                db.commit()
            else:
                print("The current balance of your Account is:", balance(account_number))
                print("")
                deposit = int(input("How much money would you like to deposit?: "))
                query_two = f"insert into deposits values('{account_number}','{deposit}', '09-05-2018')"
                c.execute(query_two)
                db.commit()
                print ("The balance of your Account is now:",balance(account_number))
                print("")
                input("Press Enter to go back to the main menu")
        else:
            print("That Account Number doesn't exist. Please try again.")

    if customer_choice == 3:
        print("")
        account_number = str(input("Please enter your Account Number: "))
        print("")
        if customername(account_number) != "Unknown":
            print("Welcome to the Bank of Jay,", customername(account_number))
            if balancecheck(account_number) == "Unknown":
                query = f"insert into deposits values('{account_number}','0','09-05-2018')"
                query1 = f"insert into withdrawals values('{account_number}','0','09-05-2018')"
                c.execute(query)
                c.execute(query1)
                db.commit()
            else:
                print("The current balance of your Account is:", balance(account_number))
                print("")
                withdraw = int(input("How much money would you like to withdraw?: "))
                if balance(account_number)- withdraw <0:
                    print("")
                    print ("You do not have enough money in your Account to do this!")
                    continue
                query_three = f"insert into withdrawals values('{account_number}','{withdraw}', '09-05-2018')"
                c.execute(query_three)
                db.commit()
                print("The balance of your Account is now:", balance(account_number))
                print("")
                input("Press Enter to go back to the main menu")
        else:
            print("That Account Number doesn't exist. Please try again.")

    if customer_choice == 4:
        print("")
        print ("""1. Show all Accounts \n2. Show all Current Accounts \n3. Show all Saving Accounts \n4. Show all Male Accounts 
5. Show all Female Accounts \n6. Bank Statement for Specific Account \n7. Exit to Main Menu""")
        print ("")
        report = int(input("Which report would you like to see?: "))
        if report == 1:
            print("")
            show_accounts("select * from accounts")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 2:
            print("")
            show_accounts("select * from accounts where AccountNumber like ('C%')")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 3:
            print("")
            show_accounts("select * from accounts where AccountNumber like ('S%')")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 4:
            print("")
            show_accounts("select * from accounts where AccountNumber like ('_M%')")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 5:
            print("")
            show_accounts("select * from accounts where AccountNumber like ('_F%')")
            print("")
            input("Press Enter to go back to the main menu")
        if report == 6:
            print("")
            account_number = str(input("Please enter your Account Number: "))
            print("")
            if balancecheck(account_number) == "Unknown":
                query = f"insert into deposits values('{account_number}','0','22-05-2018')"
                query1 = f"insert into withdrawals values('{account_number}','0','22-05-2018')"
                c.execute(query)
                c.execute(query1)
                db.commit()
            if customername(account_number) != "Unknown":
                query1 = f"select * from deposits where accountnumber='{account_number}'"
                c.execute(query1)
                rows = c.fetchall()
                print("Deposits:")
                for row in rows:
                    print("Amount:",row[1],"Date:",row[2])
                print("")
                query2 = f"select * from withdrawals where accountnumber='{account_number}'"
                c.execute(query2)
                rows = c.fetchall()
                print("Withdrawals:")
                for row in rows:
                    print("Amount:",row[1],"Date:",row[2])
                print("")
                print("Closing Balance:", balance(account_number))
                print("")
                input("Press enter to go back to the main menu")
            else:
                print("That Account Number doesn't exist. Please try again.")

        if report == 7:
            1

    if customer_choice == 5:
        sys.exit()

