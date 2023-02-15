# this is a calculator project
number1=eval(input("Enter number "))
number2=eval(input("Enter number "))
operator=input("Enter operator ")
# for addition
def add(num1,num2):
    result=num1+num2
    print (result)

# for subtraction
def subtract(num1,num2):
    result=num1-num2
    print (result)

# for division     
def divide(num1,num2):
    result=num1/num2
    print (result)

#for multiplication
def multiply(num1,num2):
    result=num1*num2
    print (result)

if operator =="+":
    add (number1,number2)
elif operator=="-":
        subtract(number1,number2)
elif operator=="/":
    divide(number1,number2)
elif operator=="*" or operator=="x" or operator=="X":
    multiply(number1,number2)    

else:
    print("invalid ")                