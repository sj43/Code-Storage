// #include<bits/stdc++.h>
// using namespace std;
// int C, N, L;
// int a[1001];
// int main(){
//   cin>>C;
//   while(C--){
//     cin>>N>>L;
//     for(int i=0;i<N;i++){
//       cin>>a[i];
//     }
//     double min = 123456789;
//     for(int i=L;i<=N;i++){
//       for(int j=0; j<=N-i; j++){
//         double sum = 0;
//         for(int k=j; k<i+j;k++){
//           sum += a[k];
//         }
//         sum /= i;
//         if(min > sum) min = sum;
//       }
//     }
//     printf("%.12f\n", min);
//   }
//   return 0;
// }

#include <iostream>
#include <cstdio>

using namespace std;

void solveCase()
{
    int N, L;
    int cost[1001];
    int sum[1001] = { 0 ,};
    double ans = 123456789;

    scanf("%d %d",&N, &L);

    for (int i = 1; i <= N; i++)
        scanf("%d",&cost[i]);

    //부분합을 빠르게 구하기 위해 index 0 부터 자기자신까지의 합을 저장해둔다.
    sum[0] = 0;
    for (int i = 1; i <= N; i++)
        sum[i] = sum[i - 1] + cost[i];

    //L개 이상이어야 하므로 j = i + L
    //sum[j] - sum[i] 이면 i + 1 번째 부터 ~ j번째 까지 대여. 즉 j - (i + 1) + 1 == j - i개 만큼 대여.
    for (int i = 0; i <= N; i++) {
        for (int j = i + L; j <= N; j++) {
            if (ans > ((double)sum[j] - sum[i]) / (j - i)) {
                ans = ((double)sum[j] - sum[i]) / (j - i);
            }
        }
    }

    printf("%.12f\n", ans);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--) {
        solveCase();
    }
    return 0;
}
