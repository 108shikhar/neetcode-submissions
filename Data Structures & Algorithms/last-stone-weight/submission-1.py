class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr=sorted(stones)
        i=len(arr)-1
        while i>0:
            val=abs(arr[i]-arr[i-1])
            arr.pop(i)
            arr.pop(i-1)
            arr.append(val)
            arr.sort()
            i=len(arr)-1
        if len(arr)>0:
            return arr[0]
        else:
            return 0