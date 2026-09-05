# Brute force solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=0
        for i in range(0,len(nums)):
            num=nums[i]
            count=1
            while nums[i]+1 in nums[i+1:]:
                count+=1
                num=num+1
            maximum=max(maximum, count)
        return maximum

# Optimal soln: sorting and checking for duplicates
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        smallest=float("-inf")
        longest_seq=0
        for i in range(0,len(nums)):
            num=nums[i]
            if num-1==smallest:
                count+=1
                smallest=num
            elif num!=smallest:
                count=1
                smallest=num
            longest_seq=max(longest_seq,count)
        return longest_seq   

# Best soln using sets
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set()
        for i in range(0, len(nums)):
            set1.add(nums[i])
        longest=0
        count=0
        for num in set1:
            if num-1 not in set1:
                x=num
                count=1
                while x+1 in set1:
                    count+=1
                    x+=1  
                longest=max(longest,count)
        return longest   
