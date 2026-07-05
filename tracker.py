name = input("What is your name? ")
salary = float(input("What is your salary? "))
expenses = float(input("What are your expenses? "))

savings = salary - expenses

print("Hello " + name)
print("Your monthly savings are: " + str(savings))
print("Your annual savings are: " + str(savings * 12))

print(f"Hello {name}")
print(f"Your monthly savings are: {savings}")
print(f"Your annual savings are: {savings * 12}")
