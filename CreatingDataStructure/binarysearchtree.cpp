// this is a binary search tree in C
#include<stdio.h>
#include<stdlib.h>

struct node{
  int key;
  struct node *left, *right;
};

struct node* newNode(int item){
  struct node* temp = (struct node*)malloc(sizeof(struct node));
  temp->key = item;
  temp->left = temp->right = NULL;
  return temp;
}

void inorder(struct node* root){
  if(root != NULL){
    inorder(root->left);
    printf("%d \n", root->key);
    inorder(root->right);
  }
}

void preorder(struct node* root){
  if(root!=NULL){
    printf("%d \n", root->key);
    preorder(root->left);
    preorder(root->right);
  }
}

void postorder(struct node* root){
  if(root != NULL){
    postorder(root->left);
    postorder(root->right);
    printf("%d \n",root->key);
  }
}

//a function to search a given key in BST
struct node* search(struct node* root, int key){
  if(root == NULL || root->key == key) return root;
  if(root->key < key) return search(root->right,key);
  return search(root->left,key);
}


struct node* insert(struct node* node, int key){
  if(node==NULL) return newNode(key);
  if(node->key > key) node->left = insert(node->left,key);
  else if(node->key < key) node->right = insert(node->right,key);
  return node;
}


int main(){
  struct node* root = NULL;
  root = insert(root, 50);
  insert(root, 30);
  insert(root, 20);
  insert(root, 40);
  insert(root, 70);
  insert(root, 60);
  insert(root, 80);
  inorder(root);
  printf("\n");
  preorder(root);
  printf("\n");
  postorder(root);
  return 0;
}
