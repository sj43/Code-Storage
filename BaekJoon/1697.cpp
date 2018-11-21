#include<bits/stdc++.h>
using namespace std;
int N, K, cnt, Min=100001;
int visited[100001];
int main(){
  cin>>N>>K;
  queue<pair<int,int>> q;
  q.push(make_pair(N,0));
  while(!q.empty()){
    int cur_pos = q.front().first;
    int cur_sec = q.front().second;
    q.pop();
    if(cur_pos == K){
      if(cur_sec < Min) Min = cur_sec;
      break;
    }
    if(cur_pos > 0 && visited[cur_pos-1]==0){
      q.push(make_pair(cur_pos-1,cur_sec+1));
      visited[cur_pos-1] = 1;
    }
    if(cur_pos < 100000 && visited[cur_pos+1]==0){
      q.push(make_pair(cur_pos+1, cur_sec+1));
      visited[cur_pos+1] = 1;
    }
    if(cur_pos*2 <= 100000 && visited[cur_pos*2] == 0){
      q.push(make_pair(cur_pos*2, cur_sec+1));
      visited[cur_pos*2] = 1;
    }
  }
  cout<<Min<<'\n';
  return 0;
}
