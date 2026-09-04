class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        list = []

        greatestcount = 1

        if not nums:
            return 0

        for i in nums:
            if i-1 not in hashset:
                list.append(i)
        for i in list:
            print(i)
            count = 1
            while i+1 in hashset:
                i = i+1
                count = count + 1
                if count > greatestcount:
                    greatestcount = count
        

        return greatestcount