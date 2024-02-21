def hex2dec(hexadecimal):
    decimal = 0
    power = len(hexadecimal)-1
    for i in hexadecimal:
        if i.isdigit():
            decimal += int(i) * (16**power)
        else:
            decimal += (ord(i.upper()) - 55) * (16**power)
        power -= 1
    return decimal
while 1:
    hex_number = input("Enter a hexadecimal number: ")
    dec_number = hex2dec(hex_number)
    print("Decimal number: ", dec_number)
"""
39)Convert each hexadecimal number to decimal:
A)23=35
B)92=146
C)1A=26
D)8D=141
E)F3=243
F)EB=235
G)5C2=1474
H)700=1792
"""