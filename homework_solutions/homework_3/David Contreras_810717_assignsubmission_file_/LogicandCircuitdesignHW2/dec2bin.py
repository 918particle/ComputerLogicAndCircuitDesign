def dec2bin(decimal):
    binary= ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //=2
    return binary
while 1:
    dec_number = int(input("Enter a decimal number: "))
    bin_number = dec2bin(dec_number)
    print("Binary number: ", bin_number)
"""
13)Convert each decimal number to binary using repeated division by 2:
A) 15=1111 
B) 21=10101
C) 28=11100
D) 34=100010
E) 40=101000
F) 59=111011
G) 65=1000001
H) 73=1001001
"""