#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program which takes 5 inputs from user for different subject’s

math = float(input("Enter your Mathematics obtained marks: "))
astrophysics = float(input("Enter your Astrophysics obtained marks: "))
cosmology = float(input("Enter your Cosmology obtained marks: "))
astronomy = float(input("Enter your Astronomy obtained marks: "))
programming = float(input("Enter your Programming obtained marks: "))

obt_marks = math + astrophysics + cosmology + astronomy + programming
percentage = (obt_marks/500)*100
if percentage <= 100 and percentage >= 80:
    print("\nCongrat! You passed with A+ grade with percentage of",percentage)
elif percentage <= 79 and percentage >= 70:
    print("\nExcellent! You passed with A grade with percentage of",percentage)
elif percentage <= 69 and percentage >= 60:
    print("\nNice! You passed with B grade with percentage of",percentage)
elif percentage <= 59 and percentage >= 50:
    print("\nPoor! You passed with C grade with percentage of",percentage)
elif percentage <= 49 and percentage >=0:
    print("Better Luck! You Failed the exam")
else:
    print("Your entered invalid values")


# 

# In[ ]:


"""Write a program which take input from user and identify that the given
number is even or odd?"""

num = int(input("Enter any number: "))
if num%2 == 0:
    print("You entered even number.")
else:
    print("You entered odd number.")


# In[ ]:


"""Write a program which print the length of the list"""

animals= ["Cat","Dog","Parrot","Fish","Cow","Goat"]
print(len(animals))


# In[ ]:


"""Write a Python program to sum all the numeric items in a list?"""
list = [4,5,10,15,25]
print(sum(list))


# In[ ]:



"""Write a Python program to get the largest number from a numeric list."""
num = [10,25,45,55,15,20,66,44,85,94,20,44]
print(max(num))


# In[ ]:


"""Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(0,len(a)):
    if a[i] < 5:
        print(a[i])


# In[ ]:




