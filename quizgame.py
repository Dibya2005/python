questions = (
    "How many elements are in the periodic table?",
    "Which animal lays the largest eggs?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Crocodile", "B. Whale", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 201", "C. 210", "D. 196"),
    ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter")
)

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0

for question_num in range(len(questions)):
    print("\nQuestion", question_num + 1, ":", questions[question_num])
    for option in options[question_num]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is", answers[question_num])

print("\nYour score is:", score, "out of", len(questions))
