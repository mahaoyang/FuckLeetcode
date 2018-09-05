class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = enumerate(nums)
        for i, e in dic:
            sub = target - e
            if sub in nums:
                idx = nums.index(sub)
                if idx != i:
                    return [i, idx]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = enumerate(nums)
        for i, e in d:
            sub = target - e
            try:
                idx = nums.index(sub)
                if idx != i:
                    return [i, idx]
            except:
                pass
