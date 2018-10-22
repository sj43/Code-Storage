#include<bits/stdc++.h>
using namespace std;
int d[3001][3001];
string a;
string b;
int main(){
  int A,B,C;
  cin>>A>>B>>C;
  cin.ignore();
  getline(cin,a);
  getline(cin,b);
  int len_a = a.size();
  int len_b = b.size();
  for(int i=1; i<=len_a; i++){
    d[i][0] = B*i;
  }
  for(int i=1;i<=len_b;i++){
    d[0][i] = B*i;
  }
  for(int i=1;i<=len_a;i++){
    for(int j=1;j<=len_b;j++){
      if(a[i-1] == b[j-1]){
        d[i][j] = d[i-1][j-1]+A;
      }
      else{
        d[i][j] = max(max(d[i-1][j],d[i][j-1])+B,d[i-1][j-1]+C);
      }
    }
  }
  cout<<d[len_a][len_b]<<endl;
  return 0;
}
