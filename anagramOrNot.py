a = input()
a = a.lower()
a = sorted(a)
b = input()
b = b.lower()
b = sorted(b)
if a==b:
	print("Anagram")
else:
	print("Not an anagram")
