#include<bits/stdc++.h>
using namespace std;
long long d[101][21];
int a[101];
int main(){
  int N;
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>a[i];
  }
  d[0][a[0]] = 1;
  for(int i=1;i<N-1;i++){
    for(int j=0; j<=20; j++){
      if(j-a[i] >= 0){
        d[i][j] += d[i-1][j-a[i]];
      }
      if(j+a[i] <= 20){
        d[i][j] += d[i-1][j+a[i]];
      }
    }
  }
  cout<<d[N-2][a[N-1]]<<endl;
  return 0;
}
