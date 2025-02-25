# @file    HW6.py
# @author  Brayden Davis
# @date    February 23rd 2025
# @brief   This is for homework six.

#This is to ask what the first input is.
num1 = input("What is the first number? ")

#This is to ask what the second input is.
num2 = input("What is the second number? ")
print(num1 , num2)
#Check to see if num2 = 0
while int(num2) == 0:
  print("You cannot pick zero for the second number ")
  num2 = input("What is the second number? ")

#This is how it finds the sum.
sum = int(num1) + int(num2)

#This is how it prints the sum.
print("The sum is...")
print(sum)

#This is how it finds the difference. It puts the greater number first.
if int(num1) > int(num2):
  print("the difference is...")
  difference = int(num1) - int(num2)
else:
  difference = int(num2) - int(num1)
  print("The difference is...")

#This is how it prints the difference.
print(difference)

#This is how it finds the product.
product = int(num1) * int(num2)

#This is how it prints the product.
print("The product is...")
print(product)

#This is how it finds the quotient.
quotient = int(num1) / int(num2)

#This is how it prints the quotient.
print("The quotient is...")
print(quotient)
