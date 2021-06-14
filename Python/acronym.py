def abbreviate(words):
	words = words.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"})
	list_of_words = [word for word in words.split()]
	return "".join(word[0].upper() for word in list_of_words)
