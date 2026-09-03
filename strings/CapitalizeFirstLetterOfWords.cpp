class Solution:
    def convert(self, s: str) -> str:
        # code here
        words=s.split()
        return " ".join(word[0].upper()+word[1:] if word else "" for word in words)
