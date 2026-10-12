name = ""
while name == "":
    name = input("Enter your Secret Word: ")
    if name == "":
        print("You have to type something, try again!")

first = ""
while first.isdigit() == False:
    first = input("Enter your first secret number: ")
    if first.isdigit() == False:
        print("Numbers only, try again!")

second = ""
while second.isdigit() == False:
    second = input("Enter your second secret number: ")
    if second.isdigit() == False:
        print("Numbers only, try again!")

first = int(first)
second = int(second)

password = ""
count = 0

for letter in name:
    if len(password) >= 8:
        break

    a = count + first
    b = count + second
    result = a + b               
    digit = result % 10

    password = password + str(digit) + letter

    if count % 2 == 0:
        password = password + "#"
    else:
        password = password + "@"

    count = count + 1

print("Your password is:", password)
