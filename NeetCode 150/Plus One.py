class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        digits[index] += 1
        while digits[index] == 10:
            digits[index] = 0
            if index == 0:
                digits.insert(0,1)
            else:
                digits[index-1] += 1
                index -= 1
        return digits
