





print("-----------------------Dictionary Methods----------------------------")

# items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# items = my_dict.items()
# print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}


# -- keys(): Returns a view object that displays a list of all the keys in the dictionary.
# -- values(): Returns a view object that displays a list of all the values in the dictionary.

# Step 2: Access All Keys and Values
# Print all students and grades
print(f"Students: {grades.keys()}")
print(f"Grades: {grades.values()}")

# Output
# Students: dict_keys(['Alice', 'Bob', 'Charlie'])
# Grades: dict_values([85, 90, 78])

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade

# -- get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default is specified).

# Get Bob's grade using get() method
bob = grades.get("Bob")
print(f"Bob's grade: {bob}")
# Bob's grade: 90

# Step 5: Remove a Student
# Remove Charlie using pop() method

# -- pop(key): Removes the element with the specified key and returns its value.

# Print the updated dictionary
popped = grades.pop("Charlie")
print(f"Updated Grades: {grades}")
# Updated Grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}