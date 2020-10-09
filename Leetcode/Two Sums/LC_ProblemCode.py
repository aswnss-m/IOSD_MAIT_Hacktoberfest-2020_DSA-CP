class Solution(object):
    def twoSum(self,nums,target):
        pos = list()
        for i in range(len(nums)):
            for x in range(i,len(nums)):
                if nums[i]+nums[x] == target and i != x:
                pos.append(i)
                pos.append(x)
        return pos
