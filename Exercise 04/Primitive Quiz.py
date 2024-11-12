#Exercise 4: Primitive Quiz
#Denise Marielle Menguita
'''
In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

Steps:
1) Write a program that asks the user "What is the capital of France?" and waits for their response.
2) If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3) If the answer is incorrect, the program should print a message saying the answer is wrong.

Advanced Requirements:
* Ignore Capitalization: Modify your program to accept answers regardless of the capitalization
(e.g., "paris", "Paris", and "PaRis" should all be considered correct).
* Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries.
Provide feedback for each question.
'''

#dictionary of all questions and answers
q_and_a = {
    "What is the capital of France?:": "Paris",
    "What is the capital of England?:": "London",
    "What is the capital of Greece?:": "Athens",
    "What is the capital of Italy?:": "Rome",
    "What is the capital of Germany?:": "Berlin",
    "What is the capital of Greenland?:": "Nuuk",
    "What is the capital of Switzerland?:": "Bern",
    "What is the capital of Austria? *Use the English spelling:": "Vienna",
    "What is the capital of Denmark?:": "Copenhagen",
    "What is the capital of Bulgaria? *Use the English spelling:": "Sofia"
}

#loop through each question
for question, answer in q_and_a.items():
    answer_user = input(question + " ").strip() #asks question and takes input

    if answer_user.lower() == answer.lower(): #check answer, ignore capitalization
        print("Correct!")
    else:
        print(f"Incorrect. The answer is {answer}.")