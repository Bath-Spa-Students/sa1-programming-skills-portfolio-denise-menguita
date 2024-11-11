#Input
name = input ("What's your name?")
print(name)
#Type Cast w Integer
while True:
        try:
                age = int (input("How old are you?"))
                break
        except ValueError:
                print("Please input integer only...")  
                continue
print(age)