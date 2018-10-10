#include<iostream>
#include<string>
#include<algorithm>
#include<array>
using namespace std;


void rotateClockwise(int ** M, int N){
  for(int i=0;i<N/2;i++){
    for(int j=i;j<N-i-1;j++){
      int temp = M[i][j];
      M[i][j] = M[j][N-i-1];
      M[j][N-i-1] = M[N-i-1][N-j-1];
      M[N-i-1][N-j-1] = M[N-j-1][i];
      M[N-j-1][i] = temp;
    }
  }
}

void printMatrix(int** M, int N){
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cout<<M[i][j]<<" ";
    }cout<<"\n";
  }cout<<"\n";
}

int main(){
  int N;
  cin>>N;
  int** matrix = new int*[N];
  for(int i=0;i<N;i++){
    matrix[i] = new int[N];
  }
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      cin>>matrix[i][j];
    }
  }
  rotateClockwise(matrix,N);
  printMatrix(matrix,N);

  for(int i=0;i<N;i++){
    delete matrix[i];
  }delete matrix;

  return 0;
}
