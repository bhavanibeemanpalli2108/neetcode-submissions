class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        result=set()
        i=0
        while i<n-2:
            left=i+1
            right=n-1
            while left<right:
                add=nums[i]+nums[left]+nums[right]
                if add==0:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif add<0:
                    left+=1
                else:
                    right-=1
                
            i+=1

        return [list(triplet) for triplet in result]