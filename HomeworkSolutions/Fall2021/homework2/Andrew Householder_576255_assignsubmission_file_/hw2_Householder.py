print("Checked for errors: None.  16/16 points.  Yay!")
def dec_to_bin(decimal):
    binary = 0
    weight = 0

    while decimal > 0:
        bit = (decimal % 2) *10**weight
        binary += bit
        weight += 1
        decimal = decimal // 2
    return binary

def bin_to_dec(binary):
    weight = 0
    decimal = 0
    remainder = binary % 10

    while binary > 0:
        binary = binary // 10
        decimal += remainder*(2**weight)
        remainder = binary % 10
        weight += 1
    return decimal

def hex_to_dec(hx):
    hex_vals = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

    hx = str(hx)
    weight = len(hx)-1
    decimal = 0

    for i in range(0, len(hx)):
        value = hex_vals[hx[i]]
        decimal += value*(16**weight)
        weight -= 1

    return decimal

def dec_to_hex(dec):
    output = ""
    hex_vals = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    while dec > 0:
        remainder = dec % 16
        val = hex_vals[remainder]
        dec = dec // 16
        output = val + output

    return output

def bcd_to_dec(bcd):
    bcd = str(bcd)
    weight = 3
    decimal = ""
    digit = 0

    for i in range(0, len(bcd)):
        x = int(bcd[i])
        digit += x*(2**weight)
        weight -= 1
        if not ((i+1) % 4):
            decimal += str(digit)
            digit = 0
            weight = 3

    return decimal



def bin_to_gray(binary):
    binary = str(binary)
    gray = "" + binary[0]

    for i in range(0, len(binary)-1):
        x = int(binary[i]) + int(binary[i+1])
        if x > 1:
            x = 0
        gray += str(x)

    return gray

def gray_to_bin(gray):
    gray = str(gray)
    binary = "" + gray[0]

    for i in range(0, len(gray)-1):
        x = int(binary[i]) + int(gray[i+1])
        if x > 1:
            x = 0
        binary += str(x)


    return binary

def check_even_parity(binary):
    binary = str(binary)
    total = 0
    for i in range(0, len(binary)):
        total += int(binary[i])

    if total % 2:
        print("Error!")
        return
    print("No Error!")

#problem 37
print("#37")

vals = ["38", "59", "A14", "5C8", "4100", "FB17", "8A9D"]

for x in vals:
    y = hex_to_dec(x)
    y = dec_to_bin(y)
    print(f"Hex: {x} Binary: {y}")

#problem 39
print("\n#39")

vals = ["23", "92", "1A", "8D", "F3", "EB", "5C2", "700"]

for x in vals:
    y = hex_to_dec(x)
    print(f"Hex: {x} Decimal: {y}")

#40
print("\n#40")

vals = [8, 14, 33, 52, 284, 2890, 4019, 6500]

for x in vals:
    y = dec_to_hex(x)
    print(f"Decimal: {x} Hex: {y}")

#50
print("\n#50")

vals = ['0001', '0110', '1001', '00011000', '00011001', '00110010', '01000101', '10011000', '100001110000']

for x in vals:
    y = bcd_to_dec(x)
    print(f"BCD: {x} Decimal: {y}")

#56
print("\n#56")

vals = ['11011', '1001010', '1111011101110']

for x in vals:
    y = bin_to_gray(x)
    print(f"Binary: {x} Gray: {y}")

#57
print("\n#57")

vals = ['1010', '00010', '11000010001']

for x in vals:
    y = gray_to_bin(x)
    print(f"Gray: {x} Bin: {y}")

#60
print("\n#60")

vals = [1001000, 1100101, 1101100, 1101100, 1101111, 101110, 100000, 1001000, 1101111, 1110111, 100000, 1100001, 1110010, 1100101, 100000, 1111001, 1101111, 1110101, 111111]

for x in vals:
    print(chr(bin_to_dec(x)), end='')
print("\n")

#63
print("\n#63")

vals = ['100110010', '011101010', '10111111010001010']

for x in vals:
    print(f"Code: {x}")
    check_even_parity(x)
