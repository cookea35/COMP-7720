''' bw_custom is based off the answers to this (https://stackoverflow.com/questions/21297887/performance-issues-in-burrows-wheeler-in-python) 
	question on stack overflow, this is used for files larger than 300000 bytes. It had to be modified slightly to be used for byte processing instead of str processing'''


def bw_custom(s):
	n = len(s)
	s2 = s*2
	class K:
		def __init__(self, i):
			self.i=i
		def __lt__(a, b):
			i, j = a.i, b.i
			for k in range(n):
				if s2[i+k] < s2[j+k]:
					return True
				elif s2[i+k] < s2[j+k]:
					return False
			return False
	inorder = sorted(range(n), key=K)
	L = [s2[i+n-1] for i in inorder]
	return L


''' bwt_me and make_sa are inspired by: https://github.com/kemaleren/bwt/blob/master/bwt.py modified for byte processing instead of strings

	They utilize a suffix array, this is used for files smaller than 300000 bytes and produce correct output to what we saw in class'''

def make_sa(s):
	suffixes = {s[i:] : i for i in range(len(s))}
	suff = list(suffixes[suffix] for suffix in sorted(suffixes.keys()))
	return suff

def bwt_me(s, sa=None):
	if sa is None:
		sa = make_sa(s)
	L = [s[index-1] for index in sa]
	return L 

