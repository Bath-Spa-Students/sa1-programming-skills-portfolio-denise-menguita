#if
x = 25
y = 15

if (x>y):
        print("x is greater than y")

#if-else w/o input
temperature = 40
if(temperature <= 40):
        print("A little cold, isn't it?")
else:
        print("Nice weather we're having.")

#if-else w/ input 1
temperature = int(input("What is the temperature?"))

if(temperature <= 40):
        print("A little cold, isn't it?")
else:
        print("Nice weather we're having.")

#if-else w/ input 2
sales = int(input("How much sales did the company make this month?"))
if(sales > 50000):
        bonus = float(500)
        print("Everyone gets a bonus of", bonus)
else:
        print("No one gets a bonus.")

#nested if
earning = int(input("Enter your earnings per year: "))
work_exp = float(input("Enter your work experience: "))

if earning >= 30000:
        if work_exp >= 2:
                print("You are eligible for a loan.")
        else:
                print("You do not have enough working experience. You are not eligible for a loan.")

else:
        print("You do not earn enough. You are not eligible for a loan.")