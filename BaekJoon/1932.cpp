#include<bits/stdc++.h>
using namespace std;
int tri[501][501];
int d[501][501];
int main(){
  int N;
  cin>>N;
  for(int i=0;i<N;i++){
    for(int j=0;j<=i;j++){
      scanf("%d",&tri[i][j]);
    }
  }
  d[0][0] = tri[0][0];
  for(int i=1;i<N;i++){
    for(int j=0;j<=i;j++){
      if(j==0) d[i][j] = d[i-1][j] + tri[i][j];
      else d[i][j] = max(d[i-1][j-1],d[i-1][j]) + tri[i][j];
    }
  }
  int maximum = 0;
  for(int i=0;i<N;i++){
    maximum = max(maximum,d[N-1][i]);
  }
  cout<<maximum<<endl;

  return 0;
}
