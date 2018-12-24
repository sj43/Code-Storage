#include<bits/stdc++.h>
using namespace std;
int C;
const int INF = 9999, SWITCHES = 10, CLOCKS = 16;
const char linked[SWITCHES][CLOCKS + 1] = {
  "***.............",
  "...*...*.*.*....",
  "....*.....*...**",
  "*...****........",
  "......***.*.*...",
  "*.*...........**",
  "...*..........**",
  "....**.*......**",
  ".*****..........",
  "...***...*...*.."};

bool areAligned(const vector<int> & clocks){
  for(int i=0;i<CLOCKS;i++){
    if(clocks[i] != 12) return false;
  }
  return true;
}

void push(vector<int> & clocks, int swtch){
  for(int i=0; i<CLOCKS;i++){
    if(linked[swtch][i] == '*'){
      clocks[i] += 3;
      if(clocks[i] == 15) clocks[i] = 3;
    }
  }
}

int solve(vector<int> & clocks, int swtch){
  if(swtch == SWITCHES) return areAligned(clocks) ? 0 : INF;
  int ret = INF;
  for(int i=0; i<4; i++){
    ret = min(ret, i + solve(clocks, swtch + 1));
    push(clocks, swtch);
  }
  return ret;
}

int main(){
  cin>>C;
  while(C--){
    vector<int> clocks;
    int temp;
    for(int i=0;i<16;i++){
      cin>>temp;
      clocks.push_back(temp);
    }
    int ans = solve(clocks, 0);
    if(ans == INF) cout<<-1<<'\n';
    else cout<<ans<<'\n';
  }
  return 0;
}
