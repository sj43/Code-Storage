#include<string>
#include<iostream>
using namespace std;


bool isOneAway(string s1, string s2){
  string a = (s1.length() < s2.length()) ? s1 : s2; // shorter string
  string b = (s1.length() >= s2.length()) ? s1 : s2; // longer string
  int len_a = a.length();
  int len_b = b.length();
  if(abs(len_a-len_b)>1){
    return false; // if length different over 1, return false
  }
  int index_a = 0;
  int index_b = 0;
  bool foundDiff = false;
  while(index_a < len_a && index_b < len_b){
      if(a[index_a]!=b[index_b]){
        if(foundDiff){
          return false;
        }
        foundDiff = true;
        if(len_a==len_b){
          index_a++;
          index_b++;
        }else{
          index_b++;
        }
      }else{
        index_a++;
        index_b++;
      }
  }
  return true;
}


int main(){
  string s1, s2;
  getline(cin,s1);
  getline(cin,s2);
  if(isOneAway(s1,s2)){
    cout<<"One edit away."<<endl;
  }else{
    cout<<"Not one edit away."<<endl;
  }
  return 0;
}
