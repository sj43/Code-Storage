#include<iostream>
using namespace std;
struct Node{
  int data;
  Node* next;
  Node(int item):data{item},next{nullptr}{}
};
Node* insert(Node* head, int item){
  Node* newNode = new Node(item);
  newNode->next = head;
  head = newNode;
  return head;
}
void printList(Node* head){
  while(head){
    cout<<head->data<<"-->";
    head = head->next;
  }cout<<"nullptr"<<endl;
}
void deleteNode(Node* node){
  if(node==nullptr || node->next == nullptr) return;
  Node* nextNode = node->next;
  node->data = nextNode->data;
  node->next = nextNode->next;
  delete nextNode;
}
int main(){
  Node* head = new Node(5);
  head = insert(head,4);
  head = insert(head,3);
  head = insert(head,2);
  head = insert(head,1);
  head = insert(head,0);
  printList(head);
  deleteNode(head->next->next);
  printList(head);
  return 0;
}
