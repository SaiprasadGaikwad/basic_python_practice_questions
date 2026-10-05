#1. print hello world

print("hello world ")


2. write a program to check number is even or odd

num=int(input("enter your number :"))
if num % 2== 0 :
    print("number is even")
else:
    print("number is odd")


# 3. write a program to check age is valied for voting or not 

age=int(input("enter your age : "))

if age >= 18 :
    print("person should eligible for voting")
else:
    print ("under the 18 or not valid for voting")  

# 4. write a program to find the word1 and word2 is anagram

word1=input("enter first word :")
word2=input("enter second word :")

if sorted (word1 )==sorted (word2 ):
    print("the word are anagram ")
else :
    print("the word are not anagram ")

# 5. creat 2 variable cost_price and seling_price and calculate the profit and loss

cost_price = 500
selling_price = 600

if selling_price > cost_price :
    profit=selling_price - cost_price 
    print("profit = ",profit )

elif cost_price> selling_price:
    loss = cost_price - selling_price 
    print("loss = " ,loss)

else :
    print("no profit , and loss ") 
    