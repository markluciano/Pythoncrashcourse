user_input =input()
parts = user_input.split()

if len(parts) == 3:
    first =parts[0]
    middle =parts[1]
    last =parts[2]
    print(f'{last}, {first[0]}. {middle[0]}.')

else:
    first = parts[0]
    last = parts[1]
    print(f'{last}, {first[0]}.')