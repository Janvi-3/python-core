import json
import os

# Load quiz data from JSON file
def load_quiz(difficulty):
    file_name = f"{difficulty}_quiz.json"
    path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return {}

# Run the quiz
def run_quiz(quiz_data):
    score = 0
    total = 0

    for category in quiz_data:
        print(f"\n--- {category} ---")
        questions = quiz_data[category]
        for q in questions:
            print(f"\n{q['Question']}")
            options = q['Options']
            for i in range(len(options)):
                print(f"{i + 1}. {options[i]}")
            try:
                user_input = input("Enter your answer (1-4): ")
                ans = int(user_input)
                if 1 <= ans <= 4:
                    if options[ans - 1] == q['Answer']:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! Correct answer: {q['Answer']}")
                    total += 1
                else:
                    print("Please enter a number between 1 and 4.")
            except:
                print("Invalid input. Skipping question.")

    print(f"\nYour Score: {score}/{total}")

# Main function
def main():
    print("Welcome to the GK Quiz App!")
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    elif choice == "3":
        difficulty = "hard"
    else:
        print("Invalid choice. Please restart and try again.")
        return

    quiz_data = load_quiz(difficulty)
    if quiz_data:
        run_quiz(quiz_data)

if __name__ == "__main__":
    main()
