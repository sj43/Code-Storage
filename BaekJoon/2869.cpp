// using math

// #include <iostream>
//
// int main() {
//     int A, B, V, d;
//     scanf("%d %d %d", &A, &B, &V);
//     d = (V - A - 1) / (A - B) + 2;
//     printf("%d\n", d);
//
//     return 0;
// }


// using binary search

#include<bits/stdc++.h>
using namespace std;
int A,B,V;
const int INF = 1000000001;
long long binarySearch(){
    long long left = 0;
    long long right = V / (A-B) + 1;
    long long totalDay;
    long long result = INF;
    while(left <= right){
        totalDay = (left+right)/2;
        if (V <= totalDay * (A-B) + A){
            result = min(result, totalDay+1);
            right = totalDay - 1;
        }else{
            left = totalDay + 1;
        }
    }
    return result;
}
int main(){
    cin>>A>>B>>V;
    cout<<binarySearch()<<'\n';
    return 0;
}
