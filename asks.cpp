#include <iostream>
#include <stdio.h>
#include "mylib.cpp"
#include <cstring>

using namespace std;

struct Question{
	const char* msg;
	int points;
	char* RightAnswear;
};

int AskQuestion(Question ask){
	char* msg = "11";

	cout<<ask.msg<<endl;

	cin>>msg;

	if (strcmp(ask.RightAnswear,msg) == 0){
		return ask.points;
	} else{
		return 0;
	}
}

int main(int argc, char* argv[]){
	int points = 0;

	Question f;
	f.msg = "5 + 6";
	f.points = 2;
	f.RightAnswear = "11";

	points += AskQuestion(f);
	cout<<"points: "<<points<<"\n";
}
