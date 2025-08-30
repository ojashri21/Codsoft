print("Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("\nEnter choice (1,2,3,4,5): ")

    if choice == "5":
        print("Exiting Calculator")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice, try again!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)