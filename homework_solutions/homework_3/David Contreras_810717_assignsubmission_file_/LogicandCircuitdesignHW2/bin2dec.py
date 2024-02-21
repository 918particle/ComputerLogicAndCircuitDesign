def bin2dec(binary):
    dec = 0
    power = len(binary)-1
    for i in binary:
        dec += int(i)*(2**power)
        power -= 1
    return dec
while 1:
    bin_number = input("Enter a binary number: ")
    dec_number = bin2dec(bin_number)
    print("Decimal Number: ", dec_number)
"""
6)Convert the following binary numbers to decimal:
A)1110=14       
B)1010=10       
C)11100=28       
D)10000=16      
E)10101=21      
F)11101=29      
G)10111=23       
H)11111=31
"""