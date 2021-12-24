class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counter=nums.count(target)
        list1=[]
        if counter>=1:
            cnst=sorted(nums).index(target)
            for i in range(counter):
                cnst+=i
                list1.append(cnst)
                cnst=sorted(nums).index(target)
            list1=sorted(list1)
            return list1
        else :
                return list1
        
        
