from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = count = 0
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                count += 1

        return list(range(less, less + count))
