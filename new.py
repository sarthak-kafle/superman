
"""# if elif else condition.
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
    print("numner is odd")"""


number=int(print("how many number do you want to check "))
num=[]
for i in  range(0,number):

    number1=int(input("enter numbers"))
    num.append(number1)
gratest=list[0]
for number in num:
    if number1>gratest:
        gratest=number1

print("gtarestnumber is ",gratest)

    





