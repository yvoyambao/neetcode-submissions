class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        amount = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                amount += 1
        return amount
        