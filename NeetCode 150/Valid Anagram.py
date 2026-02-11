class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = [char for char in s]
        for char in t:
            if char not in seen:
                return False
            else:
                seen.remove(char)
        return True
