class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        k = 0
        for i in range(0,n):
            if nums[i] != nums[i-1] or k==0:
                nums[k] = nums[i]
                k = k+1
        return k

        