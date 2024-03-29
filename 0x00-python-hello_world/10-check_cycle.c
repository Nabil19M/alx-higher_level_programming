#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of the list
 * Return: return 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = list->next;
		fast = list ->next->next;
		if (slow == fast)
		return (1);
	}
	return (0);
}