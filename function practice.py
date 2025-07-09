#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function to add two numbers.
def add(a,b):
    return a+b
print(add(2,5))


# In[2]:


#Write a function to return the square of a number
def square(a):
    return a**2
print(square(4))


# In[5]:


#Write a function to find the factorial of a number.
def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
print(factorial(5))    



# In[7]:


#Write a function to find the greatest of two numbers
def greater(a,b):
    if a>b:
        return a 
    else:
        return b 
print(greater(5,6))    


# In[8]:


# Write a function that returns whether a number is even or odd.
def even(a):
    if a%2==0:
        print("a is even")
    else:
        print("a is odd")
even(6)        


# In[1]:


#Write a function to check if a number is prime.
def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1
    if count==2:
            print("a is prime")
    else:
            print("a is not prime")
prime(7)            


# In[10]:


# Write a function to return the sum of first n natural numbers
def total(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(total(10))


# In[11]:


#Write a function to return maximum of three numbers.
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(largest(20,33,17))    


# In[18]:


#Write a function to reverse a number.
def reverse(num):
    rev=0
    while num!=0:
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    return rev
print(reverse(1234))


# In[ ]:


#Write a function to count digits in a numbe
def count_num(num):
    count=0
    while num!=0:
        if num//10:
            count=count+1
print(count_num(1234))    


# In[23]:


#Write a function to convert Celsius to Fahrenheit.
def convert_num(celsius):
    f=(celsius*1.8)+32
    return f
print(convert_num(34))


# In[5]:


#Write a function to check whether a number is palindrome
def palindrom(name="amma"):
    rev=""
    last=len(name)-1
    for i in range(last,-1,-1):
        rev=rev+name[i]
    if rev==name:
            print("name is palindrome")
    else:
            print("name is not palindrom")
palindrom()            


# In[1]:


#2
#4 6
#8,10,12
#14,16,20
row=4
num=2
for i in range(1,row+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(num)+" "
        num=num+2
    print(pattern)    


# In[2]:


#1
#3,5
#7,9,11
#13,15,17,19
row=4
num=1
for i in range(1,row+1):
    pattern=""
    for j in range(1,i+1):
        pattern+=str(num)+" "
        num=num+2
    print(pattern) 


# In[3]:


#Write a function to check if a year is a leap year.
year=int(input("enter year"))
if year%4==0 and year%400==0 or year%100!=0:
    print("year is leap year")
else:
    print("year is not a leap year")


# In[4]:


#Write a function to check if a year is a leap year.
def leap_year(year):
    if year%4==0 and year%400==0 or year%100!=0:
        print("year is leap year")
    else:
        print("year is not a leap year")
leap_year(2000)        
    


# In[5]:


#Write a function to calculate simple interest.
def simple_intrest(p,t,r):
    I=(p*t*r)/100
    return I
print(simple_intrest(5,6,9))


# In[6]:


#Write a function to return the area of a circle.
def area_circle(r):
    A=(22/7)*r*r
    return A
print(area_circle(8))


# In[13]:


# Write a function to return all factors of a number.
def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
factors(36)      


# In[20]:


#Write a function that takes name and age and prints a message.
def fun(name,age):
    print("Hi", name + "!")
    print("Your age is", age)
fun("jyothirmai",20)    


# In[21]:


#Write a function to convert decimal to binary.
def convert_binary(num):
    print(bin(num))
convert_binary(17)    


# In[ ]:


def count_num(num):
    count=0
    while num!=0:
        if num//10:
            count=count+1
        print(count_num(1234))    



# In[ ]:


#armstrong number
num=153
num1=num
num2=num
num3=num
count=0
while num!=0:
    num=num//10
    count+=1
total=0
while num1!=0:
    last_digit=num1%10
    total=total+(last_digit**count)
    num2=num2//10
if total==num3:
    print("is armstrong")
else:
    print("is not armstrong")


# In[ ]:




