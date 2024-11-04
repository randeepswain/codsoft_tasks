num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")

operation = input("Enter the operation (1,2,3 or 4): ")


if operation == '1':
    result = num1 + num2
    op_symbol = '+'
elif operation == '2':
    result = num1 - num2
    op_symbol = '-'
elif operation == '3':
    result = num1 * num2
    op_symbol = '*'
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        op_symbol = '/'
    else:
        result = "undefined (division by zero)"
        op_symbol = '/'
else:
    result = "invalid operation"
    op_symbol = '?'


if operation in ['1', '2', '3', '4']:
    print(f"The result of {num1} {op_symbol} {num2} = {result}")
else:
    print("Invalid operation choice")
