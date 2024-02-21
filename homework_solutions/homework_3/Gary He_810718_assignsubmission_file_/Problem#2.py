import wavedrom

# 1) A script that converts a binary number to a decimal number.
def BtoD():
    play = "y"
    while play != "n":
        validcheck = 0
        dec_int = 0
        bin_str = input("Please enter a binary number you want to convert: ")
        bin_len = len(bin_str)
        for i in range(bin_len):
            if int(bin_str[bin_len - i - 1]) > 1:
                print("Please eneter a valid binary number\n")
                validcheck = 1
                break
            dec_int += int(bin_str[bin_len - 1 - i]) * (2**i)
        if validcheck == 1:
            break
        print("The decimal number is: ", dec_int)
        play = input("press any key to continue, press 'n' to quit: ")
        

#2) A script that converts a decimal number to a binary number.
def DtoB():
    play = "y"
    while play != "n":
        bin_str = ""
        neg_str = ""
        count = 0
        neg_check = 0
        dec_int = int(input("Please enter a decimal number you want to convert: "))
        if dec_int == 0:
             print("The binary number is 0 ")
        else:
            if dec_int < 0:
                neg_check = 1
                dec_int = - dec_int
            while dec_int - 2**count >= 0:
                count += 1
                
            #positive==========================================
            for i in range(count-1, -1, -1):  
                if dec_int - 2**i >= 0:
                    dec_int -= 2**i
                    bin_str += "1"
                else:
                    bin_str += "0"
                    
            #negative==========================================
            neg_str = ''.join('1' if bit == '0' else '0' for bit in bin_str)
            neg_str = list(neg_str)            
            for i in range(len(neg_str)-1, -1, -1):
                if neg_str[i] == '0':
                    neg_str[i] = '1'
                    break
                neg_str[i] = '0'
            else:
                neg_str.insert(0, '1')
            neg_str = ''.join(neg_str)
            
            
            #print===========================================
            if neg_check == 0:
                print("The binary number is: ", bin_str)
            else:
                print("The binary number is: ", neg_str)
        play = input("press any key to continue, press 'n' to quit: ")
#3) A script that converts a hexadecimal number to a decimal number.
def HtoD():
    play = "y"
    while play != "n":
        hex_digits = "0123456789ABCDEF"
        Hex_str = input("Please enter a Hexadecimal number you want to convert: ")
        count = 0
        dec_int = 0
        for i in range(len(Hex_str)-1, -1, -1):
            for j in range(len(hex_digits)):
                if hex_digits[j] == Hex_str[i]:
                    dec_int += j * 16**count
                    count += 1
        print("The decimal number is:", dec_int)
        play = input("press any key to continue, press 'n' to quit: ")
                    
            
            

#4) A script that converts a decimal number to a hexadecimal number.
def DtoH():
    play = "y"
    while play != "n":
        neg_check = 0
        dec_int = int(input("Please enter a decimal number you want to convert: "))
        if dec_int == 0:
             print("The Hexadecimal number is 0 ")
        else:
            if dec_int < 0:
                neg_check = 1
                hex_neg = hex(dec_int)

            hex_digits = "0123456789ABCDEF"
            hex_str = ""


            while dec_int > 0:
                remainder = dec_int % 16
                hex_str = hex_digits[remainder] + hex_str
                dec_int = dec_int // 16
            if neg_check == 0:
                print("The Hexadecimal number is:" + "0x" + hex_str)
            else:
                print("The Hexadecimal number is:", hex_neg)
        play = input("press any key to continue, press 'n' to quit: ")


#5) And successfully run the WaveDROM script (in Python3) on Moodle.
def generate_timing_diagram(filename="timingExample.svg"):
    signals = """
    {
        "signal":
            [
                { "name": "CLK", "wave": "p..............."},
                [ "Data",
                    { "name": "D0", "wave": "lhlhlhlhlhlhlhlh"},
                    { "name": "D1", "wave": "l.h.l.h.l.h.l.h."},
                    { "name": "D2", "wave": "l...h...l...h..."},
                    { "name": "D3", "wave": "l.......h......."},
                ]
            ],
        "head":
            {
                "tock":0
            },
        "foot":
            {
                "tock":0
            }
    }"""
    svg = wavedrom.render(signals)
    svg.saveas(filename)

#start here===============================================================================================================================================================
operator = "y"
while operator != "n":
    operator = input("(a).Binary to Decimal \n(b).Decimal to Binary \n(c).Hexadecimal to Decimal \n(d).Decimal to Hexadecimal\n(e).generate timing diagram\nplease enterer the oprator you want to use: ")
    if operator == "a":
        BtoD()
    if operator == "b":
        DtoB()
    if operator == "c":
        HtoD()
    if operator == "d":
        DtoH()
    if operator == "e":
        generate_timing_diagram(filename="timingExample.svg")
    operator = input("press any key to choose operator , press 'n' to quit: ")
    if operator == "n":
        print("Thanks for using, Bye! ")
    
