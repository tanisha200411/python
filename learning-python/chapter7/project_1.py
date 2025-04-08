import random
# write a python program capable of playing this game with the user

"""
   -1 = snake
    1 = water
    0 = gun

"""

you_dict = {"s": -1, "w": 1, "g": 0}
reverse_dict = {-1: "snake", 1: "water", 0: "gun"}

computer = random.choice([-1, 0, 1])
you_str = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if you_str not in you_dict:
    print("Invalid choice! Please enter 's', 'w', or 'g'")
else:
    you = you_dict[you_str]

    print(f"\nYOU CHOSE      : {reverse_dict[you]}")
    print(f"COMPUTER CHOSE : {reverse_dict[computer]}\n")

    if you == computer:
        print("It's a draw!")
    elif (you == -1 and computer == 1) or (you == 1 and computer == 0) or (you == 0 and computer == -1):
        print("🎉 You win!")
    else:
        print("💻 Computer wins! \n You lose !")

