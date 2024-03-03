

"""
list1=[]
range1=int(input("how many index of list do younwant to create"))
for i in range(range1):
    list2=int(input("enter numbers for list2"))
    list1.append(list2)
print(list1)
list1.reverse()
print(list1)

# concatentation of two list
list1=[]
list2=[]
range1=int(input("enter how many index of list do you want to create for both the list"))
for i in range(range1):
    list3=int(input("enter  number for list "))
    list1.append(list3)
for i in range(range1):
    list4=int(input("enter numbers for list"))
    list2.append(list4)
print(list1)
print(list2)
list5=[i+j for i,j in zip(list1,list2)]
print(list5)


# converting every numbers in list into square
list1 = []
range1 = int(input("How many indices of list do you want to create? "))
for i in range(range1):
    num = int(input("Enter numbers for list1: "))
    list1.append(num)
print("List 1:", list1)

# Square each element of list1 and store the result in list1
for i in range(range1):
    list1[i] = list1[i] ** 2

print("Squared List 1:", list1)
#concatenate of string 
list1=[]
for i in range(3):
    list2=input("enter string ")
    list1.append(list2)
list2=[]

for i in range(3):
    list3=input("enter string ")
    list2.append(list3)

print(list1)
print(list2)
list5=[]
for i in  range(3):
    combined_string=list1[i]+list2[i]
    list5.append(combined_string)
print(list5)"""



list1=[]
for i in range(3):
    list2=input("enter string ")
    list1.append(list2)
list2=[]

for i in range(3):
    list3=input("enter string ")
    list2.append(list3)

list2.reverse()

for i in range(3):
    print("\n",list1[i])
    print("\n",list2[i])
    

