#include<iostream>
using namespace std;

int func1(int a){

    for(int i = 1; i <a; i++) {
        cout << i << " ";
    }
    for(int i = a; i > 0; i--) {
        cout << i << " ";
    }
    cout<<endl;
    return 1;
}

int main(){
    int n;
    cin>>n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < (n-i); j++){
            cout<<"  ";
        }
        func1(i);
    }
    for(int i = n; i> 0 ; i--){
        for(int j = 0; j < (n-i); j++){
            cout<<"  ";
        }
        func1(i);
    }
    cout<<endl;
}