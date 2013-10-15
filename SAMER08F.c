#include <stdio.h>

/* Finds no of squares in an N*N grid */

int main(){
  int n;
  scanf("%d", &n);
  while(n){
    printf("%d\n", (n*(n+1)*(2*n+1))/6 );
    scanf("%d", &n);
  }
  return 0;
}
