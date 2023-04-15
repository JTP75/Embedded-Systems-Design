#include <iostream>

#include <stdio.h>
#include <pthread.h>
#include <sched.h>
#include <unistd.h>
using namespace std;

static int tx_count_initial = 1000;
int tx_count = tx_count_initial;
pthread_mutex_t lock;
pthread_mutexattr_t attrs;

void* tx_machine0(void*);
void* tx_machine1(void*);
int get_rt_priority();

int main (int argc, char **argv) {
    pthread_t t0,t1;

    pthread_mutexattr_setprotocol(&attrs, PTHREAD_PRIO_INHERIT);
    pthread_mutex_init(&lock, &attrs);

    pthread_create(&t0, NULL, tx_machine0, NULL);
    pthread_create(&t1, NULL, tx_machine1, NULL);

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);

    return EXIT_SUCCESS;
}


void* tx_machine0(void*) {
    for (int i=0; i<tx_count_initial; i++) {
        pthread_mutex_lock(&lock);
        if (tx_count>0)
            cout << "m0: p = " << get_rt_priority() << ".\t" << --tx_count << " tickets remain.\n";
        pthread_mutex_unlock(&lock);
    } return (void*)0;
}
void* tx_machine1(void*) {
    for (int i=0; i<tx_count_initial; i++) {
        pthread_mutex_lock(&lock);
        if (tx_count>0)
            cout << "m1: p = " << get_rt_priority() << ".\t" << --tx_count << " tickets remain.\n";
        pthread_mutex_unlock(&lock);
    } return (void*)0;
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