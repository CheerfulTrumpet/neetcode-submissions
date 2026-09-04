class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups =defaultdict(list);

        for stuff in strs:
            counts = [0] * 26;
            for char in stuff:
                counts[ord(char) - ord('a')] += 1;
            key = tuple(counts);
            groups[key].append(stuff);
        return list(groups.values());



