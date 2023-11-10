# NAME: IAN NDOLO MWAU
# REG NO: SCT211-0034/2022
# Assignment on handling errors in a calculator
# implement error handling in the calculator program
class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError as err:
            return f"Error: {err}"
        except TypeError as err:
            return f"Error: {err}"
        except:
            return f"Error: {err}"
       
       
class InvalidInputError(Exception):
    pass

class EnhancedCalculator(Calculator):
    def calculate(self, num1, num2, operation):
        try:
            num1=float(num1)
            num2=float(num2)
        except ValueError:
            raise InvalidInputError("Please enter a valid number")
        if operation == "+":
            return self.add(num1, num2)
        elif operation == "-":
            return self.subtract(num1, num2)
        elif operation == "*":
            return self.multiply(num1, num2)
        elif operation == "/":
            return self.divide(num1, num2)
        else:
            raise InvalidInputError("Please enter a valid operation")
        
        
calc= EnhancedCalculator()
print(calc.calculate(5, 6, "+"))
print(calc.calculate("ian", 6, "/"))
print(calc.calculate(5, 6, "square"))      

#  end of program
