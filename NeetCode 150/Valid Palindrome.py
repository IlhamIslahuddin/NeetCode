class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" ")).lower()
        pointer1 = 0
        pointer2 = len(s) - 1
        symbols = "!.?,':;()*&"
        while pointer1 < pointer2:
            if s[pointer1] in symbols:
                pointer1 += 1
            if s[pointer2] in symbols:
                pointer2 -= 1
            if s[pointer1] != s[pointer2] and pointer1 < pointer2:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True
