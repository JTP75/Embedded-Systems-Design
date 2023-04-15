#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

class Task{
	
}

int main(int argc, char **argv){
	
	struct task A = {25,10,'A'};
	struct task B = {60,15,'B'};
	int simulation_dur = 200;	

	if(argc==5){
		A.period = atoi(argv[1]);
		B.period = atoi(argv[3]);
		A.duration = atoi(argv[2]);
		B.duration = atoi(argv[4]);
	}

	printf("--------------------------------------\n");
	printf("EDF Scheduling Algorithm\n");
	printf("--------------------------------------\n");
	printf("\n\t\tA\tB\nperiod\t\t%d\t%d\nduration\t%d\t%d\n\n",
		A.period, B.period, A.duration, B.duration);
	printf("Beginning simulation...\n\n");
	




	printf("\nSimulation complete.\n\n");
	return 0;

}
