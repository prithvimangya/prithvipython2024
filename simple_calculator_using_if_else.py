num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))
operation = input("Enter operation(+, -, *, /):")
if operation == '+':
  print("Result:", num1 + num2)
if operation == '-':
  print("Result:", num1 - num2)
if operation == '*':
  print("Result:", num1 * num2)
if operation == "/":
  print("Result:", num1 / num2)
if operation == '//':
  print("Result:", num1 // num2)
if operation == '%':
  print("Result:", num1 % num2)
if operation == ('**'):
  print("Result:", num1 ** num2)
else:
  print("Invlid operation")
