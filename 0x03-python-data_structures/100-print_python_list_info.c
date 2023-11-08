#include <Pytho n.h>

void print_python_list_info(PyObject *p)
{
    int size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "First element is not a list\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
