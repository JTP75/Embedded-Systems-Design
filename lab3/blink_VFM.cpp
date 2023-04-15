#include <iostream>
#include <fstream>
#include <unistd.h>
#include <signal.h>
using namespace std;

void KBIHandle(int);
void fwrite(const char*, const char*);
ofstream fout;

/**
 * 
 * @note    executable is blink_VFM.exe
 *  build       g++ blink_VFM.cpp -o blink_VFM.exe
 *  run         sudo ./blink_VFM.exe
 * 
 */

int main(){
    signal(SIGINT, KBIHandle);
    
    while(true){
        fwrite("/sys/class/leds/led0/brightness","0");      // must run as root
        sleep(1);
        fwrite("/sys/class/leds/led0/brightness","255");    // must run as root
        sleep(1);
    }

    return EXIT_SUCCESS;
}


void KBIHandle(int signum){
    cout    << "\n"
            << "===================================\n"
            << "Program interrupted from terminal\n"
            << "Signal: " << signum << "\n" << endl;

    fwrite("/sys/class/leds/led0/brightness","0");

    exit(signum);
}
void fwrite(const char* path, const char* val){
    fout.open(path);
    fout << val;
    fout.close();
}