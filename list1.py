list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

def remove_item(lst, item):
    return [x for x in lst if x != item]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
removing_character = 3
new_list = remove_item(my_list, removing_character)
print(new_list)

# tuple
#reversing the tuple
tup=(1,2,3,4,5,6)
tup2=tup[::-1]
print(tup2)

tup=(1,2,3,4)
num=tup[0]
print(num)
#swaping two tuples 
tup1=(1,2,3)
tup2=(4,5,6)
tup1,tup2=tup2,tup1
print(tup1)
print(tup2)
#Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
num=tuple1[3:-1]
print(num)
    