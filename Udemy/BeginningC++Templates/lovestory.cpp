#include<bits/stdc++.h>
using namespace std;
int T, N;
long long P;
long long A[1005];


int main(){
  int i,j,k;
  cin>>T;
  for(int _=0;_<T;++_){
    cin>>N;
    for(int i=1;i<=N;i++){
      cin>>A[i];
    }
    cin>>P;

    sort(A + 1, A + N + 1);

    bool found = false;

    for(i=1;i<=N;i++){
      for(j=i+1;j<=N;j++){
        int lo = j+1;
        int hi = N;
        while(lo<=hi && !found){
          int mid = (lo+hi)/2;
          if (A[mid] == P - A[i] - A[j]){
            found = true; break;
          }
          else if (A[mid] > P - A[i] - A[j]) hi = mid - 1;
          else lo = mid + 1;
        }
        if(found) break;
      }
      if(found) break;
    }
    if(found) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
  }
  return 0;
}
