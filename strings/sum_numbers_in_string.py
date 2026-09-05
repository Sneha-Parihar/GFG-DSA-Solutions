class Solution:
    def findSum(self, s):
        # code here
        total=0
        num=0
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            else:
                total+=num
                num=0
        total+=num       
        return total
