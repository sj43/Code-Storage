#include<bits/stdc++.h>
using namespace std;
struct Node{
  int data;
  Node* next;
  Node(int d):data{d},next{nullptr}{}
};
void printList(Node* head){
  while(head){
    cout<<head->data<<"-->";
    head = head->next;
  }cout<<"nullptr"<<endl;
}
void insert(Node*& head, int item){
  Node* newNode = new Node(item);
  if(head==nullptr) head=newNode;
  else{
    Node* cur = head;
    while(cur->next){
      cur = cur->next;
    }cur->next = newNode;
  }
}
Node* partition(Node* listhead, int x){
  Node * head = nullptr;
  Node * headInitial = nullptr;
  Node * tail = nullptr;
  Node * tailInitial = nullptr;
  Node * curr = listhead;
  while(curr != nullptr){
    Node * nextNode = curr->next;
    if(curr->data < x){
      if(head==nullptr){
        head = curr;
        headInitial = head;
      }
      head->next = curr;
      head = curr;
    }else{
      if(tail==nullptr){
        tail = curr;
        tailInitial = tail;
      }
      tail->next = curr;
      tail = curr;
    }
    curr = nextNode;
  }
  head->next = tailInitial;
  tail->next = nullptr;
  return headInitial;
}
int main(){
  Node* head = nullptr;
  for(int i=0;i<10;i++){
    insert(head,rand()%10);
  }
  printList(head);
  printList(partition(head,5));
  return 0;
}
