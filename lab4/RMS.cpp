#include <iostream>
#include <math.h>
#include "task.hpp"
using namespace std;

int main (int argc, char **argv) {
	Task A = Task(25,10,"A");
	Task B = Task(60,15,"B");
	Task I = Task(0,0,"idle");

	if (argc==5) {
		A.prd = atoi(argv[1]);
		B.prd = atoi(argv[3]);
		A.dur = atoi(argv[2]);
		B.dur = atoi(argv[4]);
	}	

	cout 	<< "\n\t\tA\tB\nperiod\t\t" << A.prd
	       	<< "\t" << B.prd 
		<< "\nduration\t" << A.dur 
		<< "\t" << B.dur 
		<< std::endl;

	cout 	<< "Beginning RMS Scheduling Simulation...\n\n";


	int deadline_A=A.prd, deadline_B=B.prd;
	Task *current = nullptr;
	current = &I;

	for(int t=0; t<200; t++){
		
		if (A.done && current->name=="A")
			deadline_A += A.prd;
		if (B.done && current->name=="B")
			deadline_B += B.prd;

		cout << t << "\t";

		if (t%A.prd == 0){
			if (A.restart()==-1)
				cout << "(MISS) ";
		}
		if (t%B.prd == 0){
			if (B.restart()==-1)
				cout << "(MISS) ";
		}
			

		if (A.done && B.done) {
			current = &I;
		} else if (A.done && !B.done) {
			current = &B;
		} else if (!A.done && B.done) {
			current = &A;
		} else {
			if (A.prd < B.prd) 	current = &A;
			else			current = &B;
		}

		

		cout << current->name << "\n";
		current->tick(t);

	}
	
	cout << "\n\nSimulation complete.\n" << std::endl;

	return EXIT_SUCCESS;
}

