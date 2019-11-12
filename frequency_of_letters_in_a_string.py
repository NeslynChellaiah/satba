a = input()
a=sorted(a)
dic = {}
for i in a:
	if i in dic:
		dic[i]+=1
	else:
		dic[i]=1
for i in dic.keys():
	print(i+str(dic[i]),end="")
