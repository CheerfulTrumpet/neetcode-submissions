class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedList = []

        for i in s:
            if i.isalnum():
                cleanedList.append(i.lower())

        left = 0
        right = len(cleanedList)-1

        while left  <right:
            if cleanedList[left] != cleanedList[right]:
                return False
            else:
                left = left+1
                right = right -1

        return True

