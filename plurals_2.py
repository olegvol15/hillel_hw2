list1 = [1, 2, 3, 4, 4, 5]
list2 = [3, 4, 5, 6, 6, 7]

count_common_numbers = len(set(list1) & set(list2))
print(count_common_numbers)