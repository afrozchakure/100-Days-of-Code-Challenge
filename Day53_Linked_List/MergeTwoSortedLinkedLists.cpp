/* Link list Node
struct Node {
  int data;
  struct Node *next;
  
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

Node* sortedMerge(Node* head_A, Node* head_B)  
{  
    struct Node *curr1 = head_A, *curr2 = head_B, *temp;
    int flag;
    if(curr1->data <= curr2->data){
        temp = head_A;
        flag = 1;
        curr1 = curr1->next;
    }
    else{
        temp = head_B;
        flag = 0;
        curr2 = curr2->next;
    }
    while(curr1 != NULL && curr2 != NULL){
        if(curr1->data <= curr2->data){
            temp->next = curr1;
            temp = curr1;
            curr1 = curr1->next;
        }
        else{
            temp->next = curr2;
            temp = curr2;
            curr2 = curr2->next;
        }
    }
    if(curr1 == NULL)
        temp->next = curr2;
    if(curr2 == NULL)
        temp->next = curr1;
    if(flag == 1)
        return head_A;
    else
        return head_B;
    // code here
}  

// Time Complexity - O(m+n)
// Space Complexity - O(1)
