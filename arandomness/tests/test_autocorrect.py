#! /usr/bin/env python

"""Test arandomness' autocorrect

Copyright:
    test_autocorrect.py  test arandomness' autocorrect
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

from arandomness.string import autocorrect

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production/Stable'
__version__ = '1.0.0'


def test_autocorrect():
    """Test arandomness' autocorrect"""

    # Setup test data
    words1 = ['bowtie2', 'bot']
    words2 = ['apple', 'apocalyptic', 'off word']
    words3 = ['computer', 'computational', 'compute']
    words4 = ['hello', 'hi']

    # Test "normal" word lists
    assert autocorrect('bow', words1) == 'bowtie2'
    assert autocorrect('apo', words2) == 'apocalyptic'

    # Test when no match available
    try:
        autocorrect('bad', words3, delta=0.75) == ''
    except AssertionError as error:
        assert str(error) == 'No matches for "bad" found'

    # Test exact word match
    assert autocorrect('hello', words4) == 'hello'
