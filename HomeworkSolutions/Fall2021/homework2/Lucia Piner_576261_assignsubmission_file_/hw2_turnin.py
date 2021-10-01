#cosc 330 hw 2 functions

def hex_to_bin(x):
    nums = [10 if bit == 'A' 
        else 11 if bit == 'B'
        else 12 if bit == 'C' 
        else 13 if bit == 'D'
        else 14 if bit == 'E' 
        else 15 if bit == 'F'
        else int(bit) for bit in str(x)]
    result = []
    c = 0
    for digit in nums:
        result.append(dec_to_bin(digit))
        i = 0
        while len(result[c]) < 4:
            result[c].insert(i,0)
            i+=1
        c+=1
    return result

def bin_to_dec(xb):
    result = 0
    nums = [int(bit) for bit in str(xb)]
    nums.reverse()
    for i in range(0,len(nums)):
        result = result + nums[i]*2**i
    return result

def dec_to_bin(xd):
    result = []
    while (xd > 0):
        result.append(xd%2)
        xd = xd//2
    result.reverse()
    return result

def hex_to_dec(x):
    result = 0
    nums = [10 if bit == 'A' 
        else 11 if bit == 'B'
        else 12 if bit == 'C' 
        else 13 if bit == 'D'
        else 14 if bit == 'E' 
        else 15 if bit == 'F'
        else int(bit) for bit in str(x)]
    nums.reverse()
    for i in range(0,len(nums)):
        result = result + nums[i]*16**i
    return result


def dec_to_hex(x):
    result = []
    while (x > 0):
        num = x%16
        if num == 15:
            result.append('F')
        elif num == 14:
            result.append('E')
        elif num == 13:
            result.append('D')
        elif num == 12:
            result.append('C')
        elif num == 11:
            result.append('B')
        elif num == 10:
            result.append('A')
        else:
           result.append(num) 
        x = x//16
    result.reverse()
    return result

#x = 0010 1001
#bcd = 2 9
def bcd(x):
    result = []
    l = len(x)
    while l//4 > 0:
        result.append(bin_to_dec(x[l-4:l]))
        l = l-4
    result.reverse()
    return result

def bin_to_grey(x):
    nums = [int(bit) for bit in str(x)]
    result = []
    result.append(nums[0])
    for i in range(0,len(nums)-1):
        if (nums[i]+nums[i+1])%2 == 0:
            result.append(0)
        else:
            result.append(1)
    return result

def grey_to_bin(x):
    nums = [int(bit) for bit in str(x)]
    result = []
    result.append(nums[0])
    for i in range(0,len(nums)-1):
        if (result[i]+nums[i+1])%2 == 0:
            result.append(0)
        else:
            result.append(1)
    return result
#1 = even # 1's
#0 = odd # 1's
def parity(x):
    nums = [int(bit) for bit in str(x)]
    count = 0
    for i in range(1,len(nums)):
        if nums[i] == 1: count+=1
    if nums[0] == 0:
        #print('want odd # 1's')
        if count%2 == 0:
            return False
    else:
        #print('want even # 1's')
        if count%2 == 1:
            return False
    return True

#=====================================================

print('---37---')
print('a: 0x38 =',hex_to_bin('38'))
print('b: 0x59 =',hex_to_bin('59'))
print('c: 0xA14 =',hex_to_bin('A14'))
print('d: 0x5C8 =',hex_to_bin('5C8'))
print('e: 0x4100 =',hex_to_bin('4100'))
print('f: 0xFB17 =',hex_to_bin('FB17'))
print('g: 0x8A9D =',hex_to_bin('8A9D'))
print()

print('---39---')
print('a: 0x23 =',hex_to_dec('23'))
print('b: 0x92 =',hex_to_dec('92'))
print('c: 0x1A =',hex_to_dec('1A'))
print('d: 0x8D =',hex_to_dec('8D'))
print('e: 0xF3 =',hex_to_dec('F3'))
print('f: 0xEB =',hex_to_dec('EB'))
print('g: 0x5C2 =',hex_to_dec('5C2'))
print('h: 0x700 =',hex_to_dec('700'))
print()

print('---40---')
print('a: 8 =',dec_to_hex(8))
print('b: 14 =',dec_to_hex(14))
print('c: 33 =',dec_to_hex(33))
print('d: 52 =',dec_to_hex(52))
print('e: 284 =',dec_to_hex(284))
print('f: 2890 =',dec_to_hex(2890))
print('g: 4019 =',dec_to_hex(4019))
print('h: 6500 =',dec_to_hex(6500))
print()

print('---50---')
print('a: 0001 =',bcd('0001'))
print('b: 0110 =',bcd('0110'))
print('c: 1001 =',bcd('1001'))
print('d: 00011000 =',bcd('00011000'))
print('e: 00011001 =',bcd('00011001'))
print('f: 00110010 =',bcd('00110010'))
print('g: 01000101 =',bcd('01000101'))
print('h: 10011000 =',bcd('10011000'))
print('i: 100001110000 =',bcd('100001110000'))
print()

print('---56---')
print('a: 11011 =',bin_to_grey('11011'))
print('b: 1001010 =',bin_to_grey('1001010'))
print('c: 1111011101110 =',bin_to_grey('1111011101110'))
print()

print('---57---')
print('a: 1010 =',grey_to_bin('1010'))
print('b: 00010 =',grey_to_bin('00010'))
print('c: 11000010001 =',grey_to_bin('11000010001'))
print()

print('---60---')
print('ascii code: Hello. How are you?')
print()

print('---63---')

print('a: 100110010 =',end=' ')
if parity('100110010'): print('no mistake') 
else: print('mistake')

print('b: 011101010 =',end=' ')
if parity('011101010'): print('no mistake') 
else: print('mistake')

print('c: 10111111010001010 =',end=' ')
if parity('10111111010001010'): print('no mistake') 
else: print('mistake')

print("Minus one: True False True (even parity bit is zero)")































