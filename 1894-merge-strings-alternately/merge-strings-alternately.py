class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
         merged = ""
         i = 0
         j = 0

        # Loop through both strings
         while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged += word1[i]
                i += 1
            if j < len(word2):
                merged += word2[j]
                j += 1

         return merged