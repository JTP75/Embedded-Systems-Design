#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct task{
	int period;
	int duration;
	char lbl;
};

int sched_check(struct task *tasks, int n);



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
	
	struct task tasks[] = {A,B};
	if(!sched_check(tasks,2)){
		printf("Tasks A & B are not schedulable.\n");
		return 1;
	}
	int dl_A=0, dl_B=0;
	int ctr_A=0, ctr_B=0;
	const struct task idle = {0,0,'i'};
	struct task curr;
	for(int t=0; t<simulation_dur; t++){

		// whichever task has the earliest deadline takes priority
		if(ctr_A==0 && t==dl_A){		// task A is complete
			dl_A += A.period;
			ctr_A = A.duration;
		}
		if(ctr_B==0 && t==dl_B){		// task B is complete
			dl_B += B.period;
			ctr_B = B.duration;
		}

		if(ctr_A==0 && ctr_B==0){
			curr = idle;
		}else if(dl_A <= dl_B){
			curr = A;
		}else{	
			curr = B;
		}
	
		if(curr.lbl=='A') --ctr_A;
		if(curr.lbl=='B') --ctr_B;

		printf("%d:\t%c\tdl_A=%d\tdl_B=%d\n",t,curr.lbl,dl_A,dl_B);
		
	}

	printf("\nSimulation complete.\n\n");
	return 0;

}

int sched_check(struct task *tasks, int n){
	float sum = 0;
	for(int i=0; i<n; i++)
		sum += (float)tasks[i].duration / (float)tasks[i].period;
	return sum <= 1; 
}

