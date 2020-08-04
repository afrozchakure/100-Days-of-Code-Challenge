#include<iostream>
using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
}

int isBstUtil(Node* root, int minValue, int maxValue){
    if (root == NULL) return true;
    if(root->data > minValue && 
      root->data < maxValue &&
      isBST(root->left, minValue, root->data) &&
      isBST(root->right,root->right, maxValue))
      return true;
    else
        return false;
}
// caller of the binary search tree function may want to pass 
// only the address of the root node
bool IsBST(Node* root)
{
    return isBstUtil(root, INT_MIN, INT_MAX);
}
// Time Complexity = O(n) - where n is the no. of nodes of binary tree
// Space - O




"""// Correct but not efficient
bool IsSubtreeLesser(Node *root, int value)
{
    if root == NULL return;
    if( root->data <= value &&
        IsSubtreeLesser(root->left, value) 
        && IsSubtreeLesser(root->right, value))
        return true;
    return false ;
}
bool IsSubtreeGreater(Node *root, int value)
{
    if root == NULL return ;
    if (root->data > value &&
        IsSubtreeGreater(root->right, value)
        && IsSubtreeGreater(root->left, value))
        return true;
    return false;
}
bool IsBST(Node* root)
{
    // return true if BST, false otherwise
    if (root == NULL) return;
    if (IsSubtreeGreater(root, root->data) && 
        IsSubtreeLesser(root, root->data) &&
        IsBST(root->left) &&
        IsBST(root->right))
        return true 
    return false
}
// Time Complexity - O(n^2)
"""
