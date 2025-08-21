class Solution(object):
    def majorityElement(self, nums):
        count = {}
        res = majority = 0
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > majority:
                res = i
                majority = count[i]
        return res
        


        