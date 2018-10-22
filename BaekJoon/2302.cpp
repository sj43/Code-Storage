#include<bits/stdc++.h>
using namespace std;
int d[41];
int main(){
  int N;
  cin>>N;
  d[0] = 1;
  d[1] = 1;
  for(int i=2;i<=40;i++){
    d[i] = d[i-2]+d[i-1];
  }
  int M;
  cin>>M;
  vector<int> a;
  a.push_back(0);
  int gojung;
  for(int i=0;i<M;i++){
    cin>>gojung;
    a.push_back(gojung);
  }
  a.push_back(N+1);
  long long ans = 1;
  for(int i=1;i<a.size();i++){
    ans *= d[a[i] - a[i-1] - 1];
  }
  cout<<ans<<'\n';
  return 0;
}
