#include "lists.h"

/**
 * check_cycle - This function checks if a singly
 *                              linked list has a cycle in it.
 * @list: head of the list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 *                  "(write, printf, putchar, puts, malloc, free)"
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL;
	listint_t *_tmp = NULL;

	if (!list || !(list->next))
		return (0);

	for (tmp = list, _tmp = list->next->next;
			tmp && _tmp && _tmp->next; tmp = tmp->next, _tmp = _tmp->next->next)
	{
		if (tmp == _tmp)
			return (1);
	}

	return (0);
}
