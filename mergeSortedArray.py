class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Do not return anything, modify nums1 in-place instead.
            """
        size2=len(nums2)
        size1=len(nums1)
        
        for i in range(size2):
            nums1[m]=nums2[i]
            m=m+1
        nums1.sort()
