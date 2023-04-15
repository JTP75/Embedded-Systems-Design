#include <iostream>
#include <stdio.h>

#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sched.h>


#define TASK_COMPLEXITY 1000000000

using namespace std;

pthread_mutex_t lock;
pthread_mutexattr_t attrs;

void* f0(void*);
void* f1(void*);
int get_rt_priority();

int main (int argc, char **argv) {

	static int pmax = sched_get_priority_max(SCHED_FIFO);	// 99
	static int pmin = sched_get_priority_min(SCHED_FIFO);	// 1
	
	pthread_t 	thread0, thread1;
	sched_param	param0, param1;
	sched_param	param_main;
	pthread_attr_t 	attr0, attr1;

	// create/init mutex
	pthread_mutexattr_setprotocol(&attrs, PTHREAD_PRIO_INHERIT);
	pthread_mutex_init(&lock, &attrs);

	// init attrs and parameters
	pthread_attr_init(&attr0);
	pthread_attr_init(&attr1);
	param0.sched_priority = 3;
	param1.sched_priority = 11;
	param_main.sched_priority = pmax;
	
	// set sched param for main
	pthread_setschedparam(pthread_self(), SCHED_FIFO, &param_main);

	// priority inheritance
	pthread_attr_setinheritsched(&attr0, PTHREAD_EXPLICIT_SCHED);
	pthread_attr_setinheritsched(&attr1, PTHREAD_EXPLICIT_SCHED);
	pthread_attr_setschedpolicy(&attr0, SCHED_FIFO);
	pthread_attr_setschedpolicy(&attr1, SCHED_FIFO);
	pthread_attr_setschedparam(&attr0, &param0);
	pthread_attr_setschedparam(&attr1, &param1);

	// create threads and assert stati
	int status0 = pthread_create(&thread0, &attr0, &f0, NULL);
	sleep(1);
	int status1 = pthread_create(&thread1, &attr1, &f1, NULL);

	// execution
	cout << "=================================\n" 
			<< "Beginning threading...\tMain priority is " << get_rt_priority() << "\n\n";
	pthread_join(thread0, NULL);
	pthread_join(thread1, NULL);
	cout << "\nThreading complete.\tMain priority is " << get_rt_priority() << "\n"
			<< "=================================";

	return EXIT_SUCCESS;
}

void* f0(void*) {
	cout << "task 0 begin\n"; 
	pthread_mutex_lock(&lock);
	cout << "f0 acquired lock.\n";
	for (int i=1; i<=TASK_COMPLEXITY; i++) 
	{
		if (i%100000000==0){
		cout << "\tf0 in lock: " << i << "/" << TASK_COMPLEXITY 
			<< ", priority is " << get_rt_priority() << "\n";}
	}
	pthread_mutex_unlock(&lock);
	cout << "f0 released lock.\n";
	return (void*) 0;
}
void* f1(void*) {
	cout << "task 1 begin\n"; 
	pthread_mutex_lock(&lock);
	cout << "f1 acquired lock.\n";
	for (int i=1; i<=TASK_COMPLEXITY; i++) {
		if (i%100000000 == 0) {
		cout << "\tf1 in lock: " << i << "/" << TASK_COMPLEXITY 
			<< ", priority is " << get_rt_priority() << "\n";}
	}
	pthread_mutex_unlock(&lock);
	cout << "f1 released lock.\n";
	
		
	return (void*) 0;
}
int get_rt_priority () {
	char str[50];
	sprintf(str, "/proc/%d/stat", gettid());
	FILE* fp = fopen(str, "r");
	for (int i=0; i<17; i++)
		fscanf(fp, "%s", str);
	int rtp = 0;
	fscanf(fp, "%d", &rtp);
	fclose(fp);
	return -(rtp+1);
}
