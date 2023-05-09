class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # v2

        # print(nums)
        #
        # p1 = 1
        # p2 = 1
        #
        # while p1 < len(nums):
        #
        #     if nums[p1 - 1] == nums[p1]:
        #         p1 += 1
        #
        #     else:
        #         nums[p2] = nums[p1]
        #         p1 += 1
        #         p2 += 1
        #
        # return p2

        # v3

        print(id(nums))

        i = 0
        while i < len(nums):

            if nums[i] in nums[i + 1:]:
                nums.remove(i)
            else:
                i += 1
        return i




nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(0, nums))