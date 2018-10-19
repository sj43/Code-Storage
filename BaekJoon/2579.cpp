#include<bits/stdc++.h>
using namespace std;
int d[301][2];
int main(){
  int N;
  cin>>N;
  int n;
  cin>>n;
  d[0][0] = 0;
  d[0][1] = n;
  cin>>n;
  d[1][0] = d[0][1];
  d[1][1] = d[0][1]+n;
  int prevN = n;
  for(int i=2;i<N;i++){
    cin>>n;
    d[i][0] = d[i-1][1];
		d[i][1] = max(d[i-2][0] + prevN, d[i-2][1]) + n;
    prevN = n;
  }
  cout<<d[N-1][1]<<endl;
  return 0;
}
