#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin>>n;
  vector<int> c(n,0);
  vector<int> d(n,0);
  int totmax = -1000;
  for(int i=0;i<n;i++){
    cin>>c[i];
  }
  d[0] = c[0];
  for(int i=1;i<n;i++){
    d[i] = max(d[i-1]+c[i], c[i]);
    totmax = max(totmax,d[i]);
  }
  totmax = max(totmax, d[0]);
  cout<<totmax<<endl;
  return 0;
}










// int main(){
//   int N,n;
//   cin>>N;
//   int totmax = -1001;
//   int relmax = -1001;
//   bool passed = false;
//   for(int _=0;_<N;_++){
//     cin>>n;
//     if(passed) relmax=n;
//     else if(n<0){
//       relmax=n;
//       passed=true;
//       if(relmax>totmax) totmax = relmax;
//       continue;
//     }
//     else{
//       if(relmax==-1001) relmax=n;
//       else relmax+=n;
//     }
//     if(relmax>totmax) totmax = relmax;
//     passed = false;
//   }
//   cout<<totmax<<endl;
// }
