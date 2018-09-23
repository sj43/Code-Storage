#include<iostream>
#include<vector>
using namespace std;

//creating my own stack using vector
template<class T>
class myStack{
private:
  int top=-1;
  vector<T> *stack;
public:
  myStack(){
    stack = new vector<T>();
  }
  bool isEmpty(){
    return top==-1;
  }
  void push(T element){
    stack->push_back(element);
    top++;
  }
  void pop(){
    if(!isEmpty()){
      stack->pop_back();
      top--;
    }
    else cout<<"Error: Stack Already Empty\n";
  }
  T peek(){
    if(!isEmpty()) return stack->back();
    else cout<<"Error: Stack Already Empty\n";
  }
  void clear(){
    top=-1;
    stack->clear();
    cout<<"Stack cleared\n";
  }
};

int main(){
  myStack<int> stack = myStack<int>();
  stack.push(100);
  stack.push(200);
  cout<<stack.peek();
  stack.pop();
  cout<<stack.peek();
  stack.pop();
  stack.pop();
}
