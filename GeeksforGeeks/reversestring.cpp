#include<bits/stdc++.h>
using namespace std;

// simple swapping
void reverseStr(string& str){
  int n = str.length();
  for(int i=0;i<n/2;i++){
    swap(str[i], str[n-i-1]);
  }
}

// if the string is constant?
char* reverseConstStr(char const* str){
  int n = strlen(str);
  char* rev = new char[n+1];
  strcpy(rev, str);
  for(int i=0, j=n-1; i<j; i++, j--){
    swap(rev[i], rev[j]);
  }
  return rev;
}

int main(){
  string str = "geeksforgeeks";
  reverseStr(str);
  cout<<str<<endl;
  reverse(str.begin(),str.end());
  cout<<str<<endl;

  return 0;
}
