#include<bits/stdc++.h>
using namespace std;
int findTeam(vector<int> & vec, unordered_map<int,int>& counts){
  if(vec.size()<=2){
    return 1;
  }
  int max_f = vec.back();
  vec.pop_back();
  int max_s = vec.back();
  vec.pop_back();
  counts[max_f] -= 1;
  int count = counts[max_s];
  counts[max_s] -= 1;
  return (findTeam(vec,counts)*count)%1000000007;
}
int main(){
  int t,n,_in;
  cin>>t;
  vector<int> vec;
  for(int i=0;i<t;i++){
    vec.clear();
    cin>>n;
    for(int j=0;j<n;j++){
      cin>>_in;
      vec.push_back(_in);
    }
    sort(vec.begin(),vec.end());

    unordered_map<int, int> counts;
    for (auto v : vec)
    ++counts[v];
    int answer = findTeam(vec,counts);
    cout<<answer<<"\n";
  }
}
