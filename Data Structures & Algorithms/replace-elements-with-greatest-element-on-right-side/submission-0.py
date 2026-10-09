class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr) -1 , -1, -1):
            current_val = arr[i]

            arr[i] = max

            if current_val > arr[i]:
                max = current_val
        
        return arr

            
        