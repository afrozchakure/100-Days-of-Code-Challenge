#include<iostream>
using namespace std;
struct Node{
    char data;
    Node *left;
    Node *right;
}
// data -> left -> right
void Preorder(struct Node *root)
{
    if (root==NULL) return;
    cout<<root->data;
    Preorder(root->left);
    Preorder(root->right);
}
// left -> data -> right
void Inorder(struct Node *root)
{
    if (root == NULL) return;
    Inorder(root->left);
    cout<<root->data<<" ";
    Inorder(root->right);
}
// left -> right -> data
void Postorder(struct Node *root)
{
    if(root == NULL) return;
    Postorder(root->left);
    Postorder(root->right);
    cout<<root->data<<" ";
}
