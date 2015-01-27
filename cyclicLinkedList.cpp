#include <stdio.h>
#include <assert.h>

typedef struct Node {
	Node* next;
} Node;

bool checkCylic (Node* head) {
	Node* slow = head;
	Node* fast = head;
	if (head == NULL) return true;
	while (fast->next != NULL) {
		slow = slow->next;
		fast = fast->next;
		if (fast->next != NULL) {
			fast = fast->next;
		} else return false;
		if (fast == slow) return true;
	}
	return false;
}

int main () 
{
	Node head1, node1;
	head1.next = &node1;
	node1.next = NULL;

	Node head2, node2, node3, node4;
	head2.next = &node2;
	node2.next = &node3;
	node3.next = &node4;
	node4.next = &node3;

	assert (checkCylic(&head1) == false);
	assert (checkCylic(&head2) == true);

	return 0;
}