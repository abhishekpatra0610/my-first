str1=input("enter first string:")
str2=input("enter second string:")

if sorted(str1.lower())==sorted(str2.lower()):
    print("anagrams")
else:
    print("not anagrams")
    