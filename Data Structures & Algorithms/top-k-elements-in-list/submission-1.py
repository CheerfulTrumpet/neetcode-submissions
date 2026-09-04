class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict = {};

        i = 0;

        listan = [];

        sorted_array = sorted(nums);

        for i in range(len(sorted_array)):
            if sorted_array[i] not in newdict:
                newdict[sorted_array[i]] = 0;
            newdict[sorted_array[i]] += 1
        
        res = sorted(newdict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            listan.append(res[i][0])

        return listan;
