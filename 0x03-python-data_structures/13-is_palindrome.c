#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to the starting of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int x = 0, z = 0;
	int *_arr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	x = _len(*head);
	_arr = lst_arr(&x, _arr, *head);

	for (z = 0; _arr[x] && _arr[z] && (&_arr[x] != &_arr[z]); x--, z++)
	{
		if (_arr[x] == _arr[z])
			continue;
		else
		{
			free(_arr);
			return (0);
		}
	}
	free(_arr);
	return (1);
}



/**
 * _len - Length of the list
 * @_shft: pointer to list
 * Return: integer of length
 */
int _len(listint_t *_shft)
{
	int x = 0;

	for (x = 0; _shft; _shft = _shft->next)
		x++;
	return (x);
}


/**
 * lst_arr - copies from the list to array on the heap
 * @head: pointer to list
 * @_x: length of the list
 * @_arr: array pointer pointing to NULL
 * Return: pointer to the array
 */

int *lst_arr(int *_x, int *_arr, listint_t *head)
{
	listint_t *_shft = head;
	int x = 0;

	_arr = malloc(sizeof(int) * (*_x));
	(*_x)--;

	for (; _shft; _shft = _shft->next, x++)
		_arr[x] = _shft->n;

	return (_arr);
}

