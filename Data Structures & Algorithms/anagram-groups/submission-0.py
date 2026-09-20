from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for word in strs:
            sorted_letters="".join(sorted(word))
            anagrams[sorted_letters].append(word)
        return list(anagrams.values())