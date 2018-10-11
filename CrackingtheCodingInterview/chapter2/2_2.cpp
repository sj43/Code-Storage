#include<iostream>
using namespace std;

struct Node {
  int data;
  Node * next;
  Node(int d):data{d},next{nullptr}{}
};

// insert to head
void insert(Node* & head, int data){
  Node * newNode = new Node(data);
  newNode->next = head;
  head = newNode;
}

// delete entire list
void deleteList(Node* & head){
  Node * nextNode;
  while(head){
    nextNode = head->next;
    delete(head);
    head = nextNode;
  }
}

// print entire list
void printList(Node* head){
  while(head){
    cout<<head->data<<"-->";
    head = head->next;
  }
  cout<<"null"<<endl;
}

int main(){

}
