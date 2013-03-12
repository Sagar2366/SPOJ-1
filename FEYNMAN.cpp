#include<iostream>
using namespace std;
 
int feynman(int n){
    if (n==1) {return 1;}
    else {return n*n + feynman(n-1);}
}
 
int main(void){
    int t;
    while(1){
        cin>>t;
        if (t) {cout<<feynman(t)<<endl;}
        else {break;}
    }
    return 0;
}