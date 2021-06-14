letters_values_dic = {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T' ], 2:['D', 'G'], 3:['B', 'C', 'M', 'P'], 4:['F', 'H', 'V', 'W', 'Y'], 5:['K'], 8:['J', 'X'], 10:['Q', 'Z']}

def score(word):
	word_score=0
	for char in word:
		for value, letter_list in letters_values_dic.items():
			if char.upper() in letter_list:
				word_score+=value
	return word_score 
		
