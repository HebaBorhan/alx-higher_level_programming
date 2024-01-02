#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 *@list: pointer to the head
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *current = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (current && temp && temp->next)
	{
		current = current->next;
		temp = temp->next->next;

		if (current == temp)
		{
			return (1);
		}
	}
	return (0);
}
