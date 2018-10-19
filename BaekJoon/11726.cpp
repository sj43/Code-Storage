#include<bits/stdc++.h>
using namespace std;
int main(){
  int N;
  cin>>N;
  int d[1001] = {0,};
  d[1] = 1;
  d[2] = 2;
  for(int i=3;i<=N;i++){
    d[i] = (d[i-2]+d[i-1])%10007;
  }
  cout<<d[N]<<endl;
  return 0;
}
