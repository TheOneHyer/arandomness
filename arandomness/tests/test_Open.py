#! /usr/bin/env python

"""Test arandomness' Open argparse action

Copyright:
    test_Open.py  test arandomness' Open argparse action
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

import argparse
from ..argparse import Open
import bz2
import gzip
import lzma
from tempfile import NamedTemporaryFile

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production/Stable'
__version__ = '1.0.0'


def test_Open():
    """Test arandomness' Open ability to read and write files"""

    # Test BZIP2 write
    temp = NamedTemporaryFile(delete=False, suffix='.bz2')
    parser = argparse.ArgumentParser()
    parser.add_argument('test_bzip',
                        action=Open,
                        mode='wb')
    args = parser.parse_args([temp.name])
    args.test_bzip.write(b'bzip2')
    args.test_bzip.close()

    assert bz2.decompress(open(temp.name, 'rb').read()).strip() == b'bzip2'

    # Test BZIP2 read
    parser = argparse.ArgumentParser()
    parser.add_argument('test_bzip',
                        action=Open,
                        mode='rb')
    args = parser.parse_args([temp.name])

    assert args.test_bzip.read().strip() == b'bzip2'

    # Test GZIP write
    temp = NamedTemporaryFile(delete=False, suffix='.gz')
    parser = argparse.ArgumentParser()
    parser.add_argument('test_gzip',
                        action=Open,
                        mode='wb')
    args = parser.parse_args([temp.name])
    args.test_gzip.write(b'gzip')
    args.test_gzip.close()

    assert gzip.decompress(open(temp.name, 'rb').read()).strip() == b'gzip'

    # Test GZIP read
    parser = argparse.ArgumentParser()
    parser.add_argument('test_gzip',
                        action=Open,
                        mode='rb')
    args = parser.parse_args([temp.name])

    assert args.test_gzip.read().strip() == b'gzip'

    # Test LZMA write
    temp = NamedTemporaryFile(delete=False, suffix='.xz')
    parser = argparse.ArgumentParser()
    parser.add_argument('test_lzma',
                        action=Open,
                        mode='wb')
    args = parser.parse_args([temp.name])
    args.test_lzma.write(b'lzma')
    args.test_lzma.close()

    assert lzma.decompress(open(temp.name, 'rb').read()).strip() == b'lzma'

    # Test LZMA read
    parser = argparse.ArgumentParser()
    parser.add_argument('test_lzma',
                        action=Open,
                        mode='rb')
    args = parser.parse_args([temp.name])

    assert args.test_lzma.read().strip() == b'lzma'

    # Test txt write
    temp = NamedTemporaryFile(delete=False, suffix='.txt')
    parser = argparse.ArgumentParser()
    parser.add_argument('test_txt',
                        action=Open,
                        mode='w')
    args = parser.parse_args([temp.name])
    args.test_txt.write('txt')
    args.test_txt.close()

    assert open(temp.name, 'r').read().strip() == 'txt'

    # Test txt read
    parser = argparse.ArgumentParser()
    parser.add_argument('test_txt',
                        action=Open,
                        mode='r')
    args = parser.parse_args([temp.name])

    assert args.test_txt.read().strip() == 'txt'
