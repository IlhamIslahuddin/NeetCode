class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            substring = ""
            if len(s) - i < longest:
                break
            else:
                for j in range(i, len(s)):
                    if s[j] in substring:
                        break
                    else:
                        substring += s[j]
            if len(substring) > longest:
                longest = len(substring)
        return longest
