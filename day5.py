# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Nested if
if a > b:
    if a > c:
        print("The biggest number is:", a)
    else:
        print("The biggest number is:", c)
else:
    if b > c:
        print("The biggest number is:", b)
    else:
        print("The biggest number is:", c)