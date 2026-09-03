class Solution:
	def firstAlphabet(self, s):
		# code here
	    words=s.split()
		return "".join(word[0] for word in words)
