# -----------------------Advanced Data Aggregation


# ---------------------------Challenge One-------------------------------
print("\n ---------------------------Challenge One-------------------------------")
sales = [100,200,150,300]
starting_cash = 50

print(sum(sales, starting_cash))

# ----------------------------Challenge Two ---------------------------------
print("\n----------------------------Challenge Two ---------------------------------")
def calculate_average_score(scores):
    if not scores:
        return 0
    average = sum(scores) / len(scores)
    return average
print(calculate_average_score([95,85,76,89,100,92,67]))

# -------------------------- Challenge Three -------------------------------
print("\n-------------------------- Challenge Three -------------------------------")
numbers = [42, 17, 23, 56, 9, 34]
words = ["kiwi", "apple", "banana", "cherry", "date"]
print(f"Smallest number: {min(numbers)}")
print(f"Largest number: {max(numbers)}")
print(f"Smallest word: {min(words)}")
print(f"Largest word: {max(words)}")


# -------------------------- Challenge Four -------------------------------
print("\n-------------------------- Challenge Four -------------------------------")
temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

print(f"Highest temperature: {max(temperatures)}°F")
print(f"Lowest temperature: {min(temperatures)}°F")
print((f"Highest humidity: {max(humidity)}%"))
print(f"Lowest humidity: {min(humidity)}%")

# -------------------------- Challenge Five -------------------------------
print("\n-------------------------- Challenge Five -------------------------------")

# Starter inputs
numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

# Task 1: Sort numbers in ascending order
# Task 2: Sort numbers in descending order
# Task 3: Sort words alphabetically
# Task 4: Sort words by length

# Replace 'pass' with your code for each task
ascending_numbers = sorted(numbers)
descending_numbers = sorted(numbers, reverse=True)
alphabetical_words = sorted(words)
length_sorted_words = sorted(words, key=len)

# Print the results
print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)

# -------------------------- Challenge Six -------------------------------
print("\n-------------------------- Challenge Six -------------------------------")

def analyze_grades(grades):
    # Write code here
    average = sum(grades.values()) / len(grades)
    highest = max(grades.values())
    lowest = min(grades.values())
    top_student = max(grades, key=grades.get)
    bottom_student = min(grades, key=grades.get)
    
    summary = {
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'top_student': top_student,
        'bottom_student': bottom_student
    }
    return summary

# Test the function
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
result = analyze_grades(student_grades)
print(result)

"""
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88}
print("TESTING")
average = sum(student_grades.values()) / len(student_grades)
print(average)
highest_grade = max(student_grades.values())
print(highest_grade)
lowest_grade = min(student_grades.values()) 
print(lowest_grade)
top_student = max(student_grades, key=student_grades.get)
print(top_student)
bottom_student = min(student_grades, key=student_grades.get)
print(bottom_student)
"""

# -------------------------- Challenge Seven -------------------------------
print("\n-------------------------- Challenge Seven -------------------------------")
data = {'a': 3, 'b': 1, 'c': 2}

def dictionary_sorter(data_dict):
  sorted_data = dict(sorted(data_dict.items(), key=lambda x: x[1]))
  return sorted_data    
    
dictionary_sorter(data)

    

# -----------------------------Advanced Data Aggregation