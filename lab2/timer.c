#include <stdio.h>
#include <sys/time.h>
#include <signal.h>

void timer_handler(int signum){
    static int counter = 0;
    struct timeval ts;

    counter += 1;
    gettimeofday(&ts, NULL);
    printf("%d.%06d: timer expired %d times\n", ts.tv_sec, ts.tv_usec, counter);
}

int main(void){
    struct sigaction sa;
    struct itimerval timer;

    int begin = 0;
    int interval = 500000;
    
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = &timer_handler;
    sigaction(SIGVTALRM, &sa, NULL);

    timer.it_value.tv_sec = begin;
    timer.it_value.tv_usec = begin + interval;

    timer.it_interval.tv_sec = begin;
    timer.it_interval.tv_usec = begin + interval;

    setitimer(ITIMER_VIRTUAL, &timer, NULL);
    while(1);

    return 0;
}