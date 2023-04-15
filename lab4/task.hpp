#ifndef _TASK_HPP_
#define _TASK_HPP_

class Task{
	public:
		std::string name;
		int prd;
		int dur;
		int ctr;
		bool done;
		Task(int p, int d, std::string name){
			this->name = name;
			this->prd = p;
			this->dur = d;
			this->ctr = 0;
			this->done = true;
		}
	       	void tick(int t){
			if(--this->ctr <= 0)
				this->done = true;
		}	
		float ratio(){
			return (float)this->dur / this->prd;
		}
		int restart(){
			if(!this->done) return -1;
			this->ctr = this->dur;
			this->done = false;
			return 0;
		}
};

#endif
