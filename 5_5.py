src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
nums = set()
for i in src:
    if i not in nums:
        unique.add(i)
    else:
        unique.discard(i)
    nums.add(i)
unique_sorted = [i for i in src if i in unique]
print(unique_sorted)
