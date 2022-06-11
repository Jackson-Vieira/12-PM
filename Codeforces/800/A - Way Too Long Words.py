n = int(input())
lst_word = []
for i in range(n):
	w = input()
	lst_word.append(w)
for w in lst_word:
	print(w) if len(w) <= 10 else print(w[0]+str(len(w)-2)+w[-1])