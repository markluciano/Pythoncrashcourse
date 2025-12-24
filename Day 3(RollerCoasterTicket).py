print("Welcome to the rollercoaster!") #standard print statement
height = int(input("What is your height in cm?")) #input statement stored inside the height variable
bill = 0

if height >= 160:  #if statement determining if a person's height is greater than or equal to a number
    print("You can ride the rollercoaster") #standard print statement if the input is "true"
    age = int(input("What is your age?")) # is this a nested variable? this variable sits inside this if statement and is only used if true
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for yes or n for no.")
    if wants_photo == "y":
        #Add $3 to their bill
        bill += 3

    print(f"Your total bill is:${bill}")

else:
    print("Sorry you have to grow taller you short piece of shit before you can ride.")

