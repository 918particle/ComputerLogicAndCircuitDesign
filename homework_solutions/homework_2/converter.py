def bin2dec(x):
	if(isinstance(x,str)):
		n = len(x)
		count=n
		result=0
		for i in x:
			result+=int(i)*(2**(count-1))
			count-=1
		return result
	else:
		print("Input must be a string.")

defin 2comp(x):
	
