#include<bits/stdc++.h>
using namespace std;
int d[12];
int main(){
  int N;
  int n;
  cin>>N;
  for(int _=0;_<N;_++){
    cin>>n;
    d[1] = 1;
    d[2] = 2;
    d[3] = 4;
    d[4] = 7;
    for(int i=5; i<=n;i++){
      d[i] = d[i-1]+d[i-2]+d[i-3];
    }
    cout<<d[n]<<endl;
  }
}
