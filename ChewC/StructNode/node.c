#include<stdlib.h>
#include<stdio.h>
#include"node.h"

struct Node{
  int data;
  struct Node* nextNode;
};

struct Node* CreateNode(int data){
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

  newNode->data = data;
  newNode->nextNode = NULL;

  return newNode;
}

struct Node* InsertNode(struct Node* current, int data){
  struct Node* newNode = CreateNode(data);
  newNode->nextNode = current->nextNode;
  current->nextNode = newNode;

  return newNode;
}

void DestroyNode(struct Node* destroy, struct Node* head){
  struct Node* cur = head;

  if(cur == destroy){
    free(cur);
    return;
  }

  while(cur){
    if(cur->nextNode == destroy){
      cur->nextNode = destroy->nextNode;
    }
    cur = cur->nextNode;
  }
  free(destroy);
}

void PrintNodeFrom(struct Node* head){
  while(head){
    printf("Node Data : %d \n", head->data);
    head = head->nextNode;
  }
}
