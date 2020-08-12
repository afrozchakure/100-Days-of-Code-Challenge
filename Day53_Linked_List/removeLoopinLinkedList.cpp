// Other methods are there as well

#include<bits/stdc++.h>
void removeLoop(Node* head)
{
    unordered_set <Node *> s;
    struct Node *slow, *prev;
    slow = head;
    while(slow){
        if(s.find(slow) != s.end())
            break;
        prev = slow;
        s.insert(slow);
        slow = slow->next;
    }
    
    prev->next = NULL;
    // just remove the loop without losing any nodes
}



// Floyd's method
void removeLoop(Node* head)
{
    if(head == NULL || head->next == NULL)
        return;
    struct Node *slow=head, *fast=head, *prev = head;
    slow = slow->next;
    fast = fast->next->next;
    while(fast->next && fast){
        if(fast == slow)
            break;
        prev = slow
        slow = slow->next;
        fast = fast->next->next;
    }
    // cout<<"Got it "<<fast->data<<endl;
    if(fast == head){
        prev->next = NULL;
    }
    if(slow == fast){
        slow = head;
        while(slow->next != fast->next){
            slow = slow->next;
            fast = fast->next;
        }
        fast->next = NULL;
    }
}

// Time Complexity - O(n), Space complexity - O(1)
