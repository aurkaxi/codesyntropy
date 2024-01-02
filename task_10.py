temp = int(input("Enter temperature: "))
unit = input("Enter desired unit (C/F): ")

if unit == "C":
    print((temp * 9 / 5) + 32)
elif unit == "F":
    print((temp - 32) * 5 / 9)
