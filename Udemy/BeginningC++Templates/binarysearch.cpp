#include<bits/stdc++.h>
using namespace std;

ifstream f("data.in");
ofstream g("data.out");

int A[1000], num_elements;

int binary_search(int x){
  int lo = 1;
  int hi = num_elements;
  int mid;

  while(lo <= hi){
    int mid = (lo + hi)/2;
    if(x == A[mid]) return mid;
    else if(x < A[mid]) hi = mid - 1;
    else lo = mid + 1;
  }
  return -1;
}

int main(){
  f >> num_elements;
  for (int i=0;i<num_elements;i++){
    f >> A[i];
  }
  g << "Index is: " << binary_search(6) << endl;
  return 0;
}
