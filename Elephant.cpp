#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	if(n%5 == 0){
		cout << n/5 << endl;
	}
	else{
		cout << (int)n/5 + 1 << endl;
	}
}