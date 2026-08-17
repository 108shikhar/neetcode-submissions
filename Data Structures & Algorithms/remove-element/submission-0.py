class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = nums
        nums.sort()
        for i in nums[:]:
            if i == val:
                a.remove(i)
        return len(a)