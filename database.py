import pymysql
import sys

db = pymysql.connect("localhost", "root", "****", "Practice")
c = db.cursor()

while 1:
    id = int(input("Enter ID number: "))
    name = str(input("Enter name: "))
    score = int(input("Enter Score: "))
    query=f"insert into test_results values({id},'{name}',{score})"
    c.execute(query)
    db.commit()
    print("")
    repeat_entry = str(input("Would you like to enter another score? (Y/N): "))
    if repeat_entry == "Y" or repeat_entry == "y":
        1
    elif repeat_entry == "N" or repeat_entry == "n":
        sys.exit()
    else:
        print("")
        print("You didn't enter 'Y' or 'N'!")
    print("")