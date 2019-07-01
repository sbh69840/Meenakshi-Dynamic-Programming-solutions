#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int val;
	struct node* left;
	struct node* right;
} node_t;

void insert(node_t* tree,int val);
void printTree(node_t* current);
void printDFS(node_t* current);
void addTree(node_t* current);
int main(){
	node_t* tree = malloc(sizeof(node_t));
	tree->val=0;
	tree->left=NULL;
	tree->right=NULL;
	insert(tree,7);
	insert(tree,4);
	insert(tree,9);
	insert(tree,6);
	insert(tree,5);
	insert(tree,1);
	printDFS(tree);
	addTree(tree);
	printf("AFTER THE ADDITION.\n");
	printDFS(tree);

	return 0;
}

void insert(node_t* tree,int val){
	if (tree->val==0){
		tree->val = val;
	}else{
		if (val<tree->val){
			if (tree->left!=NULL){
				insert(tree->left,val);

			}else{
				tree->left = malloc(sizeof(node_t)); 
				tree->left->val = val;
				tree->left->left=NULL;
				tree->left->right=NULL;
			}
	}else if(val>=tree->val){
		if (tree->right!=NULL){
			insert(tree->right,val);
		}else{
			tree->right=malloc(sizeof(node_t));
			tree->right->val = val;
			tree->right->left=NULL;
			tree->right->right = NULL;
		}
	}
	}
}
/*
PRE-ORDER DFS, visit, left, right
*/
void printDFS(node_t* current){
	if (current==NULL){
		return;
	}
	
	if (current->left!=NULL){
		printDFS(current->left);
	}
	if (current!=NULL){
		printf("%d \n",current->val);
	}
	if (current->right!=NULL){
		printDFS(current->right);
	}
}

void addTree(node_t* current){
	if (current==NULL){
		return;
	}
	addTree(current->left);
	addTree(current->right);
	int final = current->val;
	if (current->left!=NULL){
		final+=current->left->val;
	}
	if (current->right!=NULL){
		final+=current->right->val;
	}
	current->val=final;
}
