#Basic arithmatic operation in python 

num1=int(input ("enter your number : "))
num2=int(input ("enter your number : "))
arithmaic_operation = input("Choose operation ('+','-','*','/','%'): " )

#Display the numbers 

print("first number :",(num1))
print("second number : ",(num2))
print (arithmaic_operation)

# Perform the arithmatice operation 

if arithmaic_operation == '+' :
    print(num1+num2)
elif arithmaic_operation == '-' :
    print ( num1 - num2 )
elif arithmaic_operation == '*' :
    print (num1*num2)
elif arithmaic_operation == ' / ' :
    print(num1 / num2)
elif arithmaic_operation == '% ' :
    print(num1 % num2)
else:
    print ("invalid operation ")
