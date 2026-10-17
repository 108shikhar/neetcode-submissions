class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sorting(nums):
            if len(nums) <= 1:
                return nums
            l=len(nums)//2
            a,b=nums[:l],nums[l:]
            a=sorting(a)
            b=sorting(b)
            m,n=len(a),len(b)
            i,j,ans=0,0,[]            
            while i<m and j<n:
                if a[i]<=b[j]:
                    ans.append(a[i])
                    i=i+1
                elif a[i]>b[j]:
                    ans.append(b[j])
                    j=j+1
            while i<m:
                ans.append(a[i])
                i=i+1
            while j<n:
                ans.append(b[j])
                j=j+1
            return ans
        return sorting(nums)