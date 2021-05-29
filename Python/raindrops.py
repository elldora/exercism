def convert(number):
	sound = ("Pling", "Plang", "Plong")
	numbers = (3, 5, 7)
	result = ""
	
	for i in range(len(numbers)):
		if number%numbers[i]==0:
			result+=sound[i]
			
	return result if len(result)!=0 else f"{number}" 
    
