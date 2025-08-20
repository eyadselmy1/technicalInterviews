class Solution(object):
    def merge(self, nums1, m, nums2, n):
        mindex = m-1
        nindex = n-1
        right = m+n-1

        while nindex >=0:
            if mindex >=0 and nums1[mindex] > nums2[nindex]:
                nums1[right] = nums1[mindex]
                mindex = mindex-1
            else:
                nums1[right] = nums2[nindex]
                nindex = nindex-1
            
            right = right-1

        