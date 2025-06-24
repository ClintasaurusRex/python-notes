


# Create a program that receives a list as input and prints four new lists based on the following slicing operations:

# A list containing every fourth element, starting from index 2
# A list containing all elements from the 3rd element to the 3rd to last element
# A list containing every element in reverse order, skipping every other element
# A list containing the first three and last three elements of the original list
# Name the lists list1, list2, list3 and list4 - accordingly.


original_list = input().split(',')
# Write your code below
list1 = original_list[2::4]
list2 = original_list[2:-2]
list3 = original_list[::-2]
list4 = original_list[:3] + original_list[-3:]

# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)



# Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:

# A list containing every third element, starting from index 1 (the second element)
# A list containing all the elements from the 6th element to the 1st in reverse order
# A list containing every second element starting from the middle of the list to the end
lst = input().split(",")
lst1 = lst[1::3]
print(lst1)

lst2 = lst[6::-1]
print(lst2)

middle = len(lst) // 2
lst3 = lst[middle::2]
print(lst3)



# Create a program that takes a list and prints:

# For lists with 5 or more items: the first two and last two items
# For lists with less than 5 items: the first and last item only

input_list = input().split(', ')
# Write your code below
if len(input_list) > 5:
  result = input_list[:2] + input_list[-2:]
  print(result)
elif len(input_list) < 5:
    result = input_list[:1] + input_list[-1:]
    print(result)
   


# input_list = input().split(', ')
# # Write your code below
# if len(input_list) > 5:
#   lst1 = input_list[-1:1]
#   print(lst1)


# lst = input().split(",") # 1,2,3,4,5,6,7,8,9,10
lst_len = len(lst)
if lst_len % 2 == 0:
  mid = lst_len // 2
  result = lst[mid-1:mid+1]
  print(result)
else:
  mid = lst_len // 2
  result = lst[mid-1:mid+2]
  print(result)

# # cat,dog,bird,fish,hamster,snake,rabbit,turtle,mouse




  





