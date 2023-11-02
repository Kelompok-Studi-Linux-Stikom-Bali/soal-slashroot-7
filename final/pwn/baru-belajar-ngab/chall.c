#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define FLAGSIZE 64
#define BUFSIZE 32

void win(){
  char buff[FLAGSIZE];
  FILE *f = fopen("flag.txt", "r");
  if(f == NULL){
    printf("%s", "Flag not found");
    exit(0);
  }

  fgets(buff, FLAGSIZE, f);
  printf(buff);
}

void vuln(){
  char c[BUFSIZE];
  printf("Masukan nama anda: ");
  gets(c);

  printf(c);
}

int main(int argc, char **argv){
  setvbuf(stdout, NULL, _IONBF, 0);
  char hehe[13];

  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  gets(hehe);
  if(!strcmp(hehe, "slashroot#7")){
    printf("Hai pemain satu, siap hadapi tantangan ini?\n");
    vuln();    
  }

  printf("\nBukannya aku tidak ingin, tapi...\n");
  return 0;
}
