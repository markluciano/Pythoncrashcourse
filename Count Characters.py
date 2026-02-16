user_input = input()        #user input
target = user_input[0]
phrase = user_input[2:]
count = phrase.count(target)

if count == 1:
    print(f"{count} {target}")

else:
    print(f"{count} {target}'s")


