#include <iostream>
#include <iomanip>
#include <time.h>

#define _CACHE_LINE_SIZE_ 64
#define N 1024
#define ITERS 1

float A[N][N];
float B[N][N];
float C[N][N];
int floats_per_line = _CACHE_LINE_SIZE_ / 4;

void matmul(float A[N][N], float B[N][N], float C[N][N]);

/**
 * 
 * @note    executable is blink_VFM.exe
 *  build       g++ matmul.cpp -o matmul
 *  run         ./matmul
 * 
 */

int main(int argc, char** argv){
    srand(time(NULL));
    float dt=0;
    clock_t t0;
    for(int iter=0; iter<ITERS; iter++){

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                A[i][j] = 10*rand()/(float) RAND_MAX;
                B[i][j] = 10*rand()/(float) RAND_MAX;
                C[i][j] = 0;
            }
        }

        t0 = clock();
        matmul(A,B,C);
        dt += (float)(clock()-t0)/CLOCKS_PER_SEC;
    }
    dt /= ITERS;

    std::cout << "matmul runtime mean (" << ITERS << " iters) = " << std::setprecision(4) << dt << "s" << std::endl;
    return EXIT_SUCCESS;
}


void matmul(float A[N][N], float B[N][N], float C[N][N]){
    for(int i=0; i<N; i++)                                                  // N iters
        for(int k=0; k<N; k++)                                              // N iters
            for(int j=0; j<N; j += floats_per_line)                         // N/16 iters
                for(int j_c=0; j_c<floats_per_line; j_c++)                  // 16 iters
                    C[i][j+j_c] += A[i][k] * B[k][j+j_c];                   //      = N**3
    return;
}
