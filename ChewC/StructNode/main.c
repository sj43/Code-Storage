#include<stdio.h>
#include<stdlib.h>
#include"node.h"

int main(){
  struct Node* root = CreateNode(100);
  struct Node* node1 = InsertNode(root, 200);
  struct Node* node2 = InsertNode(node1, 300);
  struct Node* node3 = InsertNode(node1, 400);
  PrintNodeFrom(root);
  DestroyNode(node1, root);
  printf("\n");
  PrintNodeFrom(root);
  return 0;
}
