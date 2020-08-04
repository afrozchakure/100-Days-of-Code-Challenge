#include<iostream>
#include<queue>
using namespace std;
struct Node{
    char data;
    Node *left;
    Node *right;
};
void LevelOrder(Node * root)
{
    if(root == NULL) return;
    queue<Node *> Q;
    Q.push(root);

    // while there is at least one discovered node
    while(!Q.empty()){
        // Getting the 1st node from the queue
        Node* current = Q.front();
        cout<<current->data<<" ";
        // If left and right node not NULL
        if(current->left != NULL) Q.push(current->left);
        if(current->right != NULL) Q.push(current->right);
        Q.pop();  // Removing first element in Queue
    }
}

// Time-Complexity = O(n)
// Space-Complexity
// O(1) - (Best Case) Skewed Binary Tree (Only one-element in queue at a time)
// O(n) - (Worst/Average) Complete Binary Tree