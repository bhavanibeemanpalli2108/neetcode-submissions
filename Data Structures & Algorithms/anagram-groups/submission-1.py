class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage=defaultdict(list)
        for ele in strs:
            key="".join(sorted(ele))
            storage[key].append(ele)
        return list(storage.values())