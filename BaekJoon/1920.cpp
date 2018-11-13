#include<bits/stdc++.h>
using namespace std;
vector<int> DN;

int binarysearch(int lo, int hi, int m){
  cout<<"binary search called"<<endl;
  int mid = (lo+hi)/2;
  if(lo>hi) return -1;
  if(m < DN[mid]) return binarysearch(mid,hi,m);
  else if(m > DN[mid]) return binarysearch(lo,mid,m);
  else return mid;
}
int main(){
  int N, M, temp;
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>temp;
    DN.push_back(temp);
  }
  sort(DN.begin(),DN.end());

  vector<int>::iterator it;
  for(it = DN.begin(); it!=DN.end(); ++it){
    cout<<*it<<' ';
  }cout<<endl;

  cin>>M;
  for(int i=0;i<M;i++){
    cin>>temp;
    int x = binarysearch(0,N,temp);
    cout<<"binary search end"<<endl;
    if (x==-1){
      cout<<0<<endl;
    }else{
      cout<<1<<endl;
    }
  }
  return 0;
}
