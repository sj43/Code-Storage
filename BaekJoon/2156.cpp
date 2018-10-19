#include<bits/stdc++.h>
using namespace std;
int d[10001];
int wine[10001];
int main(){
  int N;
  cin>>N;
  for(int i=1;i<=N;i++){
    scanf("%d",&wine[i]);
  }
  d[1] = wine[1];
  d[2] = wine[1] + wine[2];
  for(int i=3;i<=N;i++){
<<<<<<< HEAD
    d[i] = max(d[i-1],max(d[i-2]+wine[i],d[i-3]+wine[i-1]+wine[i]));
  }
  cout<<d[N]<<endl;
=======
    d[i] = max(d[i-1],max(d[i-2]+wine[i],d[i-3]+wine[i-2]+wine[i]));
  }
  cout<<d[N]<<endl;


  //
  // d[0][0] = 0;
  // d[0][1] = wine[0];
  // d[1][0] = d[0][1];
  // d[1][1] = d[0][1] + wine[1];
  // for(int i=2;i<N;i++){
  //   d[i][0] = d[i-1][1];
  //   d[i][1] = max(d[i-2][0]+wine[i-1],d[i-3][1])+wine[i];
  // }
  // cout<<max(d[N-1][0],d[N-1][1])<<endl;
>>>>>>> f811d93590db9f778b57139534b5f4ad84b0b197
  return 0;
}
