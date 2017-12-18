#! /usr/bin/env python

"""Detects and opens compressed files for reading or writing

Copyright:
    open.py  detects and opens compressed files for reading and writing
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
import io
from os import linesep
import sys
from warnings import warn


__author__ = 'Alex Hyer'
__credit__ = 'Lauritz V. Thaulow'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Alpha'
__version__ = '2.0.0a4'


class Open(argparse.Action):
    """Argparse Action that detects and opens compressed files for rw

    Attributes:
        option_strings (list): list of str giving command line flags that
                               call this action

        dest (str): Namespace reference to value

        mode (str): mode to pass to (de)compression algorithm

        nargs (bool): True if multiple arguments specified

        **kwargs (various): optional arguments to pass to argparse and algo
    """

    def __init__(self, option_strings, dest, mode='rb', nargs=None, **kwargs):
        """Initialize class and spawn self as Base Class w/o nargs

        Warns:
            ImportError: if Open cannot import a compression library,
                         it warns the user that it cannot open the
                         corresponding file type

        Raises:
            ValueError: if nargs is not None, Open does not accept nargs
        """

        # Only accept a single value to analyze
        if nargs is not None:
            raise ValueError('nargs not allowed for Open')

        # Call self again but without nargs, considering the above, I don't
        # know why this is needed, but it is
        super(Open, self).__init__(option_strings, dest, **kwargs)

        # Store and establish variables used in __call__
        self.algo = io.open  # Only used as io.open in write mode
        self.kwargs = kwargs  # Pass along unused args
        self.mode = mode.lower().strip()
        self.modules = {}  # Later populated by compression algorithms
        self.write_mode = False if self.mode.lstrip('U')[0] == 'r' else True

        # Currently supported compression algorithms
        modules_to_import = {
            'bz2': 'BZ2File',
            'gzip': 'GzipFile',
            'lzma': 'LZMAFile'
        }

        # Dynamically import compression libraries and warn about failures
        for mod, _class in modules_to_import.items():
            try:
                self.modules[_class] = getattr(import_module(mod), _class)
            except (ImportError, AttributeError) as e:
                self.modules[_class] = open
                warn('Cannot process {0} files due to following error:'
                     '{1}{2}{1}You will need to install the {0} library to '
                     'properly use these files. Currently, such files will '
                     'open in text mode.'.format(mod, linesep, e))

    # Credits: https://stackoverflow.com/questions/13044562/
    # python-mechanism-to-identify-compressed-file-type-and-uncompress
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

        fileobject = value  # For readability, currently a str

        self.kwargs['mode'] = self.mode  # Added for later filtering

        # Write mode
        if self.write_mode is True:

            # Map file extensions to decompression classes
            algo_map = {
                'bz2': self.modules['BZ2File'],
                'gz':  self.modules['GzipFile'],
                'xz':  self.modules['LZMAFile']
            }

            # Determine the compression algorithm via the file extension
            ext = fileobject.split('.')[-1]
            try:
                self.algo = algo_map[ext]
            except KeyError:
                pass

        # Read mode
        else:

            self.algo = io.TextIOWrapper  # Default to plaintext buffer

            # Magic headers of encryption formats
            file_sigs = {
                b'\x42\x5a\x68': self.modules['BZ2File'],
                b'\x1f\x8b\x08': self.modules['GzipFile'],
                b'\xfd7zXZ\x00': self.modules['LZMAFile']
                }

            # Open the file, buffer it, and identify the compression algorithm
            fileobject = io.BufferedReader(io.open(fileobject, 'rb'))
            max_len = max(len(x) for x in file_sigs.keys())
            start = fileobject.peek(max_len)
            for sig in file_sigs.keys():
                if start.startswith(sig):
                    self.algo = file_sigs[sig]
                    break  # Stop iterating once a good signature is found

        # Filter all **kwargs by the args accepted by the compression algorithm
        algo_args = set(getfullargspec(self.algo).args)
        good_args = set(self.kwargs.keys()).intersection(algo_args)
        _kwargs = {arg: self.kwargs[arg] for arg in good_args}

        # Open the file using parameters defined above and store in namespace
        if self.write_mode is True:
            handle = self.algo(fileobject, **_kwargs)
        else:
            try:  # For algorithms that need to be explicitly given a fileobj
                handle = self.algo(fileobj=fileobject, **_kwargs)
            except TypeError:  # For algorithms that detect file objects
                handle = self.algo(fileobject, **_kwargs)

        setattr(namespace, self.dest, handle)
