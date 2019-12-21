#include <stdio.h>
#include <time.h>
#include <sys/time.h>

void print_time_now()
{
	time_t curr_time;
	struct tm *nowtime;
	struct timeval tv;
	curr_time = time(NULL);
	nowtime =  localtime(&curr_time);
	gettimeofday(&tv, NULL);
	printf("%d-%d-%d %d:%d:%d.%ld\n", 1900+nowtime->tm_year, nowtime->tm_mon, nowtime->tm_mday,
			nowtime->tm_hour, nowtime->tm_min, nowtime->tm_sec, tv.tv_usec);
}

int main()
{
	print_time_now();
	return 0;
}
