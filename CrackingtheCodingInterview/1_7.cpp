#include<iostream>
#include<string>
using namespace std;
int main(){
  string a = "abc";
  string b = "def";
  string c = a+b;
  string d = a.append(b);
  cout<<c<<endl;
  cout<<d<<endl;
}
