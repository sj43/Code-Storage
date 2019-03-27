class binarysearchtree{
  class Node{
    int key;
    Node left,right;
    public Node(int item){
      key = item;
      left = right = null;
    }
  }

  Node root;
  binarysearchtree(){
    root = null;
  }
  void insert(int key){
    root = insertRec(root,key);
  }
  Node insertRec(Node root, int key){
    if(root == null){
      root = new Node(key);
      return root;
    }
    if(key<root.key){
      root.left = insertRec(root.left,key);
    }
    else if(key > root.key){
      root.right = insertRec(root.right,key);
    }
    return root;
  }

  void inorder(){
    inorderRec(root);
  }
  void inorderRec(Node root){
    if(root!=null){
      inorderRec(root.left);
      System.out.println(root.key);
      inorderRec(root.right);
    }
  }
  void preorderRec(Node root){
    if(root!=null){
      System.out.println(root.key);
      preorderRec(root.left);
      preorderRec(root.right);
    }
  }

  //a function to search a given key in BST
  public Node search(Node root, int key){
    if( root == NULL || root.key == key) return root;
    if(root.key < key) return search(root.right,key);
    return search(root.left,key);
  }

  public static void main(String[] args) {
    binarysearchtree tree = new binarysearchtree();
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);
    tree.insert(90);
    // print inorder traversal of the BST
    tree.inorder();
  }
}
}
