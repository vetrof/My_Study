
def runningSum(nums):

    for i in range(len(nums)):
        if i > 0:
            nums[i] = nums[i] + nums[i - 1]
            
    return nums
        








nums = [1,2,3,4]
print(runningSum(nums))