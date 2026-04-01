str1="zawar"
str2="Aziz"
str3="@464"
final_str=str1+" "+str2+" "+str3
final_str=final_str.replace("zawar","shani")
final_str=final_str.capitalize()
print(final_str)
print(len(final_str))
ch=final_str[2]
print(ch)
print(final_str[1:5]+final_str[6])
print(final_str[0:len(final_str)])
print(final_str[4:1:-1])
print(final_str[-4:-1])
print(final_str[4:1:-2])
print(final_str.endswith("64"))
print(final_str.endswith("6"))
print(final_str.capitalize())
print(final_str)
print(final_str.replace("Zawar","shani"))
print(final_str.find("Shani"))
print(final_str.count("Shani"))
str4=input("Enter your name :")
print(len(str4))
print("The alphabet a occurs in your name :",str4.count("a"))

#New program of Grades
marks=int(input("Enter your marks out of 100 : "))
if(100>=marks>=90):
    print("Your grade is A ")
elif(marks>=70 and marks<90):
    print("Your grade is B")
elif(marks>=60 and marks<70):
    print("Your Grade is C")
elif(60>marks>=50):
    print("Your Grade is D")
elif(50>marks>=0):
    print("You are Fail")
#else:
    #print("Please enter correct marks")
elif(marks<0 or marks>100):
    print("You entered Invalid marks")
else:
    print("BEst of luck")

   #Even or odd number program
Number=int(input("Enter the number :"))
if(Number%7==0):
    print("Number is divisible of 7 :",Number)
else:
    print("Number is not dividsible of 7")
#Program to find Greater Number 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b and a>c):
    print("a is the greatest number")
elif(b>c and b>a):
    print("b is the greatest number")
else:
    print("c is the greatest number")
