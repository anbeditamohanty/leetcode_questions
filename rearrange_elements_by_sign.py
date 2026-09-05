nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
#Brute force 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[i for i in nums if i>0]
        neg=[i for i in nums if i<0]
        for i in range(0,len(neg)):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
        return nums


#similar to merge alternative strings and both if are true which helps in alternative merge
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[i for i in nums if i>0]
        neg=[i for i in nums if i<0]
        merged=[]
        for i in range(max(len(pos),len(neg))):
            if i<len(pos):
                merged.append(pos[i])
            if i<len(neg):
                merged.append(neg[i])
        return merged

#optimized
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        pos,neg=0,1
        for i in range(0,len(nums)):
            if nums[i]>=0:
                result[pos]=nums[i]
                pos+=2
            else:
                result[neg]=nums[i]
                neg+=2
        return result
