class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = len(candies)
        maxcandi = max(candies)
        arr = []
        if m == 0:
            return ""
        if m == 1:
            return True
        for i in range (m):
            if candies[i]+extraCandies >= maxcandi:
                arr.append(True)
            else:
                arr.append(False)
        return arr