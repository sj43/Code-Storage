#include<bits/stdc++.h>
using namespace std;
int main(){
  int N,M, Max=0;
  int a[10001];
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>a[i];
    if(Max < a[i]) Max = a[i];
  }
  cin>>M;
  int low = 0;
  int high = Max;
  int total, result=0;
  while(low <= high){
    total = 0;
    int mid = (low+high)/2;
    for(int i=0;i<N;i++){
      if(a[i]>=mid){total += mid;}
      else{total+=a[i];}
    }
    if(total>M){
      high = mid-1;
    }else{
      if(result < mid) result = mid;
      low = mid+1;
    }
  }
  cout<<result<<'\n';
  return 0;
}
