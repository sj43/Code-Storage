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

Node* kthToLastIterative(Node* head,int k){
  if(head==nullptr) return head;
  Node* ptr1 = head;
  Node* ptr2 = head;
  int i = 0;
  while(ptr1 && i < k){
    ptr1 = ptr1->next;
    i++;
  }
  if(i<k){
    return nullptr;
  }
  while(ptr1!=nullptr){
    ptr1 = ptr1->next;
    ptr2 = ptr2->next;
  }
  return ptr2;
}

Node* kthToLastHelper(Node* head, int k, int& i){
  if(head==nullptr) return head;
  // through this recursion, go all the way to the end and start from there.
  Node * node = kthToLastHelper(head->next,k,i);
  // once reached the end, exit from each recursion, adding 1 to i each time.
  i = i + 1;
  // if i equals k , it means that we have reached the kth to last element. Thus return the head.
  if(i==k) return head;
  // if i does not equal k, it means that we have not yet reached the kth to last element and we are still in
  // the process of exiting recursion. So, we return node.
  return node;
}

// We need to have i = 0 outside of the recursion function in order to keep track of how many steps
// we have come from the end. Having i = 0 inside the recursion will not work.
// That is why we have this kthToLastRecursive function generated aside, and calling the recursive helper
// function within.
Node* kthToLastRecursive(Node* head, int k){
  int i = 0;
  return kthToLastHelper(head, k, i);
}

int main(){
  Node* head = nullptr;
  for(int i=7;i>0;i--){
    insert(head,i); // note that this inserts i to the beginning of head
  }
  cout<<"List: ";
  printList(head);

  // Iterative Method
  std::cout << "4th node from last (Iterative) : ";
  Node *node4 = kthToLastIterative(head, 4);
  if ( node4 != nullptr ) {
    std::cout << node4->data << std::endl;
  } else {
    std::cout << "NULL NODE\n";
  }

  // Recursive Method
  std::cout << "4th node from last (Recursive) : ";
  node4 = kthToLastRecursive(head, 4);
  if ( node4 != nullptr ) {
    std::cout << node4->data << std::endl;
  } else {
    std::cout << "NULL NODE\n";
  }

  deleteList(head);
  return 0;
}
