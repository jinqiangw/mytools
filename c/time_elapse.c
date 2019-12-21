#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>

void print_eplase_time()
{
	struct timeval tstart, tend;
	double elapse_time;

	gettimeofday(&tstart, NULL);
	sleep(2);
	gettimeofday(&tend, NULL);
	elapse_time = 1000000*(tend.tv_sec-tstart.tv_sec)+tend.tv_usec-tstart.tv_usec;
	printf(" Time= %fs\n", elapse_time/1000000);
}

int main()
{
	print_eplase_time();
	return 0;
}

