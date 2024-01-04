# program to print prime numbers of a specific range

start = int(input("start: "))
end = int(input("end: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
