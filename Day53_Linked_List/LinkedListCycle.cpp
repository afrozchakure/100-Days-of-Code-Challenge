/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include<bits/stdc++.h>
class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_set <ListNode *> s;
        struct ListNode *slow;
        slow = head;
        while(slow != NULL)
        {
            if(s.find(slow) != s.end())  // If there is an element in the set
                return 1;
            s.insert(slow); // Else insert the element
            slow = slow->next;  // Move the pointer to next element
        }
        return 0;
    }
};


/*------------------Method-2-----------------------*/

class Solution {
public: 
    bool hasCycle(ListNode *head){
       if(head == NULL || head->next == NULL)
        return NULL;
       ListNode *slow = head, *fast = head;
       while(slow and fast and fast->next){
              slow = slow->next;
              fast = fast->next->next;
              if(slow == fast)
                return 1;
    }
    return 0;
}



