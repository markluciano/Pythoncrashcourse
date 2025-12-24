#Banner for Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
treasure_art = """
  ______________________
 |                      |
 |   TREASURE ISLAND    |
 |______________________|
        \\  |  //
         \\ | //
          \\|//
           |
          / \\
         /___\\
"""
print(treasure_art)


#Decision 1: The crossroad
print("You come to a fork in the road. One path looks dark and narrow, the other bright and open. ")
choice1 = input("Do you go left or right? ").strip().lower() #figure out what strip and lower does.
if choice1 == "left":
    print("You have made the correct choice and get to continue.")


    #Decision 2: The lake
    print("You reach a massive lake. The water is still, but something moves beneath the surface.")
    choice2 = input("Do you swim across or wait? ").strip().lower()
    if choice2 == "wait":
        print("You have made the correct choice and get to continue.")


        #Decision 3: The doors
        print("You find an ancient stone building with three doors, each glowing a different color.")
        choice3 = input("Which door do you choose? Red, Yellow, or blue? ").strip().lower()
        if choice3 == "yellow":
            print("Congratulations! You found the treasure. YOU WIN")
        elif choice3 == "blue":
            print("You open the door to a room full of monsters and are eaten by beasts. Game Over")
        elif choice3 == "red":
            print("You are burned by fire and now lay as a pile of ashes. GAME OVER!")
        else:
            print("The door opens and the floor collapses, you die. GAME OVER!")













