#NAME: IAN NDOLO MWAU
#REG NO: SCT211-0034/2022

# summation program 
def calc(a, b):
    a=int(a)
    b=int(b)
    var = input("Enter the operation: ")
    if var == "a":
        print(a+b)
    elif var == "s":
        print(a-b)
    elif var == "m":
        print(a*b)
    elif var == "d":
        print(a/b)
    else:
        print("invalid operation")

# age calculator program
def age_calculator(num1, num2):
    # num1 = year of birth
    # num2 = current year
    name = input("Enter your name: ")
    print("welcome to the improved calculator program", name)
    # input from the user
    num1 = int(input("Enter your year of birth: "))
    num2 = int(input("Enter the current year: "))
    # calculation
    age_year = num2 - num1
    age_month = age_year * 12
    age_days = age_year * 365
    print("Your age in years is: ", age_year)
    print("Your age in months is: ", age_month)
    print("Your age in days is: ", age_days)
    # end of program
    
    
#tip calculator program as a function
def tip_calculator():
    # input from the user
    bill = float(input("Enter the total bill: "))
    tip = int(input("Enter the percentage of tip(10,12 OR 15): "))
    var1 = input("Are you splitting the bill? (yes/no): ")
    if var1 == "yes":
        num = int(input("Enter the number of people: "))
        total = bill + (bill * tip/100)
        each = total / num
        print("Each person should pay: ", round(each, 2))
    elif var1 == "no":
        total = bill + (bill * tip/100)
        print("The total bill is: ", round(total, 2))
    else:
        print("Invalid input")
    # end of program
    
    # BMI calculator program as a function
    # input from the user
    # weight in kg
    # height in m

def BMI_CALCULATOR(weight, height):
     
    weight = float(weight)
    height = float(height)
    # calculation
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Your BMI is: ", round(bmi, 2))
        print("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Your BMI is: ", round(bmi, 2))
        print("You are normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Your BMI is: ", round(bmi, 2))
        print("You are overweight")
    elif bmi >= 30:
        print("Your BMI is: ", round(bmi, 2))
        print("You are obese")
        
    # end of program  

    # leap year calculator program as a function
    # input from the user
    # year
def leap_year(year):
    year = int(year)
    # calculation
    if year % 4 == 0 and year % 100 != 0:
        print("The year is a leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
    # end of program
    



