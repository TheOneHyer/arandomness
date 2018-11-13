#! /usr/bin/env python

"""Consume an arbitrary amount of 64 bit blocks of virtual memory

Copyright:
    mem_eater.pyx  Consume an arbitrary amount of virtual memory
    Copyright (C) 2017  Alex Hyer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from cpython cimport array
from cpython.mem cimport PyMem_Malloc, PyMem_Free

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production'
__version__ = '1.0.0'


# Credits: https://cython.readthedocs.io/en/latest/src/tutorial
# /memory_allocation.html
cdef class MemEater:
    """Cython Class that consumes arbitrary amounts of RAM and can enumerate

    Attributes:
        data (public char pointer): pointer to array for consuming RAM

        number (public size_t): number of elements in data
    """

    # Declare variables for use throughout MemEater
    cdef public char* data
    cdef public size_t number

    def __cinit__(self, size_t number):
        """C initialization that consumes lots of RAM.

        Args:
            number (size_t): number of bytes to allocate

        Raises:
            MemoryError: if memory cannot be allocated
        """

        # Allocate uninitialized array
        self.data = <char*> PyMem_Malloc(number)

        # Raise MemoryError in self.data cannot be allocated
        if not self.data:
            raise MemoryError()

        # Initialize and populate the array with ones cuz that's a good number
        for i in range(number):
            self.data[i] = 1

    def __init__(self, number):
        """Python initialization to make number accessible to Python

        Args:
            number (int): number of bytes of memory consumed by MemEater
        """

        self.number = number  # Yup...that's it.

    def size(self):
        """Returns the total amount of RAM consumed in bytes

        """

        # Declare and initialize counter here because why not
        cdef int total = 0

        # Calculate RAM usage in bytes by summing self-aware ones
        for i in self.data:
            total += i

        return total

    def __dealloc__(self):
        """Release memory on object destruction"""

        PyMem_Free(self.data)  # no-op if self.data is NULL
