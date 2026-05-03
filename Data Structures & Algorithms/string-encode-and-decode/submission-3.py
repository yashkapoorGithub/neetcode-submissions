class Solution:
    def encode(self, strs: List[str]) -> str:
        encoder = ""
        for i in strs:
            encoder += str(len(i)) + "#" + i
        return encoder
    def decode(self, s: str) -> List[str]:
        decoder = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j += 1
            length = int(s[i:j])
            decoder.append(s[j+1: j+length+1])
            i = j+length+1
        return decoder