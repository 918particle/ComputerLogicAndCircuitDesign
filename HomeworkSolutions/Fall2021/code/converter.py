def convert_dec_bin(x):
	result = []
	while(x != 0):
		result.append(x%2)
		x = x // 2
	result.reverse()
	return result

def convert_bin_dec(x):
	result = 0
	str_num = [int(d) for d in str(x)]
	str_num.reverse()
	n = len(str_num)
	for i in range(n):
		result += 2**i * int(str_num[i])
	return result

def max_dec(n):
	return 2**int(n) - 1

def counter(n,m):
	for i in range(n,m+1):
		if(i==0):
			print('[0]')
		else:
			print(convert_dec_bin(i))

def add_bin(x,y):
	return convert_bin_dec(x) + convert_bin_dec(y)

def two_comp(x):
	str_num = [int(d) for d in str(x)]
	n = len(str_num)
	for i in range(0,n):
		if(str_num[i]=='1'):
			str_num[i]='0'
		if(str_num[i]=='0'):
			str_num[i]='1'
	if(str_num[n-1]=='0'):
		str_num[n-1]='1'
	if(str_num[n-1]=='1'):
		str_num
	print(str_num)