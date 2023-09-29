#name - IAN NDOLO MWAU 
#REG NO - SCT211-0034/2022
# A simple calculator to add two numbers

def calc(a, b):
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
        
    
var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number: "))
calc(var1, var2)


