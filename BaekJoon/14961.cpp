#include<bits/stdc++.h>
using namespace std;
int A[10001];
int n;
int main(){
  cin>>n;
  for(int i=1;i<=n;i++){
    int temp;
    cin>>temp>>A[i];
  }
  for(int i=1;i<=n;i++){
    cout<<(A[i]==A[i+1] ? (n+1-i) : 1)<<" ";
  }cout<<endl;
  return 0;
}
