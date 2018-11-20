#include<bits/stdc++.h>
using namespace std;
#define MAX_SIZE 101
int N,M;
char m[MAX_SIZE][MAX_SIZE];
bool visit[MAX_SIZE][MAX_SIZE];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int bfs(){
  queue<pair<pair<int,int>, int>> q;
  q.push(make_pair(make_pair(0,0),1));
  visit[0][0] = 1;
  while(!q.empty()){
    int x = q.front().first.second;
    int y = q.front().first.first;
    int z = q.front().second;
    q.pop();
    if(x==M-1 && y==N-1) return z;
    for(int i=0;i<4;i++){
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(nx<0 || ny<0 || nx>=M || ny>=N) continue;
      if(visit[ny][nx]==1) continue;
      if(m[ny][nx]!='1') continue;
      q.push(make_pair(make_pair(ny,nx),z+1));
      visit[ny][nx] = 1;
    }
  }
  return -1;
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> N >> M;
  for(int i=0; i<N; i++) {
    cin >> m[i];
  }
  cout << bfs();
  return 0;
}
