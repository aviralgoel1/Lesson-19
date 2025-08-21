n = int(input("Enter a number: "))
odd= [i for i in range(1, n) if i % 2 != 0]
even= [i for i in range(1, n) if i % 2 == 0]

print("Odd: ", odd)
print("Even: ", even)

fruits = ["apple", "banana", "mango", "grapes", "orange"]
cap_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruits list:", cap_fruits)
