# simple calculator to take an object oriented approach
# NAME: IAN NDOLO MWAU
# REG NO: SCT211-0034/2022
class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
       
calc = Calculator(5, 6)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())

calc1 = Calculator(10, 2)
print(calc1.add())
print(calc1.subtract())
print(calc1.multiply())
print(calc1.divide())
#  end of program