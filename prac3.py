#NAME- IAN NDOLO MWAU
#REG NO- SCT211-0034/2022
#PROGRAM- TIP CALCULATOR

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