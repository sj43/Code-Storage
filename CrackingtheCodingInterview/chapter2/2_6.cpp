#include<bits/stdc++.h>
using namespace std;
struct Node{
  char data;
  Node* next;
  Node(char d):data{d},next{nullptr}{}
};
void insert(Node*&head,char ch){
  Node* newNode = new Node(ch);
  if(head==nullptr){
    head = newNode;
  }else{
    Node* curr = head;
    while(curr->next){
      curr = curr->next;
    }curr->next = newNode;
  }
}
void printList(Node*head){
  while(head){
    cout<<head->data<<"-->";
    head = head->next;
  }cout<<"nullptr\n";
}
bool isPalindromeIter2(Node* head){
  if(head==nullptr || head->next == nullptr){
    return true;
  }
  Node* ptr1 = head;
  Node* ptr2 = head;
  stack<Node*> nodeStack;
  while(ptr1 && ptr2 && ptr1->next){
    ptr1 = ptr1->next->next;
    nodeStack.push(ptr2);
    ptr2 = ptr2->next;
  }
  if(ptr1 && ptr1->next==nullptr){
    ptr2 = ptr2->next;
  }
  while(!nodeStack.empty() && ptr2){
    Node* curr = nodeStack.top();
    nodeStack.pop();
    if(curr->data != ptr2->data){
      return false;
    }
    ptr2 = ptr2->next;
  }
  return true;
}
int main(){
  Node* root = nullptr;
  insert(root,'a');
  insert(root,'b');
  insert(root,'c');
  insert(root,'d');
  insert(root,'e');
  insert(root,'d');
  insert(root,'c');
  insert(root,'b');
  insert(root,'a');
  printList(root);
}
