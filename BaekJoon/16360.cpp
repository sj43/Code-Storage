#include<bits/stdc++.h>
using namespace std;
int main(){
  int n;
  cin>>n;
  cin.ignore();
  for(int _=0;_<n;_++){
    string str;
    getline(cin,str);
    int len_str = str.size();
    char ch = str[len_str-1];
    if (ch == 'a' ||ch == 'o' || ch == 'u'){
      str += "s";
    }
    else if(ch=='l' || ch == 'r' || ch=='v'){
      str += "es";
    }
    else if(ch == 't' || ch == 'w'){
      str += "as";
    }
    else if(ch == 'i' || ch == 'y'){
      str.pop_back();
      str += "ios";
    }
    else if(ch=='n'){
      str.pop_back();
      str += "anes";
    }
    else if(ch == 'e'){
      str.pop_back();
      if (str[len_str-2] == 'n'){
        str.pop_back();
        str += "anes";
      }
      else{
        str += "eus";
      }
    }
    else{
      str += "us";
    }
    cout<<str<<endl;
  }
  return 0;
}
