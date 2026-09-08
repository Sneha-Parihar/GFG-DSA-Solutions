class Solution:
    def longest(self, arr):
        # code here
        max=-1
        ans=''
        for word in arr:
            if(len(word)>max):
                max=len(word)
                ans=word
            
        return ans
