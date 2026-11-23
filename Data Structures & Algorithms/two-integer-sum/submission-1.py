class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in value:
                return [min(i, value[diff]), max(i,value[diff])]
            else:
                value[nums[i]]=i
        return []