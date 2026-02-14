#Day2
#read input from users
name=input("enter your name : ")
#implicit type conversion
age=int(input("enter your age : "))
age=age+1.0

marks=float(input("enter your marks : "))
marks=int(marks)+age #explicit data conversion

print(type(name))
print(type(age))

print(f"your name is {name}")
print(f"your age is {age}")
print(f"your marks are {marks}")


#converting integers into float,string,float
num=12
print(float(num))
print(str(num))
print(bool(num))
