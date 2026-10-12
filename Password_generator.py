
name = ""
while name == "":
    name = input("Enter your Secret Word: ").strip()
    if name == "":
        print("You have to type something, try again!")

first = ""
while not first.isdigit():
    first = input("Enter your first secret number: ")
    if not first.isdigit():
        print("Numbers only, try again!")

second = ""
while not second.isdigit():
    second = input("Enter your second secret number: ")
    if not second.isdigit():
        print("Numbers only, try again!")

first = int(first)
second = int(second)

password = ""
count = 0

for letter in name:
    digit = (count + first + count + second) % 10
    password += str(digit) + letter

    if count % 2 == 0:
        password += "#"
    else:
        password += "@"

    count += 1

    if len(password) >= 8:
        password = password[:8]
        break

print("Your password is:", password)
