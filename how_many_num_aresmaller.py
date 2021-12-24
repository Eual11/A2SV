class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         list1=[]
         for n in nums:
            list1.append(sorted(nums).index(n))
         return list1
                
