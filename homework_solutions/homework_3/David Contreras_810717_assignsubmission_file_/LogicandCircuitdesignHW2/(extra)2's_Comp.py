#Alternative Method
def twos_comp(binary):
    complement = ""
    one_found = False
    for bits in binary[::-1]: #iterate backwards
        if one_found:
            if bits == '0':
                complement = '1' + complement
            else:
                complement = '0' + complement
        else:
            complement= bits + complement
            if bits == '1':
                one_found = True
    return complement
while 1:
    bin_number = input("Enter binary number: ")
    complement = twos_comp(bin_number)
    print("Twos Complement: ", complement)
"""
22)Determine the 2s complement of each binary number using either method:
A)10=10
B)111=001
C)1001=0111
D)1101=0011
E)11100=00100
F)10011=01101
G)10110000=01010000
H)00111101=11000011
"""