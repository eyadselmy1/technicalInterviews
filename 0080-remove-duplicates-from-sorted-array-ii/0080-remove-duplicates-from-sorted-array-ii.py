class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        k = 2
        for i in range (2, n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k = k+1
        return k
        