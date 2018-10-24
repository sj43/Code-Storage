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
  d[1] = 1;
  int max = 1;
  for(int i=2;i<=N;i++){
    d[i]=1;
    for(int j=1;j<=i;j++){
      if(a[i]>a[j] && d[i]<d[j]+1){
        d[i] = d[j]+1;
      }
      if(d[i] > max){
        max = d[i];
      }
    }
  }
  cout<<max<<endl;
  return 0;
}
