class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newdict = {};
        for stuff in s:
            if stuff not in newdict:
                newdict[stuff] = 1;
            else:
                newdict[stuff] = newdict[stuff] + 1;
        
        for stuff in t:
            if stuff in newdict:
                newdict[stuff] = newdict[stuff] - 1;
                if newdict[stuff] == 0:
                    del newdict[stuff];
            else:
                return False;

        if len(newdict) > 0:
            return False;
        else:
            return True;
            