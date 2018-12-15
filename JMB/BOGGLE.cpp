// This code (standard recursion) timed out. Need to solve with dynamic programming to pass.
#include<bits/stdc++.h>
using namespace std;
int c;
char board[5][5];
int n;
string s = "";
const int dx[] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dy[] = {-1, 0, 1, -1, 0, 1, -1, 1};
bool boggle(int y, int x, const string& word){
  if (x<0 || y<0 || x>4 || y>4) return false;
  if (board[y][x] != word[0]) return false;
  if (word.size() == 1) return true;
  for(int i = 0; i<8;++i){
    int y_next = y + dy[i];
    int x_next = x + dx[i];
    if(boggle(y_next, x_next, word.substr(1))) return true;
  }
  return false;
}
int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin>>c;
  for(int i=0;i<5;i++){
    cin>>board[i];
  }
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>s;
    bool alreadyfound = false;
    for(int j=0;j<5 && !alreadyfound;j++){
      for(int k=0;k<5 && !alreadyfound;k++){
        if(boggle(j, k, s)){
          cout<<s<<" YES\n";
          alreadyfound = true;
          break;
        }
      }
    }if(!alreadyfound) cout<<s<<" NO\n";
  }
  return 0;
}
