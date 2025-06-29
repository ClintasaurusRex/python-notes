# Create a function named find_occurrences that:

# Takes two string arguments: text and pattern
# Counts how many times pattern appears in text, including overlapping occurrences
# Returns a tuple containing:
# A boolean indicating if the pattern was found (True/False)
# The number of occurrences of the pattern
# A list of starting positions where the pattern was found
# For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

# If the pattern is not found, return (False, 0, []).


def find_occurrences(text, pattern):
    # Write your code here
    indices = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:

            indices.append(i)

    if indices:
        return(True, len(indices), indices)
    else:
        return (False, 0, [])

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)



# n = int(input())
# rows = int(n/2)+1
# for i in range(rows):
#   print("*" * (2 * i + 1))