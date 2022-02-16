def first_duplicate_occarance(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate


print(first_duplicate_occarance([1, 2, 3, 2 ,1]))

