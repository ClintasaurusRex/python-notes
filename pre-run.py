


def change_element(list1, index, list2):
    # Write your code below
    modified_list1 = list1.copy()
    modified_list2 = list2.copy()

    modified_list1[index] = modified_list2[0]
    return modified_list1

change_element([1, 2, 3], 1, [5, 6, 7])