class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        while i<len(nums)-1:
            k=nums[i] + nums[i+1]
            if k== target:
                return [i,i+1]
            i +=1
