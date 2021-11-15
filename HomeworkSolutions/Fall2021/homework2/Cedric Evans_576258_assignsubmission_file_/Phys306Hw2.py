print("These look like different problems than mine.  I find no problems with your code, though")
print("16/16 points.")
#====2-8, 37=====================
def HexBin(ini_string):
    scale = 16
    res = bin(int(ini_string, scale)).zfill(8)
    print(res)
print('Problem: 2-8, 37')
HexBin('46a')
HexBin('54a')
HexBin('B4a')
HexBin('1A3a')
HexBin('FAa')
HexBin('ABCa')
HexBin('ABCDa')
print(20*'-')
#================================
#====2-8, 39=====================
def HexDec(ini_string):
    res = int(ini_string, 16)
    print(res)
print('Problem: 2-8, 39')
HexDec('42')
HexDec('64')
HexDec('2B')
HexDec('4D')
HexDec('FF')
HexDec('BC')
HexDec('6F1')
HexDec('ABC')
print(20*'-')
#================================
#====2-8, 40=====================
print('Problem: 2-8, 40')
print(hex(10))
print(hex(15))
print(hex(32))
print(hex(54))
print(hex(365))
print(hex(3652))
print(hex(7825))
print(hex(8925))
print(20*'-')
#================================
#====2-10, 50====================
def BCD2Dec(s):
    length = len(s)
    check = 0
    check0 = 0
    num = 0
    sum = 0
    mul = 1
    rev = 0
    for i in range(length - 1, -1, -1):
        sum += (ord(s[i]) - ord('0')) * mul
        mul *= 2
        check += 1
        if (check == 4 or i == 0):
            if (sum == 0 and check0 == 0):
                num = 1
                check0 = 1              
            else:
                num = num * 10 + sum      
            check = 0
            sum = 0
            mul = 1
    while (num > 0):
        rev = rev * 10 + (num % 10)
        num //= 10
    if (check0 == 1):
        return rev - 1     
    return rev
print('Problem: 2-10, 50')
if __name__ == "__main__":
    print(BCD2Dec("0001"))
    print(BCD2Dec("0110"))
    print(BCD2Dec("1001"))
    print(BCD2Dec("00011000"))
    print(BCD2Dec("00011001"))
    print(BCD2Dec("00110010"))
    print(BCD2Dec("01000101"))
    print(BCD2Dec("10011000"))
    print(BCD2Dec("100001110000"))
print(20*'-')
#=================================
#====2-11, 56=====================
def xor_c(a, b):
    return '0' if(a == b) else '1'
def flip(c):
    return '1' if(c == '0') else '0'
def Gray(b):
    gray = ""
    gray += b[0]
    for i in range(1, len(b)):
        gray += xor_c(b[i - 1], b[i])
    return gray

print('Problem: 2-11, 56')
print(Gray('1010'))
print(Gray('1001010'))
print(Gray('1111011101110'))
print(20*'-')
#====2-11, 57======================
def Binary(g):
    binary = ""
    binary += g[0]
    for i in range(1, len(g)):
        if (g[i] == '0'):
            binary += binary[i - 1]
        else:
            binary += flip(binary[i - 1])
    return binary

print('Problem: 2-11, 57')
print(Binary('1010'))
print(Binary('00010'))
print(Binary('11000010001'))
print(20*'-')
#=================================
#====2-12, 63=====================
print('Problem: 2-12, 63')
print('a) is the parity code out of order.')