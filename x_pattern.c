#include<stdio.h>
int main(){
	int i,j,l,m,check;
	scanf("%d",&i);
	scanf("%d",&j);
	int a[i][j];
	for (l=0;l<i;l++){
		for (m=0;m<j;m++){
			scanf("%d",&a[l][m]);
		}
	}
	for (l=0;l<i;l++){
		check = j-l-1;
		for (m=0;m<j;m++){
			if(m==check)
				printf("%d",a[l][m]);
			else if(l==m)
				printf("%d",a[l][m]);
			else
				printf(" ");
		}
		printf("\n");
	}
	return 0;
}
