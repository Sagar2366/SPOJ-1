#include <stdio.h>
/* Given an encrypted string encrypted according to the rules
   defined in spoj/acode, finds out the possible number of 
   decryptions.
*/

int isWithin(int a, int b){  /* returns 1 if ab is a valid alphabet, 0 otherwise */
  int num;
  num = 10*a + b;
  if(num <= 26) return 1;
  else return 0;
}

int main(){
  
  char c;
  int i;		/* current digit  */
  int back=0;           /* previous digit */
  int pwback=1;         /* number of ways till one digit  back */
  int pwbackback=0;     /* number of ways till two digits back */
  int pw=1;             /* number of ways overall */

  while(1){
		c = getchar();
		if (c == '0') break;
		while (c != '\n'){
			i = c - '0';
			if (i){
				if (back == 0) pw = pwback;
				else if (isWithin(back,i)) pw = pwback + pwbackback;
				else pw = pwback;
			}
			// else account for 0s
			else{
  			  pw = pwbackback;
  			}
			back = i;
			pwbackback = pwback;
			pwback = pw;
			c = getchar();
		}
		printf("%d\n", pw);
		back=0;
		pwback=1;
		pwbackback=0;
		pw=1;
	}
  return 0;
}
