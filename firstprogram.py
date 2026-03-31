#Calculator
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
sum=a+b
subtract=a-b
multiply=a*b
divide=a/b
operation=input("Which operation you want to do (sum,divide,subtract,multiply): ")
if operation=="sum":
    print(a+b)
elif operation=="divide":
    print(a/b)
elif operation=="multiply":
    print(a*b)
elif operation=="subtract" and a>b:
    print(a-b)
else:
    print("First number is less than second number")






