#include <stdio.h>

/* 0/1 knapsack */

int max(int a, int b){
  if (a >=b ) return a;
  else return b;
}

int main(){
  int S, N;
  int i, j;
  int b, w;
  scanf("%d %d", &S, &N);

  int B[N+1][S+1];

  for (i=0; i<=N; i++){
    B[i][0]=0;
  }
  for (j=0; j<=S; j++){
    B[0][j]=0;
  }

  for(i=1; i<=N; i++){
    scanf("%d %d", &w, &b);
    for(j=1; j<=S; j++){
      if (w > j){
        B[i][j] = B[i-1][j];
      } 
      else{
        B[i][j] = max(B[i-1][j], b + B[i-1][j-w]);
      }
    }
  }
 
  printf("%d\n", B[N][S]);
  return 0;
}
