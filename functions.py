def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)

    return False


list1 = [1, 2, 3, 4, 5]
print(list1)
target1 = 9
result1 = has_pair_with_sum(list1, target1)
print(result1)

list2 = [2, 4, 6, 8, 10]
print(list2)
target2 = 15
result2 = has_pair_with_sum(list2, target2)
print(result2)
