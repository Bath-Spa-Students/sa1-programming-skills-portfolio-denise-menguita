#Exercise 4: Primitive Quiz
#Denise Marielle Menguita

'''
In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

Steps:
Write a program that asks the user "What is the capital of France?" and waits for their response.
If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
If the answer is incorrect, the program should print a message saying the answer is wrong.
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct). Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
'''

#1: FRANCE - PARIS
paris = "Paris"
parisinput = (input("What is the capital of France?")) #asks question and takes input
if (parisinput.lower() == paris.lower() and parisinput.upper() == paris.upper()):
    print(paris)
    print("Correct!")

else:
    print("Incorrect. The answer is Paris.")

#2: ENGLAND - LONDON
london = "London"
londoninput = (input("What is the capital of England?")) #asks question and takes input
if (londoninput.lower() == london.lower() and londoninput.upper() == london.upper()):
    print(london)
    print("Correct!")

else:
    print("Incorrect. The answer is London.")
    
#3: GREECE - ATHENS
athens = "Athens"
athensinput = (input("What is the capital of Greece?")) #asks question and takes input
if (athensinput.lower() == athens.lower() and athensinput.upper() == athens.upper()):
    print(athens)
    print("Correct!")

else:
    print("Incorrect. The answer is Athens.")
    
#4: ITALY - ROME
rome = "Rome"
romeinput = (input("What is the capital of Italy?")) #asks question and takes input
if (romeinput.lower() == rome.lower() and romeinput.upper() == rome.upper()):
    print(rome)
    print("Correct!")

else:
    print("Incorrect. The answer is Rome.")
    
#5: GERMANY - BERLIN
berlin = "Berlin"
berlininput = (input("What is the capital of Germany?")) #asks question and takes input
if (berlininput.lower() == berlin.lower() and berlininput.upper() == berlin.upper()):
    print(berlin)
    print("Correct!")

else:
    print("Incorrect. The answer is Berlin.")
    
#6: GREENLAND - NUUK
nuuk = "Nuuk"
nuukinput = (input("What is the capital of Greenland?")) #asks question and takes input
if (nuukinput.lower() == nuuk.lower() and nuukinput.upper() == nuuk.upper()):
    print(nuuk)
    print("Correct!")

else:
    print("Incorrect. The answer is Nuuk.")
    
#7: SWITZERLAND - BERN
bern = "Bern"
berninput = (input("What is the capital of Switzerland?")) #asks question and takes input
if (berninput.lower() == bern.lower() and berninput.upper() == bern.upper()):
    print(bern)
    print("Correct!")

else:
    print("Incorrect. The answer is Bern.")
    
#8: AUSTRIA - VIENNA
vienna = "Vienna"
viennainput = (input("What is the capital of Austria?"#asks question and takes input
                   " *Use the English spelling.")) #hint
if (viennainput.lower() == vienna.lower() and viennainput.upper() == vienna.upper()):
    print(vienna)
    print("Correct!")

else:
    print("Incorrect. The answer is Vienna.")
    
#9: DENMARK - COPENHAGEN
copenhagen = "Copenhagen"
copenhageninput = (input("What is the capital of Denmark?")) #asks question and takes input
if (copenhageninput.lower() == copenhagen.lower() and copenhageninput.upper() == copenhagen.upper()):
    print(copenhagen)
    print("Correct!")

else:
    print("Incorrect. The answer is Copenhagen.")
    
#10: BULGARIA - SOFIA
sofia = "Sofia"
sofiainput = (input("What is the capital of Bulgaria?" #asks question and takes input
                   " *Use the English spelling.")) #hint
if (sofiainput.lower() == sofia.lower() and sofiainput.upper() == sofia.upper()):
    print(sofia)
    print("Correct!")

else:
    print("Incorrect. The answer is Sofia.")