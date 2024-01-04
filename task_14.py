# write a program that checks a given phrase (ignoring spaces, punctuations and case) is a palindrome or not.

usr = input("Enter a phrase: ")
usr = usr.lower()

for i in usr:
    if i in ".,!? ":
        usr = usr.replace(i, "")

if usr == usr[::-1]:
    print("Palindrome")

else:
    print("Not Palindrome")
