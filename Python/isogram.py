def is_isogram(string):
	string = string.translate({ord(sign): "" for sign in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+ \"'"}).lower()	
	for char in string:
		if string.count(char)>=2:
			return False
	return True
