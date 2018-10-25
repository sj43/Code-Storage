#include<bits/stdc++.h>
using namespace std;
int d[301][301];
int chocolate(int n, int m){
  if(d[n][m]>0) return d[n][m];
  if(n==1 && m==1) return 0;
  if(n==1) return d[n][m] = chocolate(n,m/2)+chocolate(n,m-m/2)+1;
  else return d[n][m] = chocolate(n/2,m)+chocolate(n-n/2,m)+1;
}
int main(){
  int N,M;
  cin>>N>>M;
  cout<<chocolate(N,M)<<endl;
  return 0;
}
