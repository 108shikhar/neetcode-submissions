class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d,i={},1
        for j in order:
            d[j]=i
            i=i+1
        for m in range(len(words)-1):
            w1,w2=words[m],words[m+1]
            for n in range(len(w1)):
                if n==len(w2):
                    return False
                elif w1[n]!=w2[n] and d[w1[n]]>d[w2[n]]:
                    return False
                elif w1[n]!=w2[n] and d[w1[n]]<d[w2[n]]:
                    break
        return True