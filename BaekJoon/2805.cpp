#include<bits/stdc++.h>
using namespace std;
long long N, M, sum, Max, result;
long long a[1000001];

void binarySearch(){
  long long low = 0;
  long long high = Max;
  while(low<=high){
    sum=0;
    long long mid = (low+high)/2;
    // cout<<"low: "<<low<<" high: "<<high<<" mid: "<<mid<<'\n';
    for(int i=0; i<N;i++){
      if(mid < a[i]) sum += a[i]-mid;
    }
    // cout<<"sum: "<<sum<<'\n';
    if(sum >= M){
      if(result < mid){
        result = mid;
      }
      low = mid+1;
    }else high = mid-1;
  }
  cout<<result<<'\n';
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin>>N>>M;
  for(int i=0;i<N;i++){
    cin>>a[i];
    if(Max < a[i]) Max = a[i];
  }
  binarySearch();
  return 0;
}
