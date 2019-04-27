#include<iostream>
using namespace std;

int A[101];

int sum_to_n(int N){
  A[1] = 1;
  A[2] = 2;
  A[3] = 4;
  for(int i=4;i<=N;i++){
    A[i] = A[i-1] + A[i-2] + A[i-3];
  }
  return A[N];
}

int main(){
  cout<<sum_to_n(5)<<endl;
  return 0;
}
