#include<bits/stdc++.h>
using namespace std;
long long A[1000][1000];
int main(){
  int n,m;
  cin>>n>>m;
  long long total_sum = 0;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      cin>>A[i][j];
      total_sum += A[i][j];
    }
  }
  vector<long long*> I;
  for(int i=0;i<n;i++){
    auto row_max_index = max_element(A[i],A[i]+m);
    I.push_back(row_max_index);
  }
  for(int i=0;i<m;i++){
    long long col_max = A[0][i];
    long long* col_max_index = A[0]+i;
    for(int j=0;j<n;j++){
      if( A[j][i] > col_max){
         col_max = A[j][i];
         col_max_index = A[j]+i;
      }
    }
    auto it = find(I.begin(), I.end(), col_max_index);
    if(it == I.end()){
      I.push_back(col_max_index);
    }
  }
  for(int i=0;i<I.size();i++){
    total_sum -= *I[i];
  }
  cout<<total_sum<<"\n";
  return 0;
}
