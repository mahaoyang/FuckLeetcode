a = [2, 3, 4, 5]
b = [1, 2, 3, 4, 6, 7, 8]

# from itertools import combinations

import copy  # 实现list的深复制


#  输出原顺序不变的组合
def combinations(lst, plen):
    result = []
    tmp = [0] * plen
    length = len(lst)

    def next_num(s=0, tidx=0):
        if tidx == plen:
            result.append(copy.copy(tuple(tmp)))
            return
        for idx in range(s, length):
            tmp[tidx] = lst[idx]
            next_num(idx + 1, tidx + 1)

    next_num()
    return result


#  把组合变成集合，做交集。由长序列集合依次向短序列集合扫描，迭代到第一个交集非空交集即为最长子序列
def lcs(l1, l2, n):
    if len(l1) > len(l2):
        return lcs(l2, l1, len(l2))
    a_s = combinations(a, n)
    a_s = set(a_s)
    b_s = combinations(b, n)
    b_s = set(b_s)
    ab_s = a_s & b_s
    if ab_s:
        return n
    n -= 1
    if n:
        return lcs(l1, l2, n)
    else:
        return 0


print(lcs(a, b, len(a)))

# plen = 1
#
#
# def next_num(tidx=0, s=0):
#     if tidx == plen:
#         return
#     for idx in range(s, 2):
#         next_num(tidx + 1, idx + 1)
#
#
# next_num()
