#include<bits/stdc++.h>
using namespace std;
int d[10001];
int wine[10001];
int main(){
  int N;
  cin>>N;
  for(int i=1;i<=N;i++){
    scanf("%d",&wine[i]);
  }
  d[1] = wine[1];
  d[2] = wine[1] + wine[2];
  for(int i=3;i<=N;i++){
    d[i] = max(d[i-1],max(d[i-2]+wine[i],d[i-3]+wine[i-1]+wine[i]));
  }
  cout<<d[N]<<endl;
  return 0;
}
