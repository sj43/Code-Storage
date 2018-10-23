#include<bits/stdc++.h>
using namespace std;
long long d[11][101][101][101];
long long c[11][11];
long long go(int n, int r, int g, int b){
  if(r<0 || g<0|| b<0){
    return 0;
  }
  if(n==0){
    return 1;
  }
  if(d[n][r][b][g]!=-1){
    return d[n][r][b][g];
  }
  d[n][r][g][b] = 0;
  d[n][r][g][b] += go(n-1,r-n,g,b);
  d[n][r][g][b] += go(n-1,r,g-n,b);
  d[n][r][g][b] += go(n-1,r,g,b-n);
  if(n%2==0){
    d[n][r][g][b] += go(n-1,r-n/2,g-n/2,b)*c[n][n/2];
    d[n][r][g][b] += go(n-1,r-n/2,g,b-n/2)*c[n][n/2];
    d[n][r][g][b] += go(n-1,r,g-n/2,b-n/2)*c[n][n/2];
  }
  if(n%3==0){
    d[n][r][g][b] += go(n-1,r-n/3,g-n/3,b-n/3)*c[n][n/3]*c[n-n/3][n/3];
  }
  return d[n][r][g][b];
}
int main(){
  int n,r,g,b;
  cin>>n>>r>>g>>b;
  c[0][0]=1;
  for(int i=1;i<=10;i++){
    c[i][0] = c[i][i] = 1;
    for(int j=1;j<i;j++){
      c[i][j] = c[i-1][j-1] + c[i-1][j];
    }
  }
  memset(d,-1,sizeof(d));
  cout<<go(n,r,g,b)<<'\n';
  return 0;
}
