// gcc -z execstack -fno-stack-protector -o chall chall.c
#include <stdio.h>
#include <unistd.h>

int main(){
    char buf[16] = {0};
    setvbuf(stdout, NULL, _IOLBF, 0);
    printf("Welcome to SlashRoot!\n");
    printf("Kamu tau ini [%p] ?\n", buf);
    printf("beri tau aku! \n");
    read(0, buf, 36);
    return 0;
}
