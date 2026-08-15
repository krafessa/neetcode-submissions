class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCharacters = defaultdict(int)
        for character in s:
            sCharacters[character] += 1
        tCharacters = defaultdict(int)
        for character in t:
            tCharacters[character] += 1
        return sCharacters == tCharacters