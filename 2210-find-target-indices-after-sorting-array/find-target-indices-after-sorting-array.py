from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = 0
        count = 0
        arr = []

        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                count += 1

        for i in range(less, less + count):
            arr.append(i)

        return arr
