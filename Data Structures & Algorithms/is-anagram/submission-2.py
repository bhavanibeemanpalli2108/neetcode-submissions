class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}
        for i in s:
            freqs[i]=freqs.get(i,0)+1
        for i in t:
            freqt[i]=freqt.get(i,0)+1
        return freqs==freqt