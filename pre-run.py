
numbers = input()
prefix = input()

nums = numbers.split()
prefixed_nums = [prefix + num for num in nums]
result = ' '.join(prefixed_nums)
print(result)

# Write a program that takes two inputs: a text string and a delimiter character. The program should split the text by whitespace into words, then join these words using the specified delimited character and print the resulting string.

# text = input()
# delimiter = input()
# # Write your code below

# words = text.split()
# result = delimiter.join(words)

# print(result)






# Write a program that receives a list of words as input (given), and prints a list of the indices of the words that are either longer than 3 characters or start with the letter 'a' (case-sensitive).

# To check if a string starts with some substring use: str.startswith("substring")
# cat apple dog elephant ant bird

# lst = input().split()
# indices = []
# for index, word in enumerate(lst):
#   if len(word) > 3 or word.lower().startswith("a"):
#     indices.append(index)
    
# print(indices)