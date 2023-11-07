#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to the starting of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *_shft = *head;
	int x = 0, z = 0;
	int _arr[1024];

	if (*head == NULL)
		return (1);

	for (; _shft; _shft = _shft->next, x++)
		_arr[x] = _shft->n;
	_arr[x--] = '\0';

	for (; _arr[x] && _arr[z] && (&_arr[x] != &_arr[z]); x--, z++)
	{
		if (_arr[x] == _arr[z])
			continue;
		else
			return (0);
	}
	return (1);
}
