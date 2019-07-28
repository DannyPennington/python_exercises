import random
import string
from random_word import RandomWords

r = RandomWords()
string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

while 1:
	print("")
	strength = input("Do you want your password Weak (w), Mid (m) or Strong (s)?: ")
	strength.lower()
	if strength not in ["w", "m", "s"]:
		print("Please enter valid selection")
		print(" ")
	else:
		break

if strength == "w":
	password = r.get_random_word(maxLength=6)

elif strength == "m":
	word = r.get_random_word(maxLength=6)
	num = []
	for i in range(3):
		n = random.randint(1,10)
		num.append(n)
	password = word + ''.join(str(i) for i in num)

elif strength == "s":
	word = r.get_random_word()
	letters = ""
	num = []
	for i in range(10):
		n = random.randint(1,10)
		num.append(n)
		l = random.choice(string.ascii_letters)
		letters += l
	password = word + ''.join(str(i) for i in num) + letters


print("")
print("Your password is: " + password)
print("")
