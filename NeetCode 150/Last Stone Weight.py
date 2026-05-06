class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heavy1 = stones.pop(stones.index(max(stones)))
            heavy2 = stones.pop(stones.index(max(stones)))
            if heavy1 != heavy2:
                stones.append(max(heavy1,heavy2) - min(heavy1,heavy2))
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
