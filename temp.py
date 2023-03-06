
def pivotIndex(nums):
    for i in range(len(nums)):


        temp_sum = 0
        # for l in range(len(nums[:i])):
        #     sum_left += nums[:i][l]

        sum_right = 0
        for r in range(len(nums[i + 1 :])):
            sum_right += nums[i + 1 :][r]

        print(sum_right)

        if sum_right == temp_sum:
            return i

        else:
            temp_sum = sum_right


    return -1


nums = [1,7,3,6,5,6]

print(pivotIndex(nums))