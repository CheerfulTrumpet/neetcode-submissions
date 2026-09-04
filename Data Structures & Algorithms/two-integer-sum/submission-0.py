class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict = {};

        i = 0;

        for i in range(len(nums)):
            difference = target - nums[i];
            if difference in newdict:
                return [newdict[difference], i];
            else:
                newdict[nums[i]] = i;
