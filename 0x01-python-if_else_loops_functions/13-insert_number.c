#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a number into sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *h;
	int flag = 0;

	if (new == NULL)
		return (NULL);
	h = *head;
	new->n = number;
	if (h == NULL || h->n >= number)
	{
		new->next = h;
		*head = new;
		return (new);
	}
	while (h->next != NULL)
	{
		if (flag)
		{
			return (new);
		}
		if (number >= h->n && number <= h->next->n)
		{
			new->next = h->next;
			h->next = new;
			flag = 1;
		}
		h = h->next;
	}
	return (add_nodeint_end(&h, number));
}
