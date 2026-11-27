class Solution:
    def isValid(self, s: str) -> bool:
        string=[]
        paran={']':'[','}':'{',')':'('}
        for i in s:
            if i in paran.values():
                string.append(i)
            elif i in paran:
                if not string or string.pop()!=paran[i]:
                    return False
        return len(string)==0
                
