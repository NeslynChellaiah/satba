a = int(input())
a = bin(a)
count = 0
for i in a:
	if i == '1':
		count += 1
count = str(count)
for i in range (len(a)-1,-1,-1):
	if a[i] == '1':
		least = len(a)-1-i
		break
least = str(least)
for i in range (0,len(a)):
	if a[i] == '1':
		high = len(a)-1-i
		break
high = str(high)

print(count+"#"+least+"#"+high)
