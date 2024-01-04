# bin to decimal

usr = input("Enter a binary number: ")

decimal = 0
for i in range(len(usr)):
    decimal += int(usr[i]) * 2 ** (len(usr) - i - 1)

print(decimal)
