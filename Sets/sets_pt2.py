print("\n----------------------------Challenge 1-------------------------------------\n")
def set_operations(set1, set2):
    # Calculate the union
    union_result = set1 | set2

    # Calculate the intersection
    intersection_result = set1 & set2

    # Calculate the difference
    difference_result = set1 - set2

    # Calculate the symmetric difference
    symmetric_difference_result = set1 ^ set2

    # Return a dictionary containing the results
    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }
    
print("\n----------------------------Challenge 2-------------------------------------\n")
group1 = {"Alice", "Bob", "Charlie", "Diana"}
group2 = {"Bob", "Charlie", "Eve"}
group3 = {"Charlie", "Frank", "Bob"}

intersection_result = group1.intersection(group2, group3)
difference_result = group1.difference(group2, group3)

print("Members in all groups:", sorted(list(intersection_result)))
print("Unique members in group1:", sorted(list(difference_result)))

print("\n----------------------------Challenge 3-------------------------------------\n")
region1 = {"gold coin", "ruby", "emerald", "pearl"}
region2 = {"ruby", "emerald", "sapphire"}
region3 = {"emerald", "diamond", "sapphire"}

# Write code here
shared_treasures = region1.intersection(region2, region3)
unique_treasures_region1 = region1.difference(region2, region3)
all_treasures = region1.union(region2, region3)
exclusive_treasures = (
    region1.difference(region2.union(region3))
    .union(region2.difference(region1.union(region3)))
    .union(region3.difference(region1.union(region2)))
)

# Print the results
print("Shared treasures:", sorted(list(shared_treasures)))
print("Unique treasures in region1:", sorted(list(unique_treasures_region1)))
print("All treasures:", sorted(list(all_treasures)))
print("Exclusive treasures:", sorted(list(exclusive_treasures)))
print("\n----------------------------Challenge 4-------------------------------------\n")
# ----------------------------------------SUB SETS--------------------------------------

set1 = {1, 2}
set2 = {1, 2, 3}

is_subset = set1.issubset(set2)
is_superset = set2.issuperset(set1)
print(is_subset)
print(is_superset)

P = {1, 2, 3, 4}
Q = {1, 2, 3, 4}

subset = P <= Q
superset = Q > P
print(subset, superset)

def check_sets(set1, set2):
    # Check if set1 is a subset of set2
    is_subset = set1.issubset(set2)

    # Check if set2 is a superset of set1
    is_superset = set2 >= set1

    # Check if set1 is a proper subset of set2
    is_proper_subset = set1 < set2

    # Check if set2 is a proper superset of set1
    is_proper_superset = set2 > set1

    # Return a dictionary containing the results
    return {
        "is_subset": is_subset,
        "is_superset": is_superset,
        "is_proper_subset": is_proper_subset,
        "is_proper_superset": is_proper_superset
    }

print(check_sets({1,2}, {1,2,3,4}))
print(check_sets({1,2,3}, {1,2,3}))
print("\n----------------------------Challenge 5-------------------------------------\n")
# -------------------Iterating over sets--------------------------------------------

def iterate_and_filter_set(input_set):
    # Write code here
    new_set = set()
    for element in input_set:
        if element > 10:
            continue
        new_set.add(element)
    return new_set

# Can also be done like this

# def iterate_and_filter_set(input_set):
#     return {element for element in input_set if element <= 10}

print(iterate_and_filter_set({5,12,7,15,3,10}))

print("\n----------------------------Challenge 5 1/2-------------------------------------\n")
def filter_and_square_set(input_set):
    odd_set = set()
    for el in input_set:
        if el % 2 == 0:
            continue
        odd_set.add(el ** 2)
    return odd_set

# def get_squared_odds(input_set):
    # return {el ** 2 for el in input_set if el % 2 != 0}

print(filter_and_square_set({1,2,3,4,5}))

print("\n----------------------------Challenge 6-------------------------------------\n")

# match1 = {"Alice", "Bob", "Charlie", "Diana"}
# match2 = {"Charlie", "Diana", "Eve", "Frank"}
# match3 = {"Alice", "Diana", "Frank", "George"}

match1 ={"Alice", "Bob"}
match2 = {"Charlie", "Diana"}
match3 = {"Eve", "Frank"}

all_matches = sorted(list(match1 & match2 & match3))

in_1_and_2 = match1 & match2
in_1_and_3 = match1 & match3
in_2_and_3 = match2 & match3

in_two_or_more = in_1_and_2 | in_1_and_3 | in_2_and_3
in_all_three = match1 & match2 & match3
in_exactly_two = in_two_or_more - in_all_three

all_players = match1 | match2 | match3
in_one = all_players.difference(in_two_or_more)

# Count the total number of unique players
count = len(match1.union(match2, match3))

# find players in match 1 only
in_match1 = match1.difference(match2, match3)

sort_all_match = sorted(list(all_matches))
sort_two_matches = sorted(list(in_exactly_two))
sort_one_match = sorted(list(in_one))
sort_only_match1 = sorted(list(in_match1))

print(f"Players in all matches: {sort_all_match}")
print(f"Players in exactly two matches: {sort_two_matches}")
print(f"Players in only one match: {sort_one_match}")
print(f"Players in Match 1 only: {sort_only_match1}")