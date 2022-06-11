def solution(s1, s2):

	s1_letters = list(set([l for l in s1]))
	size = len(s1_letters)
	total = 0
	
	for letter in s1_letters:
		if letter in s2:
			c1 = s1.count(letter)
			c2 = s2.count(letter) 
			total += min(c1,c2)
		
	return total