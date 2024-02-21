def dec2hex(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal %16
        if remainder < 10:
            hexadecimal = str(remainder)+hexadecimal
        else:
            hexadecimal=chr(remainder+55)+hexadecimal
        decimal //=16
    return hexadecimal
while 1:
    dec_number=int(input("Enter a decimal number: "))
    hex_number = dec2hex(dec_number)
    print("Hexadecimal number: ", hex_number)
"""
40)Convert each decimal number to hexadecimal:
A)8=8
B)14=E
C)33=21
D)52=34
E)284=11C
F)2890=B4A
G)4019=FB3
H)6500=1964
"""