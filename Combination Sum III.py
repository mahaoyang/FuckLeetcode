# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字
import copy

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        tmp = [0] * k
        lst = [i for i in range(1, n + 1)]

        def next_num(s=0, tidx=0):
            if tidx == k:
                if sum(tmp) == n:
                    result.append(copy.deepcopy(tmp))
                return
            for idx in range(s, n):
                tmp[tidx] = lst[idx]
                next_num(idx + 1, tidx + 1)

        next_num()
        return result

d = Solution().combinationSum3(3, 7)
print(d)
