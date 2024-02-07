from calculator import Calculator

# main program
casio_calculator = Calculator(14, 7, 'grey','Casio775')

sony_calculator = Calculator(10, 25, 'white', 'SonyFw20')

# instance methods _ calc_body_area()
print(f'Area of Casio calculator = {casio_calculator.calc_body_area()}')
print(f'Area of Sony calculator = {sony_calculator.calc_body_area()}')

# static method : method which result doesn't change from object to another for the same parameters
# static method to be called from class name | self to be removed from method parameters
result = Calculator.add(4, 7)
print(result)