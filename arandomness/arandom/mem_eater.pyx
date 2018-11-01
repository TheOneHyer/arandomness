#! /usr/bin/env python

"""<description>

Copyright:
    <script name>  <description>
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

from cpython.mem cimport PyMem_Malloc, PyMem_Free
import random

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Planning'
__version__ = '0.1.0a2'


# Credits: https://cython.readthedocs.io/en/latest/src/tutorial
# /memory_allocation.html
cdef class MemEater:

    cdef double* data

    def __cinit__(self, size_t number):
        # allocate some memory (uninitialised, may contain arbitrary data)
        self.data = <double*> PyMem_Malloc(number * sizeof(double))
        if not self.data:
            raise MemoryError()

        for i in range(number):
            self.data[i] = 1

    def __dealloc__(self):
        PyMem_Free(self.data)  # no-op if self.data is NULL
