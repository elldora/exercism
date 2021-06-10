def convert(number):
	numSound = {3:"Pling", 5:"Plang", 7:"Plong"}
	result = ""
	for num, sound in (numSound.items()):
		if number%num==0:
			result+=sound
	return result if len(result)!=0 else f"{number}" 
    
