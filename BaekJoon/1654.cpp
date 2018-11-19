#include<bits/stdc++.h>
using namespace std;
int K,N;
long M;
long ans, Max;
long low, high;
long a[10001];
int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin>>K;
  cin>>N;
  for(int i=0;i<K;i++){
    cin>>a[i];
    if(M < a[i]) M = a[i];
  }
  low = 0;
  high = M;
  while(low<=high){
    ans = 0;
    long mid = (low+high+1)/2;
    for(int i=0;i<K;i++){
      if(a[i]/mid > 0) ans += a[i]/mid;
    }
    if(ans >= N){
      if(Max < mid) Max = mid;
      low = mid + 1;
    }else{
      high = mid - 1;
    }
  }
  cout<<Max<<'\n';
  return 0;
}
