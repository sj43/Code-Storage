#include<bits/stdc++.h>
using namespace std;
int d[1001];
int a[1001];
int main(){
  int N;
  cin>>N;
  for(int i=1;i<=N;i++){
    cin>>a[i];
  }
  for(int i=1;i<=N;i++){
    d[i] = d[i-1];
    int max = a[i];
    int min = a[i];
    for(int j=i-1; j>=1; j--){
      if(max < a[j]) max = a[j];
      if(min > a[j]) min = a[j];
      int cur = d[j-1] + (max-min);
      if(d[i] < cur){
        d[i] = cur;
      }
    }
  }
  cout<<d[N]<<endl;
  return 0;
}
