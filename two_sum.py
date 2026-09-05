# Brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):  # to eliminate the error for i+1 for next iteration of j
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j

# Optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,v in enumerate(nums):
           complement = target - v
           if complement not in seen:
            seen[v]=i
           else:
            return seen[complement],i
