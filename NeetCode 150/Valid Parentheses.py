class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        for i in range (len(s)):
            if s[i] in "({[":
                open_brackets.append(s[i])
            else:
                if len(open_brackets) == 0 or (s[i] == ")" and open_brackets[-1] != "(") or (s[i] == "}" and open_brackets[-1] != "{") or (s[i] == "]" and open_brackets[-1] != "["):
                    return False
                else:
                    open_brackets.pop(-1)

        return len(open_brackets) == 0
