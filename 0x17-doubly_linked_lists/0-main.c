#include "lists.h"

/**
 * main - check the code
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    dlistint_t hello = {8, NULL, NULL};
    dlistint_t *head;
    dlistint_t *new;
    size_t n;

    head = &hello;

    new = malloc(sizeof(dlistint_t));
    if (new == NULL)
    {
        dprintf(2, "Error: Can't malloc\n");
        return (EXIT_FAILURE);
    }

    new->n = 9;
    head->prev = new;
    new->next = head;
    new->prev = NULL;
    head = new;

    n = print_dlistint(head);

    printf("-> %lu elements\n", n);
    free(new);
    return (EXIT_SUCCESS);
}

/**
 * Write a function that prints all the elements of a dlistint_t list.
 * 
 * Prototype: size_t print_dlistint(const dlistint_t *h);
 * Return: the number of nodes
 * Format: see example
 * 
*/
