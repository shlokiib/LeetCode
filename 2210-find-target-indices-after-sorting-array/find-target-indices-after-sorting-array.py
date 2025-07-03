from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # First pass: count how many elements are less than target
        less = 0
        for num in nums:
            if num < target:
                less += 1
        
        # Second pass: count how many are equal to target and yield indices
        result = []
        for num in nums:
            if num == target:
                result.append(less)
                less += 1  # index increases for each target occurrence
                
        return result
