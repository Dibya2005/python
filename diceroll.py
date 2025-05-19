dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ),
    2: (
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    )
}

import random
dice=[]
total=0
num_dice = int(input("How many dice do you want to roll? "))
for die in range(num_dice):
    die = random.randint(1, 6)
    dice.append(die)
    total += die
# for die in range(num_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
for line in range(5):
    for die in range(num_dice):
        print(dice_art[dice[die]][line], end=" ")
    print()
print("Total:", total)
        