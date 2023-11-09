#include "lists.h"

/**
 * print_dlistint - check the code
 * @h: ptr to the head of the doubly linked list
 * Return: Always EXIT_SUCCESS.
 */
size_t print_dlistint(const dlistint_t *h)
{
	int x = 0;

	for (; h; h = h->next, x++)
		printf("%i\n", h->n);
	return (x);
}
