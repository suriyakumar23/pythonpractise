#write  a program to print reverse of given array list
'''a=[1,2,3,4,5,6,7]
print(a)
n=len(a)-1
for i in range(n//2+1): #midvalue of given array
    temp=a[i]
    a[i]=a[n-i]
    a[n-i]=temp
    print(a)

#another method
a=[1,7,5,4,3,2]
print(a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)'''

#write a program to print a duplicate numbers in given array::

'''number=[2,3,4,6,4,3,2]
unique=[]
duplicate=[]
for i in number:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
print(duplicate)'''

#write a program to sum of elements in even index position after reversing a given array::

'''array=[10,20,40,60,70,80,90]
n=len(array)
sum=0
array.reverse()
print(array)
for i in range(0,n,2):
    if i%2==0:
        print(array[i])
        sum+=array[i]
print("sum is:",sum)'''

#write a program to convert a below string
'''name="I am Surya"
reversename=name[:: -1]
split=reversename.split()
print(split)

for c in split:
    print(len(c),c)'''

#write a program to find max element

'''a=[2,3,47,5,6,20]
max=0
for i in a:
  if i>max:
    max=i
print("maximum is:",max)'''

#write a program to find intersection

'''a=[1,2,3,4,5,6]
b=[7,8,9,1,2,4]
intersection=[]
for i in a:
    if i in b:
        intersection.append(i)
print("intersection is :",intersection)'''

#write a program to find the unique elements in given list without using inbuilt function

'''a=[1,2,3,4,5,6,7,8,9,1,2,4,7,7,7]
unique=[]

for i in a:
    if i not in unique:
        unique.append(i)
print("unique number is:",unique)'''

#write a program to convert the given string

'''string="11101011110"
count=0

for i in string:
    if i=="1":
        count+=1
    else:
        print(chr(64+count),end="")
        count=0'''

# writr a program to convert a below string...
n=76
num=0
while n>0:
    last=n%10
    num=num+last
    n=n//10
print(num)
for i in range(2,n):
    if(i%2==0):
        print(num,"its a even number")
else:
    print(num,"its not a even number")

# writr a program to reverse

'''a=7669
reverse=0
while a>0:
    last=a%10
    reverse=reverse*10+last
    a=a//10
print(reverse)'''


#write a program to find palindrome

'''name=input("enter the string:")
palindrome_string=name[::-1]
if(palindrome_string==name):
    print("its a palindrome")
else:
    print("not a palindrome")'''
#another method

'''def is_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
input_string=input("enter a string:")

if is_palindrome(input_string):
    print(input_string,"its a palindrome")
else:
    print(input_string,"not a palindrome")'''

#write a program to find a factorial

'''n=5
f=1
if(n>=0):
    if n==0:
        print("factorial")
    else:
        for i in range(f,n+1):
             f=f*i
    print("factorial of ",n,"is",f)'''

#write a program to find prime from 1 to 100

'''n=100
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
            print(i,end=" ")'''

#write a program to find leap year
'''n=int(input("enter a year:"))
if(n%4==0 and n%100!=0) or (n%400==0):
    print("leap year")
else:
    print("not a leap year")'''

#wite a program to sum the prime number with given n value as a input

'''n=int(input("enter a number:"))
sum=0
d=0
for i in range(2,n+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        sum+=i
print(sum)'''

#write a program to print true if there is consecutive primenumber is there

'''num=[1,2,34,56,7,9,12]
n=len(num)
count=0
for i in range(n):
    if num[i]%2 !=0:
        count+=1
        if count>=3:
            print("True")
            break
    else:
        count=0
if count<3:
    print("False")'''

#write a program to running sum in array

'''a=[1,2,3,4,5,6,7,8]
sum=[]
s=0
n=len(a)
for i in range(n):
    s=s+a[i]
    sum.append(s)
print(sum)'''

#print a character which not in first string

'''a="surya"
b="suryaz"
for i in b:
    if i not in a:
        print(i)'''
    
#write a program to find the avg number which is divisible by 3 and it should be even in array:

'''nums=[12,23,45,15,18,24,30,36]
n=len(nums)
numone=[]
average=0
for i in range(0,n):
    if nums[i]%2==0 and nums[i]%3==0:
        numone.append(nums[i])
        average+=nums[i]
average=average//len(numone)
print("after sorted:",numone)
print("Average is:",average)'''

#star
'''n=5
for i in range(n):
    print("  "*i +"* "*(2*n-(2*i)-1))'''

