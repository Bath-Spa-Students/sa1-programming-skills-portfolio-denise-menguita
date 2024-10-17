#Exercise 3 Biography
#Denise Marielle Menguita

'''
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

Steps:
Store the information (name, hometown, and age) as key-value pairs in a dictionary.
Print the values on separate lines using a single print() statement.
Use variables with appropriate data types for each piece of information.
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values. Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python? Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
'''

name = "Denise"
hometown = "Cavite"
age = 19

print("My name is ", name, ".", "I'm from ", hometown, ", and I'm", age)

while True:
        try:
                name2 = (input("What's your name?")) #get input from user
                break
        except ValueError:
                print("Please input letters only...")  
                continue
print(name2)

while True:
        try:
                hometown2 = (input("Where are you from?")) #get input from user
                break
        except ValueError:
                print("Please input letters only...")  
                continue
print(hometown2)

while True:
        try:
                age2 = int(input("How old are you?")) #get int input from user
                break
        except ValueError:
                print("Please input a number...")  
                continue
print(age2)