// Left view of a binary tree is the set of nodes which are 
// visible when we visit the binary tree from the left side

#include<iostream>
using namespace std;
class node{
    public:
    node *left, *right;
    int data;
};
// Function for adding a new node
node* newNode(int item)
{
    node* temp = new node();
    temp->data = item;
    temp->left = temp->right = NULL;   
}
void leftViewUtil(node* root, int level, int* maxlevel){
    if(root == NULL) return;
    // If this is the first node of the level
    if(*maxlevel < level)
    {
        cout<<root->data<<" ";
        *maxlevel = level;
    }
    leftViewUtil(root->left, level+1, maxlevel);
    leftViewUtil(root->right, level+1, maxlevel);
}
// Wrapper for leftViewUtil() function
void leftView(node* root)
{
    int maxlevel = 0;
    leftViewUtil(root, 1, &maxlevel);  // Passing the addres of maxlevel
}
int main()
{
    node* root = newNode(12);
    root->left = newNode(10);
    root->right = newNode(30);
    root->right->right = newNode(40);
    root->right->left = newNode(25);
    leftView(root);
}