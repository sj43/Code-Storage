#include<bits/stdc++.h>
using namespace std;
int main(){
  return 0;
  long long A,B,V;
  cin>>A>>B>>V;
  long long ans = V / (A-B);
  long long mod_ans = V % (A-B);
  if(mod_ans <= B) cout<<ans<<'\n';
  else cout<<ans+1<<'\n';
}
