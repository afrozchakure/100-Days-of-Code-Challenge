#include<iostream>
using namespace std;

class BST
{
    int data;
    BST *left, *right;

    public:

    // Default Constructor
    BST();

    // Parametrized Constructor
    BST(int);

    // Insert function
    BST* Insert(BST *, int);

    // Inorder Traversal
    void Inorder(BST *);
};

// Default Constructor definition
BST:: BST() : data(0), left(NULL), right(NULL) {}

// Parametrized Constructor definition
BST :: BST(int value)
{
    data = value;
    left = right = NULL;
}

// Insert Function definition
BST* BST:: Insert(BST *root, int value)
{
    if(root == NULL)
        return new BST(value);  // Create a new BST with the value
    if(value > root->data)
    {
        root->right = Insert(root->right, value);
    }
    else if(value < root->data)
    {
        root->left = Insert(root->left, value);
    }
    // return root after insertion
    return root;
}

void BST:: Inorder(BST *root)
{
    if(root == NULL)
        return;
    Inorder(root->left);
    cout<<root->data<<endl;
    Inorder(root->right);

}

int main()
{
    BST b, *root = NULL;
    root = b.Insert(root, 50);
    b.Insert(root, 30);
    b.Insert(root, 20);
    b.Insert(root, 40);
    b.Insert(root, 70);
    b.Insert(root, 60);
    b.Insert(root, 80);
    b.Inorder(root);
    return 0;
}