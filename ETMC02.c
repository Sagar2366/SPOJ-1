#include <stdio.h>
#define MAXLENGTH 101
int matrix[MAXLENGTH][MAXLENGTH];
int main(){
  int T, S, C, Sj;
  int i,j,row_first,start;
  int flag=1;
  int saved_i=0;

  scanf("%d", &T);
  while (T--){
  
    /* obtain values for S and C */
    scanf("%d %d", &S, &C);
    
    if (S==1){
      scanf("%d", &j);
      while(C--){
        printf("%d ", j);
      }
      printf("\n");
    }
    
    else {
		  /* obtain the pattern so far for first S numbers */
			for(j=0;j<S;j++){
				scanf("%d", &matrix[0][j]);
			}
	 
		  /* create the row-wise difference matrix */
		  Sj=S;
			for(i=1;i<S;i++){
				--Sj;
				for(j=0;j<Sj;j++){
				  matrix[i][j] = matrix[i-1][j+1] - matrix[i-1][j];
				}
			  row_first = matrix[i][0];
			  for(j=0;j<Sj;j++){
			    if(matrix[i][j] != row_first) { flag=0; break;}
			    else flag =1;
			  }
				if (flag == 1){ saved_i = i; break; }
			}
		
		
			/* Create the other missing values */
			start=j+1;
			i=saved_i;
			for(j=j;j<S+C-i;j++){
				matrix[i][j]=matrix[i][j-1];
			}

		  for(i=saved_i-1;i>=0;i--){
		    for(j=start;j<=S+C-i;j++){
		      matrix[i][j] = matrix[i+1][j-1] + matrix[i][j-1];
		    } 
		    ++start;
		  }


			for(i=S;i<S+C;i++){ 
				printf("%d ", matrix[0][i]);	
			}
			printf("\n");
    
    }
    

	}//whileT--
  return 0;
  
}
