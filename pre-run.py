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
