#! /usr/bin/env python

"""Detects and opens compressed files for reading or writing

Copyright:
    COpen.py  detects and opens compressed files for reading and writing
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

from ..files import copen
from argparse import Action


__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Beta'
__version__ = '2.0.0b5'


class COpen(Action):
    """Argparse Action that detects and opens compressed files for rw

    Attributes:
        option_strings (list): list of str giving command line flags that
                               call this action

        dest (str): Namespace reference to value

        mode (str): mode to pass to (de)compression algorithm

        nargs (bool): True if multiple arguments specified, must be None

        **kwargs (various): optional arguments to pass to argparse and algo

    Examples:
        .. code-block:: Python
            >>> import argparse
            >>> from tempfile import NamedTemporaryFile
            >>> # Write bzip file using COpen
            >>> temp = NamedTemporaryFile(delete=False, suffix='.bz2')
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('test_bzip',
            ...                   action=COpen,
            ...                   mode='wb')
            >>> args = parser.parse_args([temp.name])
            >>> args.test_bzip.write(b'bzip2')
            >>> args.test_bzip.close()
            >>> # Read bzip file using COpen
            >>> parser = argparse.ArgumentParser()
            >>> parser.add_argument('test_bzip',
            ...                   action=COpen,
            ...                   mode='rb')
            >>> args = parser.parse_args([temp.name])
            >>> args.test_bzip.read()
            b'bzip2'
    """

    def __init__(self, option_strings, dest, mode='rb', nargs=None, **kwargs):
        """Initialize class and spawn self as Base Class w/o nargs

        Raises:
            ValueError: if nargs is not None, COpen does not accept nargs
        """

        # Only accept a single value to analyze
        if nargs is not None:
            raise ValueError('nargs not allowed for COpen')

        # Call self again but without nargs, considering the above, I don't
        # know why this is needed, but it is
        super(COpen, self).__init__(option_strings, dest, **kwargs)

        # Store and establish variables used in __call__
        self.kwargs = kwargs  # Pass along unused args
        self.mode = mode.lower().strip()

    def __call__(self, parser, namespace, value, option_string=None, **kwargs):
        """Detects and opens compressed files

        Args:
            parser (ArgumentParser): parser used to generate values

            namespace (Namespace): namespace to set values for

            value (str): actual value specified by user

            option_string (str): argument flag used to call this function

            **kwargs (various): optional arguments later passed to the
                                compression algorithm
        """

        handle = copen(value, mode=self.mode, **self.kwargs)

        setattr(namespace, self.dest, handle)
