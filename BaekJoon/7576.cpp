#include<bits/stdc++.h>
using namespace std;

const int dx[] = {0,0,-1,1};
const int dy[] = {-1,1,0,0};

int n,m,a[1003][1003];
queue<pair<int, int>> que;

int main(){
  cin>>m>>n;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      cin>>a[i][j];
      if(a[i][j]==1) que.push({i,j});
    }
  }

  while(!que.empty()){
    auto now = que.front();
    que.pop();
    int x = now.first, y = now.second;
    for(int i=0; i<4; i++){
      int nx = x+dx[i];
      int ny = y+dy[i];
      if(ny<0 || ny>=m || nx<0 || nx>=n) continue;
      if(a[nx][ny]==0){
        a[nx][ny] = a[x][y]+1;
        que.push({nx,ny});
      }
    }
  }
  int mx = -1e9;
  for(int i=0; i<n; i++){
    for(int j=0; j<m; j++){
      if(!a[i][j]){
        cout<<-1<<endl;
        return 0;
      }
      mx = max(mx, a[i][j]);
    }
  }
  cout<<mx-1<<endl;
  return 0;
}
