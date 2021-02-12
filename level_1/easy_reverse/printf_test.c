#include <stdlib.h>
#include <stdio.h>

main (int argc, char* argv[]) {
	// argc is the number of arguments
	// argv[] is an array of arguments
	// Note: argv[0] is the filename
	printf("Usage: %s <password>\n", argv[1]);
	exit(0);
}
