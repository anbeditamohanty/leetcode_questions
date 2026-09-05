# Brute Force  O(N2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float("-inf")  # as the max value could be a negative integer
        for i in range(0, len(nums)):
            total=0
            for j in range(i,len(nums)):
                total=total+nums[j]
                maximum=max(maximum, total)
        return maximum

#Optimal/ Kadane Algorithm
#Reset total to zero when you find sum to be negative 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float("-inf")  # as the max value could be a negative integer
        total=0
        for i in range(0, len(nums)):
            total=total+nums[i]
            maximum=max(maximum, total)
            if total<0:
                total=0
        return maximum
