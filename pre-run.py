# ----------------------------------Challenge 1-----------------------------------------
print("\n----------------------------Challenge 1-------------------------------------\n")

# Creates a set called numbers Contains values 1-5
# Creates a set called fruits containing "apple", 'banana', 'cherry'
# prints both sets

numbers = {1,2,3,4,5}
fruits = {"apple", "banana", "cherry"}
print(numbers, fruits)

print("\n------------------------------Challenge 2----------------------------------\n")
# create function called manage set
# takes 3 args - set1, element to add and element to remove
my_set = {1,2,3,4}
def manage_set(set1, element_to_add, element_to_remove):
  set1.add(element_to_add)
  set1.remove(element_to_remove) if element_to_remove in set1 else None
  return "5 is in the set" if int(5) in set1 else "5 is not in the set"

manage_set(my_set, 7, 7)
my_list = [1,2,3,4,5]
def manage_list(list1, element_to_append, index_to_remove):
  list1.append(element_to_append)
  list1.pop(index_to_remove) if index_to_remove in list1 else None
  if len(list1) > 3:
    return "The list has more than 3 elements"
  else:
    return "The list has 3 or fewer elements"


print(manage_list(my_list,6,8))
print("\n------------------------------Challenge 3----------------------------------\n")
# -------------------------------------Set methods--------------------------------------
# discard(element): Removes the specified element from the set if it exists. 
# Does not raise an error if the element is not found.
my_set = {1, 2, 3}
my_set.discard(3)    # Removes 3 from the set
my_set.discard(4)    # No error, even though 4 is not in the set

# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

my_set = {1, 2, 3}
element = my_set.pop()  # Removes and returns an arbitrary element
my_set = {1, 2, 3}

# clear(): Removes all elements from the set, making it empty.
my_set.clear()       # Removes all elements
# Output: set()


numbers = {10,20,30,40,50}
numbers.discard(35)
print(numbers)
popped_element = numbers.pop()
print(popped_element)
numbers.clear()
print(numbers)

print("\n------------------------------------Challenge 4---------------------------------")
numbers = [1, 2, 2, 3, 4, 4, 5]
def remove_duplicates(numbers):
    # Write code here
    return list(set(numbers))

    

print(remove_duplicates(numbers))