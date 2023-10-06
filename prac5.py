#NAME- IAN NDOLO MWAU
#REG NO- SCT211-0034/2022

#PROGRAM- LEAP YEAR CALCULATOR
name = input("Enter your first name: ")

print("Welcome to the leap year calculator", name)

# input from the user
year = int(input("Enter the year: "))
# calculation
if year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")
# end of program

