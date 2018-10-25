#include<bits/stdc++.h>
using namespace std;
int d[401][401][401];
int main(){
  int n;
  cin>>n;
  vector<int> a,b;
  a.push_back(0);
  b.push_back(0);
  for(int i=0;i<n;i++){
    int temp;
    cin>>temp;
    if(temp!=0) a.push_back(temp);
  }
  for(int i=0;i<n;i++){
    int  temp;
    cin>>temp;
    if(temp!=0) b.push_back(temp);
  }
  for(int k=1;k<=n;k++){
    for(int i=1;i<a.size();i++){
      for(int j=1;j<b.size();j++){
        if(i>k) continue;
        if(j>k) continue;
        int cur = d[k-1][i-1][j-1] + a[i]*b[j];
        if(j-1 >= 0 && k-1>=i) cur = max(cur, d[k-1][i][j-1]);
        if(i-1 >= 0 && k-1>=j) cur = max(cur, d[k-1][i-1][j]);
        d[k][i][j] = cur;
      }
    }
  }
  cout<<d[n][a.size()-1][b.size()-1]<<endl;
  return 0;
}
