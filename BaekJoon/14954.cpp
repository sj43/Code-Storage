#include<bits/stdc++.h>
using namespace std;
vector<int> v;
void happyNumber(int n){
  if(n==1){
    cout<<"HAPPY"<<endl;
    return;
  }
  for(int i=0;i<v.size();i++){
    if(n==v[i]){
      cout<<"UNHAPPY"<<endl;
      return;
    }
  }
  v.push_back(n);
  int copy = n;
  int result = 0;
  while(copy){
    result += (copy%10)*(copy%10);
    copy /= 10;
  }
  happyNumber(result);
}

int main(){
  int n;
  cin>>n;
  happyNumber(n);
  return 0;
}
