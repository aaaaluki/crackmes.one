#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	// *(char *)(argv[1] + 4) == '@'
	
	char pass = *(char *)(argv[1] + 4);
	printf("Password = %c\n", pass);
	exit(0);
}
