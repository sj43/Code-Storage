// struct Node{
//   int data;
//   struct Node* nextNode;
// };
struct Node* CreateNode(int data);
struct Node* InsertNode(struct Node* current, int data);
void DestroyNode(struct Node* destroy, struct Node* head);
void PrintNodeFrom(struct Node* head);
