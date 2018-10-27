#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin>>n;
  vector<int> A;
  for(int i=0;i<n;i++){
    int temp;
    cin>>temp;
    A.push_back(temp);
  }
  sort(A.begin(),A.end());
  int twomax = max(A[0]*A[1], A[n-1]*A[n-2]);
  int threemax = max(A[0]*A[1]*A[n-1], A[n-1]*A[n-2]*A[n-3]);
  cout<< max(twomax,threemax)<<endl;
  return 0;
}
