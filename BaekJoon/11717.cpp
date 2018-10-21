#include<bits/stdc++.h>
using namespace std;
int main(){
  int d[1010] = {};
  int n;
  d[0] = 1; d[1] = 1;
  cin>>n;
  for(int i=2;i<=n;i++){
    d[i] = (d[i-1]+d[i-2]*2)%10007;
  }cout<<d[n]%10007<<endl;
}
