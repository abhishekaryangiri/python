# Check palindrome
word = input("Enter word")
reverse = ""
for i in word:
    reverse = i + reverse
# print it outside loop
if  word == reverse:
    print("palindrom")
else:
    print("Not Palindrom")