#include <iostream>
#include <stdio.h>

using namespace std;

int GetInt(){
	int x;
	try	{std::cin>>x;}
	catch(std::exception){return GetInt();}
	return x;
}

float GetFloat(){
	float x;
	try	{std::cin>>x;}
	catch(std::exception){return GetInt();}
	return x;
}

char* GetStr(){
	char* x;
	std::cin>>x;
	return x;
}

int rint(int min,int max){
	// random int (min & max included)
	srand(time(0));
	max++;
	return (rand() % (max-min))+min;
}

int BiggerInt(int a,int b){
	if (a > b){
		return a;
	} else {
		return b;
	}
}

int SmallerInt(int a,int b){
	if (a < b){
		return a;
	} else {
		return b;
	}
}

void pos(int x, int y){
	printf("\x1b[%i;%iH\n",y,x);
}

auto format = sprintf;
