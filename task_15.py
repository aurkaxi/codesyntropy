# word frequency counter

usr = input("Enter a phrase: ").lower()
for i in usr:
    if i in ".,!?":
        usr = usr.replace(i, "")
usr = usr.split()

counts = {}

for word in usr:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, count in counts.items():
    print(word, count)
