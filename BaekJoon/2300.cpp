#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin>>n;
  vector<pair<int,int>> a(n+1);
  for(int i=1;i<=n;i++){
    cin>>a[i].first >> a[i].second;
    if(a[i].second<0) a[i].second*=-1;
  }
  sort(a.begin()+1,a.end());
  vector<int> d(n+1,100000000);
  d[0] = 0;
  for(int i=1; i<=n; i++){
    int up = 0;
    for(int j=i;j>=1; j--){
      up = max(up, a[j].second);
      int square = max(a[i].first - a[j].first, up*2);
      if(d[i] > d[j-1] + square) d[i] = d[j-1] + square;
    }
  }
  cout<<d[n]<<'\n';
  return 0;
}
