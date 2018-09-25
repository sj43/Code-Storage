// this is a binary search tree in C
// to change the code from C to C++, we need to change 'free' to 'delete'.

//#include<iostream>
//#include<stack>
#include<bits/stdc++.h>
using namespace std;

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


void inorderWithStack(struct node* root){
  stack<node*> s;
  node* curr = root;
  while( curr!=NULL || s.empty()==false ){
    while(curr!=NULL){
      s.push(curr);
      curr = curr->left;
    }
    curr = s.top();
    s.pop();
    cout<<curr->key<<" ";
    curr = curr->right;
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


struct node* minValueNode(struct node* root){
  if(root->left == NULL) return root;
  return minValueNode(root->left);
}


struct node* deleteNode(struct node* root, int key){
  if(root==NULL) return root;
  else if(root->key < key) root->right = deleteNode(root->right, key);
  else if(root->key > key) root->left = deleteNode(root->left, key);
  else{
    // one child
    if(root->left == NULL){
      struct node* temp = root;
      root = root->right;
      free(temp);
    }
    else if(root->right == NULL){
      struct node* temp = root;
      root = root->left;
      free(temp);
    }
    // two child (get the minimum of the right subtree)
    else{
      struct node* temp = minValueNode(root->right);
      root->key = temp->key;
      root->right = deleteNode(root->right, temp->key);
    }
  }
  return root;
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
  root = deleteNode(root, 50);
  printf("Inorder traversal of the modified tree \n");
  inorder(root);
  printf("\n");
  root = deleteNode(root, 30);
  inorder(root);
  printf("\n");
  inorderWithStack(root);
  return 0;
}
