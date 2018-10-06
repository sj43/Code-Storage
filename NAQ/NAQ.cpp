#include<iostream>
using namespace std;
int gcd3(int a, int b)
{
    return (a % b == 0 ? b : gcd3(b,a%b));
}
int main(){
    int p,q,s;
    cin>>p>>q>>s;
    if(p>q){
        int temp = p;
        p = q;
        q = temp;
    }
    if(p==1 && q==1) cout<<"yes\n";
    else if(p==1){
        if(s>=q) cout<<"yes\n";
        else cout<<"no\n";
    }
    else if(p==q){
        if(s>=q) cout<<"yes\n";
        else cout<<"no\n";
    }
    else if(q%p==0){
        if(s>=q) cout<<"yes\n";
        else cout<<"no\n";
    }
    else{
        int a = gcd3(p,q);
        if(s>= (p*q)/a) cout<<"yes\n";
        else cout<<"no\n";
    }


    // if(p==q && p<=s){
    //     cout<<"yes\n";
    // }
    // if(p==1 || q==1){
    //     if(p==1 && q<=s) cout<<"yes\n";
    //     else if(q==1 && p<=s) cout<<"yes\n";
    //     else cout<<"no\n";
    // }
    // if(p%q==0 || q%p==0){
    //     if(p%q==0 && p<=s) cout<<"yes\n";
    //     else if(q%p==0 && q<=s) cout<<"yes\n";
    //     else cout<<"no\n";
    // }
    // else if(p*q<=s) cout<<"yes\n";
    // else{
    //   cout<<"no\n";
    // }
    return 0;
}
