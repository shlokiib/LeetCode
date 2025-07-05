class Solution(object):
    def findLucky(self, arr):
         d=Counter(arr)
         m=0
         for i,j in d.items():
            if i ==j:
                m=max(m,i)
         if m != 0:
            return m 
         else: 
            return -1
        
