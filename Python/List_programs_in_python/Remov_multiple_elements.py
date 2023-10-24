# Python program to remove multiple
# elements from a list 

# creating a list
list1 = [11, 5, 17, 18, 23, 50] 

# Iterate each element in list
# and add them in variable total
for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)

# printing modified list
print("New list after removing all even numbers: ", list1)
