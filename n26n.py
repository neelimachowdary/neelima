#include<stdio.h>
void main()
{
int k[10],i,j,tmp,m;
printf("enter the number");
scanf("%d",&m);
printf("enter the number");
for(i=0;i<m;i++)
{
scanf("%d",&k[i]);
}
for(i=0;i<m;i++)
{
for(j=i+1;j<m;j++)
{
if(k[i]>k[j])
{
tmp=k[i];
k[i]=k[j];
k[j]=tmp;
}
}
}
for(i=0;i<m;i++)
{
printf("%d",k[i]);
}
}
