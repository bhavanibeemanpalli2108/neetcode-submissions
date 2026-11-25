class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_long=1
        curr_max=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            if nums[i+1]-nums[i]==1:
                curr_max+=1
                max_long=max(max_long,curr_max)
            else:
                curr_max=1
            
        return max_long