class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         answer = [1] * n

        # left will hold the product of all elements to the left of index i
         left = 1
         for i in range(n):
            answer[i] = left
            left *= nums[i]

        # right will hold the product of all elements to the right of index i
         right = 1
         for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

         return answer