#write a program to print below pattern ;;
'''count=10
primes=[]
num=2
while len(primes)<count:
    prime_flag=1

    if num<2:
        prime_flag=0
    for i in range(2,num):
        if num%i==0:
            prime_flag=0
            break
    if prime_flag==1:
        primes.append(num)
    num+=1

#to print
index=0
for i in range(1,5):
    for j in range(i):
        print(primes[index],end=" "*(5-len(str(primes[index]))))
        index+=1
    print()'''


#write a program for abcde

'''index=1
for i in range(1,6):
    for j in range(i,6):
        print(chr(64+j),end=" ")
    print()'''

#find the min value in array and index

'''nums=[7,8,9,11,12,1,34]
n=len(nums)
minimum=nums[0]
for i in range(n):
    if nums[i]<minimum:
        minimum=nums[i]
        index=i
print("minimum value is:",minimum,"index value is:",index)'''

#seacrh a integer in given list
'''nums=[2,3,4,5,6,17,8,19]
n=len(nums)
search=17
for i in range(n):
    if nums[i]==search:
        print(search,"found at index:",i)
        break
else:
        print("Not found")'''

#write a program to move all zero to last in given list

'''nums=[0,1,0,3,5,6,0,23,31,0,77,0,98,66,0,12]
n=len(nums)
left=0
for i in range(n):
    if nums[i]!=0:
        temp=nums[i]
        nums[i]=nums[left]
        nums[left]=temp
        left+=1
print(nums)'''

#write a prgram to reverse a array
'''nums=['h','e','l','l','o']
n=len(nums)-1
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)'''

#string is valid ifits have open and closing bracket

'''s="()[]{}"
num=""
n=len(s)
for i in range(0,n,2):
    if(s[i]=="("and s[i+1]==")"or s[i]=="["and s[i+1]=="]" or s[i]=="{" and s[i+1]=="}") :
        num+=s[i]
        num+=s[i+1]
    else:
        print("Not valid")
        break
else:
    print("A string is valid ")'''

#write a program to sum of cubes
'''a=1
b=5
sumofcubes=0
for i in range(a,b+1):
    sumofcubes+=i*i*i
print(sumofcubes)'''

#to check program is anagram

'''a="rat"
b="art"
a=sorted(a)
b=sorted(b)
n=len(a)
if len(a)!=len(b):
    print("Not anagram")
else:
    for i in range(n):
        if a[i]!=b[i]:
            print("Not Anagram")
            break
    else:
        print("Its Anagram")'''

#move to zero at last..
'''a=[12,3,4,0,9,8,7,6,0,34,0,14,13]
b=len(a)
left=0
for i in range(b):
    if a[i]!=0:
        temp=a[i]
        a[i]=a[left]
        a[left]=temp
        left+=1
print(a)'''

#armstrongnumber

'''def isarmstrong(number):
    temp=number
    noofdigits=0
    while temp>0:
        temp=temp//10
        noofdigits+=1
    temp=number
    sumofpower=0
    while temp>0:
        digit=temp%10
        sumofpower+=digit**noofdigits
        temp=temp//10
    if sumofpower==number:
        return True
    else:
        return False
n=int(input("Enter a number:"))
if isarmstrong(n):
    print(n,"is a Armstrong number")
else:
    print(n,"not a Armstrong number")'''

#write a program to print following
#output:sync
#fusi without slicing method

'''str="syncfusion"
a=len(str)
count=0
word=""
for i in range(a):
    if count==4:
        print(word)
        count=1
        word=""
    else:
        count+=1
    word=word+str[i]'''


#remove empty space from start and end

'''str=" hello world "
b=len(str)
inword=0
cleaned_string=""
spacebetween=0
for i in range(b):
    if str[i]!=' ':
        if spacebetween==1:
            cleaned_string+=' '
            spacebetween=0
        cleaned_string+=str[i]
        inword=1
    else:
        if inword==1:
            spacebetween=1
        inword=0
print(cleaned_string)'''

#another method
'''def cleaned_string(str):
    inword=0
    clean_string=""
    spacebetween=0
    for i in range(len(str)):
        if str[i]!=" ":
            if spacebetween==1:
                clean_string+=" "
                spacebetween=0
            clean_string+=str[i]
            inword=1
        else:
            if inword==1:
                spacebetween=1
            inword=0
    return clean_string
str=" hello  world  "
print(str)
clean_string=cleaned_string(str)
print(clean_string)'''

#after reverse array find max and min

