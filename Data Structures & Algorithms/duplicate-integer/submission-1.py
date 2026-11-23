class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ele=set()
        for i in nums:
            if i not in ele:
                ele.add(i)
            else:
                return True
        return False