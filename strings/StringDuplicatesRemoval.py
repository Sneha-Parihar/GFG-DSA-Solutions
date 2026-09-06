class Solution:
    def reverseWords(self, s):
        # code here
        words=s.split('.')
        words=[word for word in words if word]
        return ".".join(words[::-1])
