import converter
import sys

#2-2, 6
print("2-2,6")
l = ['1110','1010','11100','10000','10101','11101','10111','11111']
for n in l:
	print(converter.convert_bin_dec(n))

#2-2, 8
print("2-2,8")
l = ['2','3','4','5','6','7','8','9','10','11']
for n in l:
	print(converter.max_dec(n))

#2-2, 10
print("2-2,10")
converter.counter(0,7)
print("\n")
converter.counter(8,15)
print("\n")
converter.counter(16,31)
print("\n")
converter.counter(32,63)
print("\n")
converter.counter(64,123)

#2-3, 13
print("2-3,13")
l = ['15','21','28','34','40','59','65','73']
for n in l:
	print(converter.convert_dec_bin(int(n)))

#2-4, 15
print("2-4,15")
x = ['11','10','101','111','1001','1101']
y = ['01','10','11','110','101','1011']
for i,j in zip(x,y):
	print(converter.add_bin(i,j))

#2-2, 19
print("2-5,19")
print("For 8 bit numbers:")
print("00000000 or 11111111")