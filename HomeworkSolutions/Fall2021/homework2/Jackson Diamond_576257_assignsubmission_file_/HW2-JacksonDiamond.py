#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:20:47 2021

@author: jackson
"""
print("14/16 points, well done.")
print("\n2-8 - 37")

hex_list = ["38", "59", "A14" , "5C8" , "4100" , "FB17", "8A9D"]
for i in range(0, len(hex_list)):
    stringy = hex_list[i]
    print(bin(int(stringy, 16))[2:].zfill(8))


print("\n2-8 - 39")

hex_list2 = ["23", "92", "1A" , "8D" , "F3" , "EB", "5C2" , "700"]
for s in range(0, len(hex_list2)):
    stringu = hex_list2[s]
    dec = int(stringu, 16)
    print(str(dec))
    
    
print("\n2-8 - 40")

dec_list = ['8','14','33','52','284','2890','4019','6500']
for i in range(0, len(dec_list)):
    intu = int(dec_list[i])
    print(hex(intu))
    
    
print("\n2-10 - 50")

bcd_list = ['0001','0110','1001','00011000','00011001','00110010','01000101','10011000','100001110000']
for i in range(0, len(bcd_list)):
    binary_string = bcd_list[i]
    numStr = ""
    for x in range(0, len(binary_string)//4):
        four = binary_string[x*4:x*4+4]
        deci = int(four,2)
        numStr += str(deci)
    print(numStr)
    

print("\n2-11 - 56")

bin_list = ["00011011","01001010","0001111011101110"]

def xor_c(a, b):
    return '0' if(a == b) else '1';

for i in range(0, len(bin_list)):
    binstr = bin_list[i]
    gray = binstr[0]
    for i in range(1, len(binstr)):
        gray += xor_c(binstr[i - 1], binstr[i]);
    print(gray)


print("\n2-11 - 57")

gray_list = ["1010","00010","11000010001"]

def flip(c):
    return '1' if(c == '0') else '0';
 
for c in range(0, len(gray_list)):
    stringr = gray_list[c]
    binary = stringr[0]
    for i in range(1,len(stringr)):
        if (stringr[i] == '0'):
            binary += binary[i - 1];
        else:
            binary += flip(binary[i - 1]);
    print(binary)
    
    
print("\n2-11 - 60")
print("minus one point: tried to debug ascii_text, I think the b2a function needs bytes.")
import binascii
ascii_list = ['1001000','1100101','1101100','1101100','1101111','0101110',
              '0100000','1001000','1101111','1110111','0100000','1100001',
              '1110010','1100101','0100000','1111001','1101111','1110101','0111111']
for i in range(0,len(ascii_list)):
	code = int(ascii_list[i],2)
	ascii_text = binascii.b2a_uu(code)
	print(ascii_text)
    
print("\n2-12 - 64")
print("minus one: I get True False True, but you get True True False")
print("A and B have no error, but C dose")

