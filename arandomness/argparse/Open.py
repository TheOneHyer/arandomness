#! /usr/bin/env python

"""Detects and opens compressed files

Copyright:
    open.py  detects and opens compressed files
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
from importlib import import_module

modules = {
    'bz2': 'BZ2File',
    'gzip': 'GzipFile',
    'lzma': 'LZMAFile',
    'zipfile': 'ZipFile'
}

for package, mod in modules.items():
    try:
        import_module(mod, package=package)
    except ImportError:
        pass

__author__ = 'Alex Hyer'
__credit__ = 'Lauritz V. Thaulow'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Alpha'
__version__ = '0.1.0a1'


class Open(argparse.Action):
    """Argparse Action that detects and opens compressed files

    Attributes:
        option_strings (list): list of str giving command line flags that
                               call this action

        dest (str): Namespace reference to value

        nargs (bool): True if multiple arguments specified

        **kwargs (various): optional arguments to pass to super call
    """

    def __init__(self, option_strings, dest, comp_algo='txt', mode='r',
                 nargs=None, **kwargs):
        """Initialize class and spawn self as Base Class w/o nargs

        Args:
            option_strings (list): list of str giving command line flags that
                                   call this action

            dest (str): namespace reference to value

            nargs (str): number of args as special char or int

            **kwargs (various): optional arguments to pass to super call
        """

        # Only accept a single value to analyze
        if nargs is not None:
            raise ValueError('nargs not allowed for Open')

        self.mode = mode.lower().strip()
        self.comp_algo = comp_algo.lower().strip()

        # Call self again but without nargs
        super(Open, self).__init__(option_strings, dest, **kwargs)

    # Credits: https://stackoverflow.com/questions/13044562/
    # python-mechanism-to-identify-compressed-file-type-and-uncompress
    def __call__(self, parser, namespace, value, option_string=None, **kwargs):
        """Detects and opens compressed files

        Args:
            parser (ArgumentParser): parser used to generate values

            namespace (Namespace): namespace to set values for

            value (str): actual value specified by user

            option_string (str): argument flag used to call this function

        Raises:
            ValueError: if value does not map to a supported compression
                        algorithm
        """

        filename = value

        algo = open

        if self.mode not in ['r', 'rb']:

            algo_map = {
                'bz2': BZ2File,
                'gzip': GzipFile,
                'lzma': LZMAFile,
                'txt': open,
                'zip': ZipFile
            }

            if self.comp_algo not in algo_map.keys():
                raise ValueError('"{0}" not supported'.format(self.comp_algo))

            algo = algo_map[self.comp_algo]

        else:

            file_sigs = {
                '\x42\x5a\x68': BZ2File,
                '\x1f\x8b\x08': GzipFile,
                '\xff\x4c\x5a\x4d\x41\x00': LZMAFile,
                '\x50\x4b\x03\x04': ZipFile
                }

            max_len = max(len(x) for x in file_sigs.keys())

            with open(filename, 'rb') as in_handle:
                start = str(in_handle.read(max_len))
                for sig in file_sigs.keys():
                    if start.startswith(sig):
                        algo = file_sigs[sig]
                        break

        handle = algo(value, mode=self.mode, **kwargs)

        setattr(namespace, self.dest, handle)
