class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right]
                if sum + nums[i] > 0:
                    right = right -1
                elif sum + nums[i] <0:
                    left = left +1
                else:
                    results.append([nums[i],nums[left],nums[right]])
                    left = left + 1

                    right = right -1
                    while left > 0 and left <len(nums)-1 and nums[left] == nums[left-1]:
                        left = left + 1
                    while  right < len(nums)-2 and nums[right] == nums[right+1]:
                        right= right-1
                
        return results