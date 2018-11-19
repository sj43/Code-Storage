#include<bits/stdc++.h>
using namespace std;
vector<int> DN;

int binarysearch(int n, int key){
  int start = 0;
  int end = n-1;
  int mid;
  while(end >= start){
    mid = (start+end)/2;
    if(key == DN[mid]) return mid;
    else if(key < DN[mid]) end = mid-1;
    else start = mid+1;
  }
  return -1;
}

int main(){
  cin.tie(NULL);
  ios_base::sync_with_stdio(false);
  int N, M, temp;
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>temp;
    DN.push_back(temp);
  }
  sort(DN.begin(),DN.end());

  cin>>M;
  for(int i=0;i<M;i++){
    cin>>temp;
    int x = binarysearch(N, temp);
    if (x==-1){
      cout<<0<<'\n';
    }else{
      cout<<1<<'\n';
    }
  }
  return 0;
}
