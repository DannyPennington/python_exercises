import getpass

p1_name = input("Player 1, what's your name?: ")
p2_name = input("Player 2, what's your name?: ")

while 1:
	player1 = getpass.getpass((p1_name + " , do you want to play rock (r), paper (p) or scissors (s)?: "))
	player2 = getpass.getpass((p2_name + " , do you want to play rock (r), paper (p) or scissors (s)?: "))

	player1.lower()
	player2.lower()

	if player1 not in ["r","p","s"] or player2 not in ["r","p","s"]:
		print("Please enter a valid selection!")
		1
	else:
		break

if player1 != player2:
	if player1 == "r" and player2 == "s":
		print(p1_name + " wins!")
	elif player1 == "r" and player2 == "p":
		print(p2_name +  " wins!")
	elif player1 == "p" and player2 == "r":
		print(p1_name + " wins")
	elif player1 == "p" and player2 == "s":
		print(p2_name + " wins!")
	elif player1 == "s" and player2 == "r":
		print(p2_name + " wins!")
	elif player1 == "s" and player2 == "p":
		print(p1_name + " wins!")
else:
	print("It's a draw!")

print(p1_name +  " : " + player1)
print(p2_name + " : " + player2)
