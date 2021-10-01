import converter

#2-8, 37, 39, 40
print("2-8,37")
l = ['38','59','A14','5C8','4100','FB17','8A9D']
for i in l:
	print(converter.convert_hex_bin(i))
print("2-8,39")
l = ['23','92','1A','8D','F3','EB','5C2','700']
for i in l:
	print(converter.convert_hex_dec(i))
print("2-8,40")
l = ['8','14','33','52','284','2890','4019','6500']
for i in l:
	print(converter.convert_dec_hex(i))
print("2-10,50")
l = ['0001','0110','1001','00011000','00011001','00110010','01000101','10011000','100001110000']
for i in l:
	print(converter.convert_bcd_dec(i))
print("2-11,56")
l = ['11011','1001010','1111011101110']
for i in l:
	print(converter.convert_bin_gray(i))
print("2-11,57")
l = ['1010','00010','11000010001']
for i in l:
	print(converter.convert_gray_bin(i))
print("2-11,60")
l = ['1001000','1100101','1101100','1101100','1101111','0101110','0100000','1001000','1101111', \
'1110111','0100000','1100001','1110010','1100101','0100000','1111001','1101111','1110101','0111111']
for i in l:
	print(converter.convert_bin_ascii(i))
print("2-12,63")
l = ['100110010','011101010','10111111010001010']
for i in l:
	print(converter.parity_check(i))