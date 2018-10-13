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
void deleteList(Node*& head){
  Node * nextNode;
  while(head){
    nextNode = head->next;
    delete(head);
    head = nextNode;
  }
}
Node* add_recursive(Node* l1, Node* l2, int carry){
  if(l1==nullptr && l2==nullptr && carry ==0){
    return nullptr;
  }
  int value = carry;
  if(l1!=nullptr){
    value += l1->data;
  }
  if(l2!=nullptr){
    value += l2->data;
  }
  Node* resultNode = new Node(value%10);
  resultNode->next = add_recursive(l1?(l1->next):nullptr, l2?(l2->next):nullptr, value>9?1:0);
  return resultNode;
}
int main(){
  Node* list1 = nullptr;
  insert(list1,6);
  insert(list1,1);
  insert(list1,7);
  printList(list1);

  Node* list2 = nullptr;
  insert(list2,2);
  insert(list2,9);
  insert(list2,5);
  printList(list2);

  Node* list3 = add_recursive(list1, list2,0);
  cout<<"Recursive solution: \n";
  cout<<"List3: ";
  printList(list3);
  return 0;
}
