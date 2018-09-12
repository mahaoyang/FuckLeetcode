class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        t = str.split(' ')
        a = map(pattern.find, pattern)
        b = map(t.index, t)
        a = list(a)
        b = list(b)
        return list(map(pattern.find, pattern)) == list(map(t.index, t))


a = Solution().wordPattern(pattern="abba", str="dog cat cat dog")
print(a)

a = 'aabb'
b = a.find(a)
print(b)
