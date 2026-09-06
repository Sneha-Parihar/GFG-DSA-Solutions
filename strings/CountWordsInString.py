class Solution:
    def countWords(self, s: str) -> int:
        # code here
        count=0
        for words in s.split():
                count+=1
        return count
