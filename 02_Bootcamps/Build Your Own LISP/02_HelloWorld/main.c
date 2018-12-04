#include <stdio.h>

typedef struct {
    float x;
    float y;
} point;

void hwn(int n) {
    for (int i = 0; i < n; i++) {
        puts("Hello, world!");
    }
}

int main(int argc, char** argv) {
    puts("Hello, world!");
    hwn(5);
    return 0;
}
