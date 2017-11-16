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

import argparse
from ..argparse import Open
import gzip
from tempfile import NamedTemporaryFile

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Planning'
__version__ = '0.1.0a1'


def test_Open():
    """Test arandomness' Open ability to read and write files"""

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

    parser = argparse.ArgumentParser()
    parser.add_argument('test_gzip',
                        action=Open,
                        mode='rb')
    args = parser.parse_args([temp.name])

    assert args.test_gzip.read().strip() == b'gzip'
