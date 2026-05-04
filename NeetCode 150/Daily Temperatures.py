class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        for i in range (len(temperatures)):
            counter = 0
            for j in range (i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = counter
                    break
                else:
                    counter += 1
        return result
