class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        if n == 1:
            return True
        while n != 1 and n not in seen:
            seen.append(n)
            temp = 0
            for i in range (len(str(n))):
                temp += (int(str(n)[i])) ** 2
            n = temp
            if n == 1:
                return True
        return False
