#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ans = input("Do you want Easy Password or Hard Password? Reply 'Easy' for Easy Password or 'Hard' for Hard Password. ")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

if ans == "Easy":
    print("Here is your Password: ",end="")
    for a in range(0,nr_letters):
        print(random.choice(letters),end="")
    for b in range(0,nr_symbols):
        print(random.choice(symbols),end="")
    for c in range(0,nr_numbers):
        print(random.choice(numbers),end="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

elif ans == "Hard":
    h=[]
    for a in range(0,nr_letters):
        x = random.choice(letters)
        h.append(x)
    for b in range(0,nr_symbols):
        y = random.choice(symbols)
        h.append(y)
    for c in range(0,nr_numbers):
        z = random.choice(numbers)
        h.append(z)
    
    random.shuffle(h)
    h = ''.join(h)
    print(h)

else:
    print("Sorry invalid input. Type 'Easy' for Easy Password or 'Hard' for Hard Password.")