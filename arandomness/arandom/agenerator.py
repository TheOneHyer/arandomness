#! /usr/bin/env python

"""Generate an arandom number sequence

Copyright:
    generator.py  generates an arandom number sequence
    Copyright (C) 2018  Alex Hyer

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

from . import MemEater
import psutil
from time import sleep

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Planning'
__version__ = '0.1.0a1'


def agenerator():
    """Arandom number generator"""

    free_mem = psutil.virtual_memory().available
    mem_24 = 0.24 * free_mem
    mem_26 = 0.26 * free_mem
    a = MemEater(int(mem_24 / 8))
    b = MemEater(int(mem_26 / 8))
    sleep(5)
    return (free_mem/1000/1000, psutil.virtual_memory().available/1000/1000)
