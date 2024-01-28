# This is test for Math Section
# Techlink@Directory

import random


def generate_question():
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operation: addition, subtraction, or multiplication
    operation = random.choice(['+', '-', '*'])

    # Construct the math question
    question = f"{num1} {operation} {num2}"

    # Calculate the correct answer
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2

    return question, answer

user_opt = input("Do you want to do math practice?\n")


def main():
    # Set the number of questions you want
    num_questions = int(input("How many questions would you like to try?\n"))

    for _ in range(num_questions):
        # Generate a question and get the correct answer
        question, correct_answer = generate_question()

        # Ask the question and get the user's answer
        user_answer = input(f"What is {question}? ")

        total_score = []
        # Check if the user's answer is correct
        if int(user_answer) == correct_answer:
            print("Correct!")
            total_score.append("1")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

        

if user_opt == "Yes":
    main()
else:
    print("Okay! Come back when you are ready!!")