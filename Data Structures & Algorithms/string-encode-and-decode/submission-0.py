class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i;
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        j = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            substring = s[j+1:j+1+length]
            strs.append(substring)
            i = j+1+length
        return strs;
