#include<bits/stdc++.h>
using namespace std;
int main(){
  long N;
  long sum=0;
  cin>>N;
  long x;
  for(int i=0;i<N*N;i++){
    cin>>x;
    sum+=x;
  }
  cout<<sum<<endl;
  return 0;
}
