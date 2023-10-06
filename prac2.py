# updated version of the calcluator program
#NAME: IAN NDOLO MWAU
#REG NO: SCT211-0034/2022

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
