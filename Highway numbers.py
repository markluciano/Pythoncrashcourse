highway_number = int(input("Enter highway number: "))

if highway_number < 1 or highway_number > 999: #checks for valid numbers
    print(f'{highway_number} is not a valid highway number.')
elif 1 <= highway_number <= 99:
    if highway_number % 2 == 0:
        direction = "east/west"
    else:
        direction = "north/south"
    print(f'I-{highway_number} is primary going {direction}.')
else:
    primary = highway_number % 100
    if primary == 0: #checks for valid numbers
        print(f'{highway_number} is not a valid highway number.')
    else:
        if primary % 2 == 0: #determines direction "even numbers = east/west"
            direction = "east/west"
        else:
            direction = "north/south"
        print(f'I-{highway_number} is auxiliary, serving I-{primary} going {direction}.')

