marks=[6.2, 5.9, 60.8, 92.4]
print(marks)
print(marks[0 : 3])
print(marks[3 : 0 : -1])
print(marks[-1 : -4 : -1]) #if we want slicing from left to right we have to use -1
print(marks[-3 : -1])
print(len(marks))
marks.append(50.5) # add something at he end of the list
print(marks)
str=("11"+"15"+"20")
print(int(str))
# str=int(str)
print(str)
print(str[0])
print(str[0 : 2])
print(str[2 : 0 : -1])
print(str[-1 : -3 : -1])
print(str[-3 : -1])
print(len(str))
print(type(str))
marks[0]=9.2# We can change the index in listing but not in string 
print(marks)
#str[0]=2
# print(str)
print(marks.sort()) #arrange the list in ascending order
print(marks.sort(reverse=True)) # arrange the list in descending order
print(marks)
marks.reverse() # arrange the list in the reverse order 
print(marks)
marks.insert(2,20.6)# insert (write index before we want to add and then the number we want to add)
print(marks)
marks.remove(20.6) #remove the number from the list 
print(marks)
marks.pop(2) # removes the number on that index from the list
print(marks)
# Tuples are like list but in tuples we cannt change specifix index value like list , they are immutable like strings
tup=(2,3,5,8)
print(type(tup))
print(tup[1])
# tup[1]=7 We cannot change the index value in tupple but we can in list
tup2=(4,) # if we want to write single value in tup we also type coma , to avoid this tuple from int type
print(tup2)
print(type(tup2))
 #  Slicing is same in tuple as string and list 
# If we want to find the index of some value we use index operation like this
tup.index(5)
print(tup.index(5))
# if we want to check specific number exixts how many times in tup we use this operation
tup.count(8)
print(tup.count(5))
##################Program ############################
Movies=[]
Movie1=input("Enter your favrt movie 1 : ")
Movie2=input("Enter your favrt movie 2 :")
Movie3=input("Enter your favrt movie 3 :")
Movies.append(Movie1)
Movies.append(Movie2)
Movies.append(Movie3)
print(Movies)
# ############# Program #################################
list1=[]
num1=input("Enter first num : ")
num2=input("Enter second number : ")
num3=input("Enter third number : ")
list1.append(num1)
list1.append(num2)
list1.append(num3)
list2=list1.copy()
list2.reverse()
if(list1==list2):
    print("List is palindrome :",list1)
else:
    print("List is not palindrome :",list1)
##############Program###################################
tup=("A", "B", "A", "C", "A")
print("Students with Grade A : ",tup.count("A"))
list=["A", "B", "A", "C", "A"]
list.sort()
print(list)
########   End of todays lecture 3 work ###################
