#! /usr/bin/env python

"""Test arandomness' CopyRight

Copyright:
    test_CopyRight.py  test arandomness' CopyRight
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

from arandomness.argparse import CopyRight
import argparse
from io import StringIO
import sys

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Production/Stable'
__version__ = '1.0.2'


def test_CopyRight():
    """Test arandomness' CopyRight with a simulated command line"""

    # Capture STDOUT for later testing
    capture = StringIO()
    sys.stdout = capture

    # Stop parser.exit() in CopyRight from exiting program
    sys.exit = lambda *x: None

    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('test',
                        action=CopyRight,
                        copyright_text='test')
    parser.parse_args()

    # Test printed "copyright"
    assert capture.getvalue().strip() == 'test'
