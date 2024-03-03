
# if elif else condition.
num1=int(input("enter a number for num 1"))
num2=int(input("enter a number for num2"))
sum=num1+num2
print(sum)
  
light=input("enter light:")
if(light=="red"):
    print("stop")

elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("redy to stop")

else:
    ("light is broken")

#ternary operator
fruit=input("enter name")
eat="yes" if fruit=="apple" else "no"
print(eat)

sweet=input("enter food")
print("sweet" if sweet=="laddu" or sweet=="jalebi" else "not sweet")


number=int(input("enter the number to check weather number is odd or even"))
if(number%2==0):
    print("number is even")

else:
    print("numner is odd")


number = int(input("How many numbers do you want to check? "))
num = []

for i in range(number):
    number1 = int(input("Enter number: "))
    num.append(number1)

greatest = num[0]

for number in num:
    if number > greatest:
        greatest = number

print("The greatest number is:", greatest)


#checking palindrom list or not 
num=[]
for i in range(0,5):
    num2=input("neter number")
    num.append(num2)
num_copy=num.copy()
num_copy.reverse()
if (num==num_copy):
    print("palindrom list")
else:
    print("not palindrom list")


# tuple count and sort  methos use
num=["a","a","b","c","a"]
print(num.count("a"))
num.sort()
print(num)