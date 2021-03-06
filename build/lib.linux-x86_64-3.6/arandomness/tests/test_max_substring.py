#! /usr/bin/env python

"""Test arandomness' max_substring

Copyright:
    test_max_substring.py  test arandomness' max_substring
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

from arandomness.str import max_substring

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production/Stable'
__version__ = '1.0.2'


def test_max_substring():
    """Test arandomness' max_substring"""

    # Setup test data
    test1 = ['aaaa', 'aaab', 'aaac']
    test2 = ['abbb', 'bbbb', 'cbbb']
    test3 = ['abc', 'bcd', 'cde']

    # Perform basic test
    assert max_substring(test1) == 'aaa'

    # Test non-zero starting position
    assert max_substring(test2, position=1) == 'bbb'

    # Test no match
    assert max_substring(test3) == ''
