#!/usr/bin/python3
"""function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices.
    Agrs:
        m_a(list): List of list
        m_b(list): List of list
    Raises:
        TypeError: m_a must be a list
        TypeError: m_a must be a list of lists
    Returns:
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(z, list) for z in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(z, list) for z in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not x for x in m_a):
        raise ValueError("m_a can't be empty")
    if not m_a or any(not x for x in m_a):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(x, (int, float)) for z in m_a for x in z):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(x, (int, float)) for z in m_b for x in z):
        raise TypeError("m_b should contain only integers or floats")
    if any(not isinstance(x, (int, float)) for z in m_b for x in z):
        raise TypeError("m_b should contain only integers or floats")

    _l = len(m_a[0])
    __l = len(m_b[0])

    if any(len(x) != _l for x in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(x) != __l for x in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a) != __l:
        raise ValueError("m_a and m_b can't be multiplied")

    for x in range(len(m_a)):
        [k for ]





