class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        
        if l<=1:
            return nums
            
        m=l//2
        a=nums[:m]
        b=nums[m:]

        a=self.sortArray(a)
        b=self.sortArray(b)
        
        i=0
        j=0

        c=[]

        while i<len(a) and j<len(b):
            x=a[i]
            y=b[j]
            if x<=y:
                c.append(x)
                i=i+1
            elif x>y:
                c.append(y)
                j=j+1
        
        while i<len(a):
            x=a[i]
            c.append(x)
            i=i+1
            
        while j<len(b):
            y=b[j]
            c.append(y)
            j=j+1
        
        return c