#include <iostream>
#include <stdio.h>
#include "mylib.cpp"

int main(int argc, char* argv[]){
	char buff[1000];
	int len = format(buff,"hi!, you are %dyo\n",15);
	char msg[len];


	cout<<msg;
}
