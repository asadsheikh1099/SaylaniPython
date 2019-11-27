#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Make a calculator using Python with addition , subtraction , multiplication , 
#division and power.


operator = input("Wanna Perform addition, subraction, multiplication, division or square? \nEnter an operator: ")
value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))

if operator == "add" or operator == "+":
    print("Sum of given values is: ",value1+value2)
elif operator == "minus" or operator == "-":
    print("Subraction of given values is: ",value1-value2)
elif operator == "multiply" or operator == "*":
    print("Multiplication of given values is: ",value1*value2)
elif operator == "divide" or operator == "/":
    print("Division of given values is: ",value1/value2)
elif operator == "square" or operator == "**":
    print("Square of given values is: ", value1**value2)
else:
    print("You Entered incorrect operator.")


# In[ ]:


#Write a program to check if there is any numeric #value in list using for loop 


list = ["Cat",2,"Boy",5,6.,"Pen",7.6,False,None,3e8]
for i in range(0,len(list)):
        if type(list[i]) == float or type(list[i]) == int:
            numeric = print("Numeric values from the list is: ",list[i])


# In[ ]:


#Write a Python script to add a key to a dictionary 

print("\nCurrent Dictionary is;")
dic = {"University":"University of Karachi","Department":"Institute of Space Science and Technology","Batch":2019,"Student Name":"Hafeez Ghanchi"}
print(dic)

print("\nUpdated Dictionary is;")
new_dic = {"Student ID":"EH1918015","Major":"Astrophysics"}
dic.update(new_dic)
print(dic)


# In[ ]:


#Write a Python program to sum all the numeric items in a dictionary 

dic = {"Math":80,"Physics":94,"Astrophsics":88,"Programming":82}

mark = sum(dic.values())
percentage = (mark/400)*100

print("Your obtained marks is",mark,"with percentage of",percentage)


# In[ ]:


#Write a program to identify duplicate values from list 

list = ["Hammer",24,.75,"Cow",3e8,"Hammer",50,.75,"Beast","Beast",3e8]
duplicate = []
for i in range(len(list)):
    inc = i+1
    for j in range(inc,len(list)):
        if list[i] == list[j] and list[i] not in duplicate:
            duplicate.append(list[i])
print("Duplicate values from a list is: ",duplicate)


# In[ ]:


#Write a Python script to check if a given key already exists in a dictionary 

dic = {"Student1":"Hafeez","Student2":"Sameer","Student3":"Asad","Student4":"Mehmood","Student5":"Hamza"}
duplicate = {}
print(dic)
key = "Student1"
if key in dic.keys(): 
        print(key," is present and his name is ",dic[key])
else:
        print("Not present")


# In[ ]:




