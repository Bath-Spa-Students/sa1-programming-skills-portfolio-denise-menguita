#Exercise 3 Biography
#Denise Marielle Menguita

name = "Denise"
hometown = "Cavite"
age = 19

print("My name is ", name, ".", "I'm from ", hometown, ", and I'm", age)

while True:
        try:
                name2 = str(input("What's your name?"))
                break
        except ValueError:
                print("Please input letters only...")  
                continue
print(name2)

while True:
        try:
                hometown2 = str(input("Where are you from?"))
                break
        except ValueError:
                print("Please input letters only...")  
                continue
print(hometown2)

while True:
        try:
                age2 = int(input("How old are you?"))
                break
        except ValueError:
                print("Please input a number...")  
                continue
print(age2)