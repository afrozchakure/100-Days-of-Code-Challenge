#include<iostream>
using namespace std;
// Inorder Successor in a BST
struct Node{
    int data;
    Node* left;
    Node* right;
    Node* parent;
};

// Function to find Node with minimum value in BST
struct Node* FindMin(struct Node* root){
    while(root->left != NULL)  // while root->left not NULL
        // Goto left-most node in right-subtree
        // While there is something in left keep going
        root = root->left; 
    return root;
    
}

// Function for finding the particular node 
struct Node* Find(struct Node* root, int data){
    if(root == NULL || root->data == data ) return root;
    else if(root->data < data) return Find(root->left, data);
    else return Find(root->right, data);
}

// Simpler function when a BST and (reference to Node x) in BST given
struct Node* Getsucessor(struct Node* root, struct Node* n){
    if(n != NULL){
        return NULL;
    }
    if(n->right!=NULL)
        return FindMin(n->right);
    struct Node* succ = NULL;
    while(n != root){
        if(n->data < root->data){
            succ = root;
            root = root->left;
        }
        else{
            root = root->right;
        }
    }
    return succ;
}
// Time Complexity = O(h) , h is the height of the tree
// Space complexity = O(1)


// left -> data -> right
// Function to find the successor, It can take root node and another node (current) as input for which we want to find successor

/*// Function returns the addess of successor node (as a pointer)
struct Node* Getsuccessor(struct Node* root, int data){
    
    struct Node* current = Find(root, data); //  Search the Node - O(h) (in BST), where h is height of the tree
    
    if(current == NULL) return NULL;
    
    // Case 1: Node has right subtree (find minimum element in right subtree)
    if(current->right != NULL){  
        return FindMin(current->right); // Passing the right sub-tree
    } // - Finding min element in subtree is O(h)
    
    // Case 2: No right subtree - O(h)
    else{
        struct Node* successor = NULL; 
        struct Node* ancestor = root;
        
        while(ancestor != current) { // Walk the tree till we have not reached the current node
            if(current->data < ancestor->data){ // value of current less than value of ancestor
                successor = ancestor;  // so far ancestor is the deepest node for which current node is in left
                ancestor = ancestor->left;
            }  
            else{
                ancestor = ancestor->right;
            }
        return successor;
    }
    

}*/