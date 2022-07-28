#include "lists.h"
#include <stdio.h>

/*
* insert_node - insert node into a sorted linked list
* @head: pointer to the linked list
* @number: number to the inserted
*
* Description: insert a node into a sorted linked list
*
* Return: address of new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
		return (NULL);

	while (current->next != NULL)
	{
		if (current->n < number && current->next->n > number)
		{
			new_node->n = number;
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (*head);
}
