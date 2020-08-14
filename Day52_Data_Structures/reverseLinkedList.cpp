struct Node{
    struct Node *next;
    int data;
}
struct Node* reverseList(struct Node *head)
{
    struct Node *curr, *prev, *future;
    curr = head;
    prev = NULL;
    while(curr != NULL)
    {
        future = curr->next;
        curr->next = prev;
        prev = curr;
        curr = future;
    }
    curr = prev;
    return curr;
    // return head of reversed list
}
