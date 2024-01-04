# patterns

n = 5
# Right-angled triangle pattern

for i in range(1, n + 1):
    print("*" * i)

# diamond pattern
for i in range(1, n + 1):
    stars = "*" * (2 * i - 1)
    spaces = " " * (n - i)
    print(spaces + stars)

for i in range(n - 1, 0, -1):
    stars = "*" * (2 * i - 1)
    spaces = " " * (n - i)
    print(spaces + stars)
