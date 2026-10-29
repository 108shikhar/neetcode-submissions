class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,h=0,len(nums)-1
        while l<=h:
            m=(l+h)//2
            if nums[m]==target:
                return True
            if nums[l]==nums[m]==nums[h]:
                l=l+1
                h=h-1
            elif nums[l]<=nums[m]: #Sorted
                if nums[l]<=target<=nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return False