#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *@head: head
 *@number: integer to be inserted
 *
 * Return: address of new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}

		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
