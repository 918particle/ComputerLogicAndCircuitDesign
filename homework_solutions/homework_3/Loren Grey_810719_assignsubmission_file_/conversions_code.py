

#BINARY ----> DECIMAL
def BiToDec(binary_num):
    print(f'Binary: {binary_num}')
    decimal_num = int(binary_num, base=2)
    print(f'Decimal: {decimal_num}')
Bi_Example = '100010'
BiToDec(Bi_Example)



#DECIMAL ----> BINARY
def DecToBi(num):
    if num >= 1:
        DecToBi(num // 2)
    print(num % 2, end='')
decimal_Example = 32
DecToBi(decimal_Example)




# TWOS COMPLEMENT
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
Bi_Example = "00000101"
print(TwosComp(Bi_Example))




#HEX ----> DECIMAL
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
hex_Example = "A12"
HexToDec(hex_Example)




#DECIMAL ----> HEX
def DecToHex(decnum):
    hex_chars = "0123456789ABCDEF"
    if decnum == 0:
        return "0"
    hexnum = ""
    while decnum > 0:
        r = decnum % 16
        hexnum = hex_chars[r] + hexnum
        decnum //= 16
    print(f'Hex: {hexnum}')
dec_Example = 40
DecToHex(dec_Example)








