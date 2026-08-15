class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = s.lower()
        t = t.lower()

        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True