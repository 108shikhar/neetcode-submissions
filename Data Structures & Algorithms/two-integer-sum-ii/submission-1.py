class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            add=numbers[l]+numbers[r]
            if add>target:
                r=r-1
            elif add<target:
                l=l+1
            elif add==target:
                return [l+1,r+1]