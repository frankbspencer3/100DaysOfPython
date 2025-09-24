import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #easy mode
# pw = ""
# for i in range(nr_letters):
#     pw += random.choice(letters)
# for i in range(nr_symbols):
#     pw += random.choice(numbers)
# for i in range(nr_numbers):
#     pw += random.choice(symbols)
# print(pw)

# #hard mode
# pw = ""
# for i in range(nr_letters):
#     pw += random.choice(letters)
# for i in range(nr_symbols):
#     pw += random.choice(numbers)
# for i in range(nr_numbers):
#     pw += random.choice(symbols)
# print(pw)
# shufflepw = list(pw)
# random.shuffle(shufflepw)
# pw="".join(shufflepw)
# print(pw)

#hard mode v2
pw = []
for i in range(nr_letters):
    pw.append(random.choice(letters))
for i in range(nr_symbols):
    pw.append(random.choice(numbers))
for i in range(nr_numbers):
    pw.append(random.choice(symbols))
print(pw)
random.shuffle(pw)

password = ""
for i in pw:
    password += i
print(password)