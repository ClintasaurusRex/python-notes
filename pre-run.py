lst = list(map(int, input().split(",")))
# Write your code below
indices = []
for index, num in enumerate(lst):
    if num < 50 or num % 5 == 0:
        indices.append(index)
print(indices)



# 2,4,6,8,10





# lst = input().split(",")
# # Write your code below
# longer_then_5 = []
# for char in lst:
#     if len(char) > 5:
#         longer_then_5.append(char)
#     else:
#         continue
# print(longer_then_5)

# penguin,elephant,koala,tiger,dolphin,giraffe,kangaroo,zebra,lion,panda