a = int(input())
b = int(input())
mat = []
for i in range(a):
	c = [int(x) for x in input().split()]
	mat.append(c)
for i in range (a):
	check = b-i-1
	for j in range (b):
		if (i==j):
			print(mat[i][j],end="")
		elif(j==check):
			print(mat[i][j],end="")		
		elif (i!=j):
			print(" ",end="")
	print("")
