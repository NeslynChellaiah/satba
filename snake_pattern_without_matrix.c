#include<stdio.h>
int main(){
	int a,p;
	scanf("%d",&a);
	int b =a;
	a = a*a;
	for (int i=1; i<=a; i++){
		if(i%4==0){
			printf("%d ",i);
			i = i+b;
			int check = 0;
			for (int j=0;j<b;j++)
				{
					p = i-check;
					printf("%d ",p);
					check++;
				}
		}
		else
			printf("%d ",i);
	}
	return 0;
}
