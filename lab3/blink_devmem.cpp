#include <iostream>
#include <iomanip>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>

#define __GPIO_BASE       0xfe200000
#define __GPIO_GPFSEL     0x00000010
#define __GPIO_GPSET      0x00000020
#define __GPIO_GPCLR      0x0000002c
using namespace std;

void KBIHandle(int);

static uint8_t pin = 42;

/**
 * 
 * @note    executable is blink_devmem.exe
 *  build       g++ blink_devmem.cpp -o blink_devmem.exe
 *  run         sudo ./blink_devmem.exe
 * 
 */

int main(){
    
    int fd = open("/dev/mem", O_RDWR);
    void *GPIO_BASE = mmap(0, sysconf(_SC_PAGESIZE), PROT_READ | PROT_WRITE, MAP_SHARED, fd, __GPIO_BASE);
    close(fd);
    if(GPIO_BASE == MAP_FAILED){
        cout << "mmap call failed." << endl;
        exit(EXIT_FAILURE);
    }else{
        cout << "mmap call success! GPIO_BASE = " << GPIO_BASE << endl;
    }

    uint32_t *GPIO_SEL = (uint32_t*)(GPIO_BASE + __GPIO_GPFSEL);
    uint32_t *GPIO_SET = (uint32_t*)(GPIO_BASE + __GPIO_GPSET);
    uint32_t *GPIO_CLR = (uint32_t*)(GPIO_BASE + __GPIO_GPCLR);

    *GPIO_SEL &= ~(7<<(pin%10*3));
    *GPIO_SEL |= (1<<(pin%10*3));
    
    int i = 5;
    while(i-- > 0){
        *GPIO_SET = (uint32_t)(1<<(pin%32));
        sleep(1);
        *GPIO_CLR = (uint32_t)(1<<(pin%32));
        sleep(1);
    }

    if(munmap(GPIO_BASE, sysconf(_SC_PAGESIZE))==-1){
        cout << "munmap call failed." << endl;
        exit(EXIT_FAILURE);
    }else{
        cout << "munmap call success!" << endl;
    }

    exit(EXIT_SUCCESS);
}


