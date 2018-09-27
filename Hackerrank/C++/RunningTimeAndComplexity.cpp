#include<bits/stdc++.h>
using namespace std;
bool isItPrime(int n){
        if(n==1) return false;
        if(n==2) return true;
        if(n%2==0) return false;
        for(int i=3;i*i<n;i+=2){
            if(n%i==0){
              return false;
            }
        }
        return true;
}
int main(){
    int T;
    cin>>T;
    int n;
    for(int i=0;i<T;i++){
        cin>>n;
        bool tf = isItPrime(n);
        cout<<(tf?("Prime\n"):("Not Prime\n"));
    }
}
