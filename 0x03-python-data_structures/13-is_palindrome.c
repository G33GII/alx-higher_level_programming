#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer to the starting of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head);
int is_palindrome(listint_t **head)
{
	listint_t *reversed_second_half = NULL;
	listint_t *second_half = NULL;
    listint_t *first_half = NULL;
	listint_t *next_node = NULL;
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev = NULL;
	listint_t *mid = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	/* Find the middle of the list */
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	/*Handle odd-length lists: Move slow_ptr to the next node (the true middle)*/
	if (fast_ptr != NULL)
	{
		mid = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	/* Reverse the second half of the list */
	second_half = slow_ptr;
	reversed_second_half = NULL;
	while (second_half != NULL)
	{
		next_node = second_half->next;
		second_half->next = reversed_second_half;
		reversed_second_half = second_half;
		second_half = next_node;
	}
	/* Compare the first half and the reversed second half of the list */
	first_half = *head;

	while (reversed_second_half != NULL)
	{
		if (first_half->n != reversed_second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		first_half = first_half->next;
		reversed_second_half = reversed_second_half->next;
	}
	/* Restore the original list by reversing the reversed_second_half */
	second_half = NULL;

	while (reversed_second_half != NULL)
	{
		next_node = reversed_second_half->next;
		reversed_second_half->next = second_half;
		second_half = reversed_second_half;
		reversed_second_half = next_node;
	}
	/* Reconnect the second half to the middle (for odd-length lists) */
	if (mid != NULL)
		mid->next = second_half;
	else
		prev->next = second_half;

	return (is_palindrome);
}
