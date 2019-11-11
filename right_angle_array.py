l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
le = len(l[0])-1
for j in range(le,-1,-1):
    for i in range (0,len(l)):
        print(l[i][j],end = " ")
    print("")
