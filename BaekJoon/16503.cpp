#include<bits/stdc++.h>
using namespace std;
int calc(int a, char p, int b){
  if(p=='+') return a+b;
  else if(p=='-') return a-b;
  else if(p=='*') return a*b;
  else return a/b;
}
int main(){
  int a,b,c;
  char p, q;
  cin>>a>>p>>b>>q>>c;
  int first_case = calc(calc(a,p,b), q, c);
  int second_case = calc(a, p, calc(b,q,c));
  cout<<min(first_case, second_case)<<endl<<max(first_case, second_case)<<endl;
}
