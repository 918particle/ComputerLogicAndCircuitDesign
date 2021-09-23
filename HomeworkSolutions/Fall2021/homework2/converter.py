hex_digits = {'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],'4':[0,1,0,0], \
'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],'8':[1,0,0,0],'9':[1,0,0,1],'A':[1,0,1,0], \
'B':[1,0,1,1],'C':[1,1,0,0],'D':[1,1,0,1],'E':[1,1,1,0],'F':[1,1,1,1]}
hex_conv = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, \
'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
hex_conv_rev = {y:x for x,y in hex_conv.items()}

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

def one_comp(x):
	str_num = [int(d) for d in str(x)]
	n = len(str_num)
	for i in range(0,n):
		if(int(str_num[i])==1):
			str_num[i]=0
			continue
		if(int(str_num[i])==0):
			str_num[i]=1
			continue
	return str_num

def two_comp(x):
	str_num = one_comp(x)
	str_pass = ''
	for i in str_num:
		str_pass+=str(i)
	return convert_dec_bin(add_bin(str_pass,1))

def convert_hex_bin(x):
	n = len(x)
	result = []
	for i in range(0,n):
		block = hex_digits[x[i]]
		result.extend(block)
	return result

def convert_hex_dec(x):
	result = 0
	n = len(x)
	for i in reversed(range(n)):
		result += 16**i * hex_conv[x[i]]
	return result

def convert_dec_hex(x):
	result = []
	while(x != 0):
		result.append(hex_conv_rev[x%16])
		x = x // 16
	result.reverse()
	return result

def convert_bcd_dec(x):
	list_in = []