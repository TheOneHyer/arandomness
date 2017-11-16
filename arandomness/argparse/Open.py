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
from inspect import getfullargspec
from os import linesep
from warnings import warn


__author__ = 'Alex Hyer'
__credit__ = 'Lauritz V. Thaulow'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Alpha'
__version__ = '0.1.0a2'


class Open(argparse.Action):
    """Argparse Action that detects and opens compressed files

    Attributes:
        option_strings (list): list of str giving command line flags that
                               call this action

        dest (str): Namespace reference to value

        nargs (bool): True if multiple arguments specified

        **kwargs (various): optional arguments to pass to super call
    """

    def __init__(self, option_strings, dest, mode='rb', nargs=None, **kwargs):
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
        self.kwargs = kwargs

        modules_to_import = {
            'bz2': 'BZ2File',
            'gzip': 'GzipFile',
            'lzma': 'LZMAFile',
            'zipfile': 'ZipFile'
        }

        self.modules = {}

        for mod, _class in modules_to_import.items():
            try:
                self.modules[_class] = getattr(import_module(mod), _class)
            except (ImportError, AttributeError) as e:
                self.modules[_class] = open
                warn('Cannot process {0} files due to following error:'
                     '{1}{2}{1}Such files will open in text mode.'
                     .format(mod, linesep, e))

        # Call self again but without nargs
        super(Open, self).__init__(option_strings, dest)

    # Credits: https://stackoverflow.com/questions/13044562/
    # python-mechanism-to-identify-compressed-file-type-and-uncompress
    def __call__(self, parser, namespace, value, option_string=None, **kwargs):
        """Detects and opens compressed files

        Args:
            parser (ArgumentParser): parser used to generate values

            namespace (Namespace): namespace to set values for

            value (str): actual value specified by user

            option_string (str): argument flag used to call this function
        """

        filename = value

        algo = open  # Default to plaintext

        if self.mode not in ['r', 'rb']:

            algo_map = {
                'bz2': self.modules['BZ2File'],
                'gz': self.modules['GzipFile'],
                'xz': self.modules['LZMAFile'],
                'zip': self.modules['ZipFile']
            }

            ext = value.split('.')[-1]
            try:
                algo = algo_map[ext]
            except KeyError:
                pass

        else:

            file_sigs = {
                b'\x42\x5a\x68': self.modules['BZ2File'],
                b'\x1f\x8b\x08': self.modules['GzipFile'],
                b'\xff\x4c\x5a\x4d\x41\x00': self.modules['LZMAFile'],
                b'\x50\x4b\x03\x04': self.modules['ZipFile']
                }

            max_len = max(len(x) for x in file_sigs.keys())

            with open(filename, 'rb') as in_handle:
                start = in_handle.read(max_len)
                for sig in file_sigs.keys():
                    if start.startswith(sig):
                        algo = file_sigs[sig]
                        break

        algo_args = getfullargspec(algo).args
        good_args = set(self.kwargs.keys()).intersection(algo_args)
        _kwargs = {arg: self.kwargs[arg] for arg in good_args}

        handle = algo(value, mode=self.mode, **_kwargs)

        setattr(namespace, self.dest, handle)