'''def revmax_min(arr):
    reversedarray=[]
    for i in range(len(arr)-1,-1,-1):
            reversedarray.append(arr[i])
    min_num=arr[0]
    max_num=arr[0]
    for i in arr:
          if i<min_num:
                min_num=i
          if i>max_num:
                max_num=i
    return reversedarray,min_num,max_num
arr=[23,45,34,67,89,65,11,77]
reversedarray,min_num,max_num=revmax_min(arr)
print("original array:",arr)
print("reversedarray:",reversedarray)
print("minimum is:",min_num)
print("maximum is:",max_num)'''

#another method
'''def rev(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    min_num=arr[0]
    max_num=arr[0]
    for i in arr:
        if i<min_num:
            min_num=i
        if i>max_num:
            max_num=i
    return arr ,min_num,max_num
str=[23,45,6,78,98,76,65]
print(str)
reversed_string,min_num,max_num=rev(str)
print("reversedarray:",reversed_string)
print("minimum is:",min_num)
print("maximum is:",max_num)'''

#write a  program  to print a list with given input which is divisible

'''input=60
find=[]
for i in range(1,input):
    if input%i==0:
        find.append(i)
print(find)'''

'''a=[23,45,0,87,66,0,55,0,27,0,0,12,34,]
b=len(a)-1
left=0
for i in range(len(a)):
    if a[i]!=0:
        temp=a[i]
        a[i]=a[left]
        a[left]=temp
        left+=1
print(a)'''

#move zero at last position just using to replace index value
'''a = [0,23, 45, 0, 87,0, 66, 0, 55, 0, 27, 0, 0, 12, 34]
left = 0  # Tracks the position for non-zero elements
right = len(a) - 1  # Tracks the position for zeros from the right end

while left <= right:
    if a[left] == 0:
        # Swap zero at 'left' with the element at 'right'
        a[left], a[right] = a[right], a[left]
        right -= 1  # Decrement right since we placed a zero
    else:
        left += 1  # Increment left when encountering a non-zero element
print(a)'''

#pyramid number
'''rows = 5  # You can adjust the number of rows for the pyramid

for i in range(1,rows+1):  #print space
    for j in range(rows-i):
        print(" ",end="")

    for k in range(1,i+1): #print numbers in increasing order
        print(k,end="")
    for l in range(i-1,0,-1):#print numbers in decreasing order
        print(l,end="")
    print()'''

#sum in given input
'''nums=66
sum=0
#count=0
while nums>0:
    lastdigit=nums%10
    sum=sum+lastdigit
    nums=nums//10
    #count+=1
print(sum)
#print("executed by:",count)'''

#write a program to find factors and prime numbers of factors given input

'''n=210
factors=[]
primefactors=[]
for i in range(2,n):
    if n%i==0:
        factors.append(i)
for i in factors:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        primefactors.append(i)
print("Factors is:",factors)
print("Primefactors is:",primefactors)'''

#find th max number i in given array with a index of k
'''a=[1,2,3,4,5,3,2,12,4,5,6]
b=len(a)
k=3
maximum=[]
for i in range(b-k+1):
    maxi=max(a[i:i+k])
    maximum.append(maxi)
print(maximum)'''
#another method
'''a=[1,2,3,4,5,3,2,12,4,5,6]
b=len(a)
k=3
maximum=[]
for i in range(b-k+1):
    currentmax=a[i]
    for j in range(1,k):
        if a[i+j]>currentmax:
            currentmax=a[i+j]
    maximum.append(currentmax)
print(maximum)'''

#given an integer array,nums calculate the product(array/list) of all elements in a given list except for the elements itself nums[i]
'''nums=[2,5,7,8,9]
n=len(nums)
products=[]
product=1
for i in range(n):
    for j in range(n):
        if nums[i]==nums[j]:
            pass
        else:
            product*=nums[j]
            print(product,end=",")
    products.append(product)
    product=1
print(products)'''

#write a program to find max avg of k-length subarray in nums

'''nums=[1,12,-5,-6,50,3]
n=len(nums)
k=4
maxi=0
for i in range(n-k+1):
    maxavg=sum(nums[i:i+k])/k
    maxi=max(maxavg,maxi)
    print(sum(nums[i:i+k])/k)
    print(maxi)
print(maxi)'''

'''nums=[1,12,-5,-6,50,3,5,4,3]
n=len(nums)
k=4
maxi=0
maxavg=0
for i in range(n-k+1):
    d=sum(nums[i:i+k])/k
    if d>maxavg:
        maxavg=d
print(maxavg)'''
'''
#python pattern programs
rows=5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()'''
#write a program to find the leap year with start end end year
'''print("Leap years are:",end="")
start=2000
endto=2070
for i in range(start,endto+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        print(i,end=" ")'''

