#include<bits/stdc++.h>
using namespace std;
class Stack{
public:
  int a[100000];
  int n;
  Stack(){
      n = -1;
  }
  void push(int x){
    a[++n] = x;
  }
  int pop(){
		if(n==-1) return -1;
    else return a[n--];
  }
  int size(){
    return n+1;
  }
  bool empty(){
    return n==-1;
  }
  int top(){
    if(this->empty()) return -1;
    return a[n];
  }
};

int main(){
  int N;
  cin>>N;
  Stack mystack;

	for (int i = N; i > 0; --i)
	{
		char cmd[6];
		std::cin >> cmd;

		if (!strcmp(cmd, "push"))
		{
			int push_val = 0;
			cin >> push_val;
	  	mystack.push(push_val);
		}
		else if (!strcmp(cmd, "pop"))
		{
			int poped = mystack.pop();

			cout << poped << endl;
		}
		else if (!strcmp(cmd, "size"))
		{
			cout << mystack.size() << endl;
		}
		else if (!strcmp(cmd, "empty"))
		{
			cout << mystack.empty() << endl;
		}
		else if (!strcmp(cmd, "top"))
		{
			cout << mystack.top() << endl;
		}
	}

  return 0;
}
