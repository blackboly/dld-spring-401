#include <iostream>  
using namespace std;  
int main()  
{  
    int a[10], n, i;    
    cout<<"Enter the number to convert: ";    
    cin>>n;    
    for(i=0; n>0; i++)    
    {    
    a[i]=n%2;    
    n= n/2;  
    }    
    int max = 0 , b = 0;
    for(int i=0; i <10; i++) {
        if(a[i] == 1){
            b++;
        }else{
            b = 0;
        }
        if(b>max) max=b;

    }
} 