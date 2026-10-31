class Solution:
    def validPalindrome(self, s: str) -> bool:
        res=0
        l,r=0,len(s)-1
        while l<r:
            if s[l].lower()!=s[r].lower():
                left,right=s[l+1:r+1],s[l:r]
                if left==left[::-1] or right==right[::-1]:
                    return True
                else:
                    return False
            l,r=l+1,r-1
        return True