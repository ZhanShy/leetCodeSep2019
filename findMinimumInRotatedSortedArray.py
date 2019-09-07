class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = nums[0]
        size=len(nums)
        for i in range(size):
            if nums[i]<minn:
                minn=nums[i]
        return minn
