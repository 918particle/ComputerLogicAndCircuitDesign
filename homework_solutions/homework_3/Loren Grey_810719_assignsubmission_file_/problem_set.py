# ------------------------------------------------  HOMEWORK  -------------------------------------------------------

#6.BINARY ----> DECIMAL
def BiToDec(binary_num):
    print(f'Binary: {binary_num}')
    decimal_num = int(binary_num, base=2)
    print(f'Decimal: {decimal_num}')
Bi_A = '100001'
Bi_B = '100111'
Bi_C = '101010'
Bi_D = '111001'
Bi_E = '1100000'
Bi_F = '11111101'
Bi_G = '11110010'
Bi_H = '11111111'
BiToDec(Bi_A)   #Decimal: 33
BiToDec(Bi_B)   #Decimal: 39
BiToDec(Bi_C)   #Decimal: 42
BiToDec(Bi_D)   #Decimal: 57
BiToDec(Bi_E)   #Decimal: 96
BiToDec(Bi_F)   #Decimal: 253
BiToDec(Bi_G)   #Decimal: 242
BiToDec(Bi_H)   #Decimal: 255







#13.DECIMAL ----> BINARY
def DecToBi(num):
    if num >= 1:
        DecToBi(num // 2)
    print(num % 2, end='')
dec_A = 13
dec_B = 17
dec_C = 23
dec_D = 30
dec_E = 35
dec_F = 40
dec_G = 49
dec_H = 60
print("Decimal: 13")        #01101
DecToBi(dec_A)
print("\nDecimal: 17")      #010001
DecToBi(dec_B)
print("\nDecimal: 23")      #010111
DecToBi(dec_C)
print("\nDecimal: 30")      #011110
DecToBi(dec_D)
print("\nDecimal: 35")      #0100011
DecToBi(dec_E)
print("\nDecimal: 40")      #0101000
DecToBi(dec_F)
print("\nDecimal: 49")      #0110001
DecToBi(dec_G)
print("\nDecimal: 60")      #0111100
DecToBi(dec_H)






#22.TWOS COMPLEMENT
def TwosComp(binum):
    l = len(binum)
    i = l - 1
    while (i >= 0):
        if (binum[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return '1' + binum
    j = i - 1
    while (j >= 0):
        if (binum[j] == '1'):
            binum = list(binum)
            binum[j] = '0'
            binum = ''.join(binum)
        else:
            binum = list(binum)
            binum[j] = '1'
            binum = ''.join(binum)
        j -= 1
    return binum
Bi_A = '11'
Bi_B = '110'
Bi_C = '1010'
Bi_D = '1001'
Bi_E = '101010'
Bi_F = '11001'
Bi_G = '11001100'
Bi_H = '11000111'
print(f'Binary: {Bi_A}')
print(f'2s Comp: {TwosComp(Bi_A)}')     #2s Comp: 01
print(f'Binary: {Bi_B}')
print(f'2s Comp: {TwosComp(Bi_B)}')     #2s Comp: 010
print(f'Binary: {Bi_C}')
print(f'2s Comp: {TwosComp(Bi_C)}')     #2s Comp: 0110
print(f'Binary: {Bi_D}')
print(f'2s Comp: {TwosComp(Bi_D)}')     #2s Comp: 0111
print(f'Binary: {Bi_E}')
print(f'2s Comp: {TwosComp(Bi_E)}')     #2s Comp: 010110
print(f'Binary: {Bi_F}')
print(f'2s Comp: {TwosComp(Bi_F)}')     #2s Comp: 00111
print(f'Binary: {Bi_G}')
print(f'2s Comp: {TwosComp(Bi_G)}')     #2s Comp: 00110100
print(f'Binary: {Bi_H}')
print(f'2s Comp: {TwosComp(Bi_H)}')     #2s Comp: 00111001






#39.HEX ----> DECIMAL
def HexToDec(hex):
    print(f'Hex: {hex}')
    c = counter = i = 0
    size = len(hex) - 1
    while size >= 0:
        if hex[size] >= '0' and hex[size] <= '9':
            rem = int(hex[size])
        elif hex[size] >= 'A' and hex[size] <= 'F':
            rem = ord(hex[size]) - 55
        elif hex[size] >= 'a' and hex[size] <= 'f':
            rem = ord(hex[size]) - 87
        else:
            c = 1
            break
        counter = counter + (rem * (16 ** i))
        size = size - 1
        i = i + 1
    print("Decimal: ", counter)
hex_A = '42'
hex_B = '64'
hex_C = '2B'
hex_D = '4D'
hex_E = 'FF'
hex_F = 'BC'
hex_G = '6F1'
hex_H = 'ABC'
HexToDec(hex_A)     #Decimal:  66
HexToDec(hex_B)     #Decimal:  100
HexToDec(hex_C)     #Decimal:  43
HexToDec(hex_D)     #Decimal:  77
HexToDec(hex_E)     #Decimal:  255
HexToDec(hex_F)     #Decimal:  188
HexToDec(hex_G)     #Decimal:  1777
HexToDec(hex_H)     #Decimal:  2748




#40.DECIMAL ----> HEX
def DecToHex(decnum):
    print(f'Dec: {decnum}')
    hex_chars = "0123456789ABCDEF"
    if decnum == 0:
        return "0"
    hexnum = ""
    while decnum > 0:
        r = decnum % 16
        hexnum = hex_chars[r] + hexnum
        decnum //= 16
    print(f'Hex: {hexnum}')
dec_A = 10
dec_B = 15
dec_C = 32
dec_D = 54
dec_E = 365
dec_F = 3652
dec_G = 7825
dec_H = 8925
DecToHex(dec_A)     #Hex: A
DecToHex(dec_B)     #Hex: F
DecToHex(dec_C)     #Hex: 20
DecToHex(dec_D)     #Hex: 36
DecToHex(dec_E)     #Hex: 16D
DecToHex(dec_F)     #Hex: E44
DecToHex(dec_G)     #Hex: 1E91
DecToHex(dec_H)     #Hex: 22DD