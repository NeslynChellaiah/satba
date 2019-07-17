# You are using Python
l = [int(x) for x in input().split()]
n = l[0]
del(l[0])
print (l)
d = l[len(l)-1]
del(l[len(l)-1])
print (l)
for i in range (0,d):
    a = l[0]
    l.remove(l[0])
    l.append(a)
print (l)
for i in range (0,len(l)-1):
    print (l[i],end=" ")
print (l[len(l)-1],end="")
    
