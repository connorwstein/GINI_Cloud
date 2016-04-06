#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){

	char *ip = "172.33.22.11";
	char result[20];
	memset(result, 0, sizeof(result));
	int len = strlen(ip);
int ip_index = len - 1;
int result_index = 0;
int current_field = 0;
printf("Result: ");
while(ip_index > 0){
//	printf("Result index %d\n", result_index);
	int index_dot = ip_index;
	// Find index of dot
	while(ip[index_dot] != '.' && index_dot >= 0) index_dot--;  
//	printf("Dot index %d", index_dot);
	// Copy each character before the dot to the result
	int k;
	for(k = 0; k < (ip_index - index_dot); k++){
		printf("%c", ip[index_dot + k + 1]);
		result[result_index++] = ip[index_dot + k + 1];
//		printf("result index %d\n", result_index);
	}
	if(result_index < len)
	result[result_index++] =  '.';
	ip_index = index_dot - 1;
//	result_index++;
}

	printf("\n\n%s\n", result);


}






