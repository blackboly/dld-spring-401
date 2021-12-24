#include<iostream>
using namespace std;

int IS_CS(int a ){
    int i = 0;
    while(true){
        int b = i*i + (i-1)*(i-1);
        if(a == b){
            return 1;
        }
        else if(b>a){
            return 0;
        }
        i++;
    }
    return 1;
}

int main(){
    int a;
    cin>>a;
    if(IS_CS(a)){
        cout<<"YES"<<endl;
    }
    else{
        cout<<"NO"<<endl;
    }
}