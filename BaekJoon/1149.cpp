#include<bits/stdc++.h>
using namespace std;
int d[1001][3];
int main(){
  int N,r,g,b;
  cin>>N;
  cin>>d[0][0]>>d[0][1]>>d[0][2];
  for(int i=1;i<N;i++){
    cin>>r>>g>>b;
    d[i][0] = min(d[i-1][1],d[i-1][2])+r;
    d[i][1] = min(d[i-1][0],d[i-1][2])+g;
    d[i][2] = min(d[i-1][0],d[i-1][1])+b;
  }
  cout<<min(d[N-1][2],min(d[N-1][0],d[N-1][1]))<<endl;
  return 0;
}
