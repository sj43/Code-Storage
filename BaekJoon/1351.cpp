#include<bits/stdc++.h>
using namespace std;
map<long long, long long> d;
long long n,p,q;
long long go(long long i){
  if(i==0){
    return 1;
  }else if(d.count(i)>0){
    return d[i];
  }else{
    return d[i] = go(i/p)+go(i/q);
  }
}
int main(){
  cin>>n>>p>>q;
  cout<<go(n)<<"\n";
  return 0;
}
