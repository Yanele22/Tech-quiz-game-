import json
import random


# Load questions from JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)


# Save score to file
def save_score(name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{name} - {score}\n")


# Show question
def show_question(q, number):
    print("\n" + "=" * 40)
    print(f"Question {number}")
    print("=" * 40)
    print(q["question"])

    for option in q["options"]:
        print(option)


# Check answer
def is_correct(user_answer, correct_answer):
    return user_answer.upper() == correct_answer


# Get rank
def get_rank(score):
    if score >= 50:
        return "Quiz Master"
    elif score >= 30:
        return "Tech Expert"
    elif score >= 20:
        return "Knowledge Seeker"
    else:
        return "Beginner"


# Filter by difficulty
def filter_questions(questions, level):
    return [q for q in questions if q["difficulty"] == level]


def play():
    print("=" * 40)
    print("🎮 QUIZ CHALLENGE 🎮")
    print("=" * 40)

    name = input("Enter your name: ")

    print("\nSelect Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Choose (1-3): ")

    if choice == "1":
        level = "easy"
    elif choice == "2":
        level = "medium"
    else:
        level = "hard"

    questions = load_questions()
    questions = filter_questions(questions, level)
    random.shuffle(questions)

    score = 0
    lives = 3
    streak = 0

    for i, q in enumerate(questions, start=1):

        if lives == 0:
            print("\nGame Over!")
            break

        print(f"\n❤️ Lives: {lives} | 🔥 Streak: {streak} | 💯 Score: {score}")

        show_question(q, i)

        answer = input("Your answer: ")

        if is_correct(answer, q["answer"]):
            print("Correct!")
            score += 10
            streak += 1

            if streak == 3:
                print(" STREAK BONUS +5!")
                score += 5
        else:
            print(f"Wrong! Correct answer: {q['answer']}")
            lives -= 1
            streak = 0

    print("\n" + "=" * 40)
    print(" GAME OVER")
    print("=" * 40)

    rank = get_rank(score)

    print(f"Player: {name}")
    print(f"Score: {score}")
    print(f"Rank: {rank}")

    save_score(name, score)


# Play again loop
while True:
    play()

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break

