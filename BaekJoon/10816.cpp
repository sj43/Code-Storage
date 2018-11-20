// using multiset. it timeed out.
//
// #include<bits/stdc++.h>
// using namespace std;
// int main(){
//   ios::sync_with_stdio(false);
//   cin.tie(NULL);
//   cout.tie(NULL);
//   int N, M, temp;
//   multiset<int> mults;
//   cin>>N;
//   for(int i=0;i<N;i++){
//     cin>>temp;
//     mults.insert(temp);
//   }
//   cin>>M;
//   for(int i=0;i<M;i++){
//     int c;
//     cin>>c;
//     cout<<mults.count(c)<<' ';
//   }cout<<'\n';
//   return 0;
// }
//
//

// using unordered_map. this passed.

// #include<bits/stdc++.h>
// using namespace std;
// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);
//     int N, M, temp;
//     unordered_map<int, int> m;
//     cin>>N;
//     for(int i=0;i<N;i++){
//       cin>>temp;
//       m[temp]++;
//     }
//     cin>>M;
//     for(int i=0;i<M;i++){
//       cin>>temp;
//       cout<<m[temp]<<' ';
//     }
//   return 0;
// }


// using binary search, recursion. this timed out as well :(
//
// #include <stdio.h>
// #include <algorithm>
// using namespace std;
// int a[500001];
// int N, M, temp;
// int twosearch(int left, int right, int cnt, int num){
//   int mid = (left+right)/2;
//   if(left>right) return cnt;
//   else{
//     if(a[mid] > num) return twosearch(left, mid-1, cnt, num);
//     else if(a[mid] < num) return twosearch(mid+1, right, cnt, num);
//     else return twosearch(left, mid-1, cnt, num) + twosearch(mid+1, right, cnt, num) + 1;
//   }
// }
// int main(){
//   scanf("%d",&N);
//   for(int i=0;i<N;i++){
//     scanf("%d",&a[i]);
//   }
//   sort(a,a+N);
//   scanf("%d",&M);
//   for(int i=0;i<M;i++){
//     scanf("%d",&temp);
//     printf("%d ",twosearch(0, N-1, 0, temp));
//   }printf("\n");
//   return 0;
// }
