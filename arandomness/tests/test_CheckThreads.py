#! /usr/bin/env python

"""Test arandomness' CheckThreads

Copyright:
    test_ParseCommas.py  test arandomness' ParseCommas
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

from arandomness.argparse import CheckThreads
import argparse
from multiprocessing import cpu_count

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production/Stable'
__version__ = '1.0.0'


def test_CheckThreads():
    """Test arandomness' CheckThreads with a simulated command line"""

    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('test',
                        type=int,
                        action=CheckThreads)

    # Test when thread count is correct
    threads = cpu_count() - 1
    args = parser.parse_args([str(threads)])
    assert args.test == threads

    # Test >1 thread
    try:
        parser.parse_args([0])
    except ValueError as error:
        assert str(error) == 'Must use at least one thread'

    # Test too many threads
    threads = cpu_count() + 1
    try:
        parser.parse_args([str(threads)])
    except ValueError as error:
        assert str(error) == 'Cannot use more threads than available: {0}'\
                             .format(str(cpu_count()))
