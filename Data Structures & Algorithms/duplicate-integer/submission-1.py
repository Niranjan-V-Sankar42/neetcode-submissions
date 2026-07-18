class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         n = len(nums)
         seen = {}
         for i in range(n):
            if nums[i] in seen:  
                    return True
            else:
                    seen[nums[i]] = 1
         return False       