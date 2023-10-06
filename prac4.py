#NAME - IAN NDOLO MWAU
#REG NO - SCT211-0034/2022

#PROGRAM - BMI CALCULATOR

# input from the user
# weight in kg
# height in m
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
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
