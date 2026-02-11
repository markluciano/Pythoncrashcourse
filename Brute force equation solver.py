a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

d = int(input("Enter the fourth number: "))
e = int(input("Enter the fifth number: "))
f = int(input("Enter the sixth number: "))

found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (a * x + b * y == c) and (d * x + e * y == f):
            print(f'x = {x} and y = {y}')
            found = True
    if found:
        break
if not found:
    print("There is no solution.")