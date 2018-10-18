#! /usr/bin/env python

"""Test arandomness' Open function from files subpackage

Copyright:
    test_Open.py  test arandomness' Open function from files subpackage
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

from ..files import Open
import bz2
import gzip
import lzma
from tempfile import NamedTemporaryFile

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Alpha'
__version__ = '1.0.0b1'


def test_Open():
    """Test arandomness' Open ability to read and write files"""

    # Test BZIP2 write
    temp = NamedTemporaryFile(delete=False, suffix='.bz2')
    test_bz2 = Open(temp.name, 'wb')
    test_bz2.write(b'bzip2')
    test_bz2.close()

    assert bz2.decompress(open(temp.name, 'rb').read()) == b'bzip2'

    # Test BZIP2 read
    test_bz2 = Open(temp.name, 'rb')

    assert test_bz2.read() == b'bzip2'

    # Test GZIP write
    temp = NamedTemporaryFile(delete=False, suffix='.gz')
    test_gz = Open(temp.name, 'wb')
    test_gz.write(b'gzip')
    test_gz.close()

    assert gzip.decompress(open(temp.name, 'rb').read()) == b'gzip'

    # Test GZIP read
    test_gz = Open(temp.name, 'rb')
    print(test_gz)

    assert test_gz.read() == b'gzip'

    # Test LZMA write
    temp = NamedTemporaryFile(delete=False, suffix='.xz')
    test_lzma = Open(temp.name, 'wb')
    test_lzma.write(b'lzma')
    test_lzma.close()

    assert lzma.decompress(open(temp.name, 'rb').read()) == b'lzma'

    # Test LZMA read
    test_lzma = Open(temp.name, 'rb')

    assert test_lzma.read() == b'lzma'

    # Test txt write
    temp = NamedTemporaryFile(delete=False, suffix='.txt')
    test_txt = Open(temp.name, 'wt')
    test_txt.write('txt')
    test_txt.close()

    assert open(temp.name, 'rt').read().strip() == 'txt'

    # Test txt read
    test_txt = Open(temp.name, 'rt')

    assert test_txt.read().strip() == 'txt'
