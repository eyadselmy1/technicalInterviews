class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        k = 0
        for i in range(0,n):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k+1
        return k
