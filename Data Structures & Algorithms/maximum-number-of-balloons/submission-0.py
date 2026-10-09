class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counter = {}
        for c in text:
            if c in "balloon":
                balloon_counter[c] = balloon_counter.get(c,0) + 1
            
        b = balloon_counter.get('b',0)
        a = balloon_counter.get('a', 0)
        l = balloon_counter.get('l', 0) // 2
        o = balloon_counter.get('o', 0) // 2
        n = balloon_counter.get('n', 0)

        return min(b,a,l,o,n)
        

            
        

        
        
