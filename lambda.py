'''
1. Expected output of the following code
'''
data=[10,501,22,37,100,999,87,351]
result=filter(lambda x:x>4, data)
print(list(result))
#**************Expected output is [10, 501, 22, 37, 100, 999, 87, 351]
'''
2. Python code using lambda function to check every element of a list is integer or string
'''
string = "mangalore chennai bangalore 430"
#Printing original data
print(string)
#filtering only strings
alpha = lambda x : x.isalpha()
res=''.join(filter(alpha,string))
print("String:",res)
#filtering only digits
digit=lambda x:x.isdigit()
res=''.join(filter(digit,string))
print("Digits:", res)

'''
3. Creating fibonacci series using lambda function
'''
#using user defined function and passing count as argument
def fibonacci(count):
#initializing the list starting values 
   data = [1,2]
   any(map(lambda _:data.append(sum(data[-2:])), range(2, count)))
   return data[:count]
#passing count value to print fibonacci series till 50 elements
print(fibonacci(50))

'''
4. Validating regular expression for the given data
'''
# a.Validating Email address
import re
emailid="k$3@gmail.com"
req="^[a-z0-9.]{5,10}+@[a-z]{3,5}+.+[a-z]{2,6}$"
res=re.search(req,emailid)
if res:
    print ("Valid email address")
else:
    print ("Invalid email address")

#b. Validating mobile number of bangladesh
mobile="01948564565"
req="^[0-1]{1,2}+[0-9]{9}$"
res=re.search(req,mobile)
if res:
    print("Valid Bangaladesh Mobile number ")
else:
    print("Invalid Bangaladesh Mobile number")

#c. Validating telephone number of USA
telep="5553434567"
req="^[5]{3}+[0-9]{7}$"
res=re.search(req,telep)
if res:
    print("Valid USA telephone number")
else:
    print("Invalid USA telephone number")

#d. Validating Password which comprises of Uppercase, lowercase, special char, numbers
password="Krukr#4502Erth$5"
req="^[A-Za-z@#$%^&*!~_0-9]{16}$"
res=re.search(req,password)
if res:
    print("Valid password")
else:
    print("Invalid Password")
