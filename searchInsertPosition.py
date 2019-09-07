class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size=len(nums)
        check=0
        for i in range(size):
            if nums[i]==target:
                check=check+1
                return i
            elif nums[i]>target:
                check=check+1
                return i
        if check==0:
            return size
        
        return 0
