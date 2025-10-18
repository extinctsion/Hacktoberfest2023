#ask for the user input
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


operation = input("Choose one operation from the following-(1)ADD, (2)SUBTRACT, (3)MULTIPLY, (4)DIVIDE: ")


#conditional statements
if operation == "ADD":
    sum = first_number+second_number
    print(sum)
elif operation == "SUBTRACT":
    subtract = first_number-second_number
    print(subtract)
elif operation == "MULTIPLY":
    multiply = first_number*second_number
    print(multiply)
elif operation == "DIVIDE":
    divide = first_number/second_number
    print(divide)
else:
    print("Input Required")