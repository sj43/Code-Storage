#include<bits/stdc++.h>
using namespace std;
int dfs(vector<vector<int>>& graph, vector<int>& neighbor, vector<int>& dp, int cur){
  if(dp[cur]) return dp[cur];
  int cnt = 1;
  for(auto& next : graph[cur]){
    if(neighbor[cur] < neighbor[next]){
      cnt = max(cnt, 1+dfs(graph,neighbor,dp,next));
    }
  }
  return dp[cur] = cnt;
}
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);
  int n,m; cin>>n>>m;
  vector<vector<int>> graph(n);
  vector<int> neighbor(n);
  vector<int> dp(n);
  for(int edge=0, i, j; edge<m;edge++){
    cin>>i>>j;
    graph[i].push_back(j);
    graph[j].push_back(i);
    neighbor[i]++;
    neighbor[j]++;
  }
  int biggest=0;
  for(int i=0;i<n;i++){
    biggest = max(biggest, dfs(graph,neighbor,dp,i));
  }
  cout<<biggest<<endl;
  return 0;
}