#factorial using recursive
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=5
s=fact(n)
print("fact is:",s)'''
    
#fibonacci using recursive
'''def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=10
s=fibo(n)
print("fibo is:",s)'''

'''nums=[1,23,45,0,8,0,6,0,5,0,0,3,34,56]
b=len(nums)
left=0
for i in range(b):
    if nums[i]!=0:
        temp=nums[i]
        nums[i]=nums[left]
        nums[left]=temp
        left+=1
print(nums)'''

'''n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f)'''

#diamond star
'''n=1
f=5
s=2
v=4
while n<6 and f>0:
    print(" "* f,end="")
    print("* "* n)
    n+=1
    f-=1
while v>0 and s<6:
    print(" "* s,end="")
    print("* "* v)
    v-=1
    s+=1'''

#left arrow star
"""
n=1
upperlimit=5
upperspace=5
lower=4
lowerspace=2
#upper star
while n<=upperlimit:
    print(" "* upperspace,end="")
    print("*"* n,end=" ")
    n+=1
    upperspace-=1
    print()
#lower star
while lower>0:
    print(" "* lowerspace,end="")
    print("*"* lower,end=" ")
    print()
    lower-=1
    lowerspace+=1
"""
#conversation of whole string into either upper or lower case it should be one of these two cases
'''str1="HELLO WORLD"
if ord(str1[0])<97:
    lowercase=str1.lower()
    print(lowercase)
else:
    uppercase=str1.upper()
    print(uppercase)'''

'''def tolowercase(s):
    result=""
    for char in s:
        if 'A'<=char<='Z':
            result+=chr(ord(char)+32)
        else:
            result+=char
    return result
def touppercase(s):
    result=""
    for char in s:
        if 'a'<=char<='z':
            result+=chr(ord(char)-32)
        else:
            result+=char
    return result
str1='hello world'
if ord(str1[0])<97:
    print(tolowercase(str1))
else:
    print(touppercase(str1))'''

#armstrong
'''def countcheck(num):
    count=0
    temp=num
    while temp>0:
        count+=1
        temp//=10
    return count
def power(base,exp):
    if exp==0:
        return 0
    elif exp==1:
        return base
    else:
        return base*power(base,exp-1)
def isarmstrong(num):
    num_digit=countcheck(num)
    temp=num
    sumofpower=0
    while temp>0:
        digit=temp%10
        sumofpower+=power(digit,num_digit)
        temp//=10
    return sumofpower==num
n=int(input("enter a number to check:"))
if isarmstrong(n):
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")'''

# Python program to demonstrate instantiating
# a class
'''class Dog:

	# A simple class attribute
	attr1 = "mamal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)
		
	def greet(self):
	    print("hope you are doing well")


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes and method through objects
print(Rodger.attr1)
print(Rodger.attr2)
Rodger.fun()
Rodger.greet()'''

'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sk(self):
        print("name:",self.name)

v=person("sk",23)
v.sk()'''

'''class Animal:  # Parent class
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inheritance (Dog inherits Animal)
    def bark(self):
        print("Dog barks")
d=Dog()
d.speak()
d.bark()'''
'''
class Color:

    # constructor method

    def __init__(self):

        # object attributes

        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print('Name:', self.name)

    # create Inner Lightgreen class

    class Lightgreen:

        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)

# create Color class object
outer = Color()


# method calling
outer.show()

# create a Lightgreen
# inner class object

g = outer.lg

# inner class method calling

g.display()'''

'''def cleamed_string(str):
    inword=0
    spacebetween=0
    cleanstring=""
    for i in range(len(str)):
        if str[i]!=" ":
            if spacebetween==1:
                cleanstring+=" "
                spacebetween=0
            cleanstring+=str[i]
            inword=1
        else:
            if inword==1:
                spacebetween=1
            inword=0
    return cleanstring
str="  hello  world  "
print(str)
print(cleamed_string(str))'''

'''a=[1,2,3,4,5,3,2,12,4,5,6]
b=len(a)
k=3
maxi=[]
for i in range(b-k+1):
    currentmax=a[i]
    for j in range(1,k):
        if a[i+j]>currentmax:
            currentmax=a[i+j]
    maxi.append(currentmax)
print(maxi)'''

'''a=[2,3,4,5,6]
n=len(a)
products=[]
product=1
for i in range(n):
    for j in range(n):
        if a[i]==a[j]:
             pass
        else:
            product*=a[j]
    products.append(product)
    product=1
print(products)'''

'''a=[2,3,4,5,6,8,9,12]
b=len(a)
k=4
maxavg=0
for i in range(b-k+1):
    d=sum(a[i:i+k])/k
    if d>maxavg:
        maxavg=d
print(maxavg)'''

