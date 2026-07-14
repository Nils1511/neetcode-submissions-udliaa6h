class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            res[tuple(counts)].append(st)
        
        return list(res.values())