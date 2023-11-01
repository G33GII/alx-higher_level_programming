#include "lists.h"

/**
 * insert_node -
 * @head:
 * @number:
 * Return:
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node_ptx = *head, *_nx = NULL;

    _nx = malloc(sizeof(listint_t));
    if (_nx == NULL)
        return (NULL);
    _nx->n = number;

    if (node_ptx == NULL || node_ptx->n >= number)
    {
        _nx->next = node_ptx;
        *head = _nx;
        return (_nx);
    }

    while (node_ptx && node_ptx->next && node_ptx->next->n < number)
        node_ptx = node_ptx->next;

    _nx->next = node_ptx->next;
    node_ptx->next = _nx;

    return (_nx);
}
