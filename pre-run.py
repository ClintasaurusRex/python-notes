
lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
new_lst = []
for item in lst1:
  if item not in lst2:
    new_lst.append(item)
print(new_lst)



# numbers = input().split()
# # Write your code below
# reverse_lst = numbers[::-1]
# first = numbers[:1]
# last = numbers[-1:]
# new_lst = first + numbers + reverse_lst + last
# repeat = new_lst * 2
# print(repeat)




