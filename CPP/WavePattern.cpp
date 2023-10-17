#include<iostream>
using namespace std;
int main(){
    int m,n;
    cout<<"Enter the number of rows and columns :";
    cin>>m>>n;
    int a[m][n];
    cout<<"Enter the values of the matrix : "<<endl;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            cin>>a[i][j];
        }
    }
    cout<<"The matrix in wave form is :"<<endl;
    for(int i=0;i<=m-1;i++){
        if(i%2==0){
            for(int j=0;j<n;j++){
                cout<<a[j][i]<<" ";
            }
        }
        else{
            for(int j=n-1;j>=0;j--){
                cout<<a[j][i]<<" ";
            }
        }
        cout<<endl;
    }
}