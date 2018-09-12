#include <iostream>
#include <deque>
using namespace std;

void printKMax(int arr[], int n, int k){
	int max_arr[n-k+1];
	int max=0;
	//Write your code here.
	for(int i=0; i<n-k+1; i++) {
		max=0;
		for(int j=i; j<i+k; j++) {
			if(max<arr[j]) max=arr[j];
		}
		max_arr[i] = max;
	}
	for(int i=0; i<n-k+1; i++) {
		cout<<max_arr[i]<<" ";
	} cout<<endl;
}
int main(){
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
		cin >> n >> k;
		int i;
		int arr[n];
		for(i=0; i<n; i++)
			cin >> arr[i];
		printKMax(arr, n, k);
		t--;
	}
	return 0;
}
