class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dict = {}
        for l in s:
            if l in dict:
                dict[l] += 1
            else:
                dict[l] = 1
        for l in t:
            if l in dict:
                dict[l] -= 1
            else:
                return False
        for val in dict.values():
            if val != 0:
                return False
        return True