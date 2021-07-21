#include <iostream>
#include "mylib.cpp"

using namespace std;


int main(int argc, const char* argv[]){
	int num1 = 1, num2 = 6, min, max;

	if (argc > 1){
		num1 = atoi(argv[1]);
		if (argc > 2){
			num2 = atoi(argv[2]);
		}
	}



	min = SmallerInt(num1,num2);
	max = BiggerInt(num1,num2);

	if (min==max){

		cout<<min<<endl;

	} else{
		cout<<rint(min,max)<<endl;
	}

	return 0;
}