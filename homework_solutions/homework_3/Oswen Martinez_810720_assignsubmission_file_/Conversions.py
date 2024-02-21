# # BINARY TO DECIMAL
# binary = input("Enter Binary: ")
# decimal = 0
# power = len(binary) - 1
# i = 0
#
# while i < len(binary):
#     if binary[i] == '1':
#         decimal += 2 ** power
#     power -= 1
#     i += 1
# print("DECIMAL IS:", decimal)

# # DECIMAL TO BINARY
# decimal = int(input("Enter a decimal number: "))
# binary = ""
#
# while decimal > 0:
#     remainder = decimal % 2
#     binary = str(remainder) + binary
#     decimal = decimal // 2
#
# print("BINARY IS:", binary)

#
# #DECIMAL TO HEX
# decimal = int(input("Enter a decimal number: "))
# hex_chars = "0123456789ABCDEF"
# hex_number = ""
# while decimal > 0:
#         remainder = decimal % 16
#         hex_number = hex_chars[remainder] + hex_number
#         decimal = decimal // 16
# print(hex_number)
#
#HEX TO DECIMAL
hex_number = input("Enter a hex number: ")
decimal_1 = 0
hex_chars = "0123456789ABCDEF"
for digit in hex_number:
    decimal_1 = decimal_1 * 16 + hex_chars.index(digit)

print(decimal_1)