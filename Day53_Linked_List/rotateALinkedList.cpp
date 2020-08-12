struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

// This function should rotate list counter-clockwise
// by k and return new head (if changed)
Node* rotate(Node* head, int k)
{
    struct Node *curr; 
    curr = head;
    while(curr->next != NULL)
        curr = curr->next;
        
    // Making it a closed loop
    curr->next = head;
    curr = head;
    for(int i=0; i<k-1; i++ )
        curr = curr->next;
    head = curr->next;
    curr->next = NULL;
    return head;
}
