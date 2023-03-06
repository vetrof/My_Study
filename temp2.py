def pivotIndex(nums):

    left_summ = 0
    right_sum = sum(nums)

    for i in range(len(nums)):
        right_sum = right_sum - nums[i]

        if right_sum == left_summ:
            return i

        left_summ = left_summ + nums[i]
    return -1



nums = [1, 7, 3, 6, 5, 6]

print(pivotIndex(nums))