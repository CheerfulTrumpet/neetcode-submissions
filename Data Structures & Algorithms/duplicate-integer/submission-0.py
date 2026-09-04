class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_list = set();
        for stuff in nums:
            if stuff in set_list:
                return True;
            else:
                set_list.add(stuff);
        return False;