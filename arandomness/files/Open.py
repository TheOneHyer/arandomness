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

from importlib import import_module
from inspect import getfullargspec
import io
from os import linesep
from warnings import warn


__author__ = 'Alex Hyer'
__credit__ = 'Lauritz V. Thaulow'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Beta'
__version__ = '2.0.0b1'


# Credits: https://stackoverflow.com/questions/13044562/
# python-mechanism-to-identify-compressed-file-type-and-uncompress
def Open(fileobj, mode='rb', **kwargs):
    """"""

    algo = io.open  # Only used as io.open in write mode
    mode = mode.lower().strip()
    modules = {}  # Later populated by compression algorithms
    write_mode = False if mode.lstrip('U')[0] == 'r' else True
    kwargs['mode'] = mode

    # Currently supported compression algorithms
    modules_to_import = {
        'bz2': 'BZ2File',
        'gzip': 'GzipFile',
        'lzma': 'LZMAFile'
    }

    # Dynamically import compression libraries and warn about failures
    for mod, _class in modules_to_import.items():
        try:
            modules[_class] = getattr(import_module(mod), _class)
        except (ImportError, AttributeError) as e:
            modules[_class] = open
            warn('Cannot process {0} files due to following error:'
                 '{1}{2}{1}You will need to install the {0} library to '
                 'properly use these files. Currently, such files will '
                 'open in text mode.'.format(mod, linesep, e))

    # Write mode
    if write_mode is True:

        # Map file extensions to decompression classes
        algo_map = {
            'bz2': modules['BZ2File'],
            'gz':  modules['GzipFile'],
            'xz':  modules['LZMAFile']
        }

        # Determine the compression algorithm via the file extension
        ext = fileobj.split('.')[-1]
        try:
            algo = algo_map[ext]
        except KeyError:
            pass

    # Read mode
    else:

        algo = io.TextIOWrapper  # Default to plaintext buffer

        # Magic headers of encryption formats
        file_sigs = {
            b'\x42\x5a\x68': modules['BZ2File'],
            b'\x1f\x8b\x08': modules['GzipFile'],
            b'\xfd7zXZ\x00': modules['LZMAFile']
            }

        # Open the file, buffer it, and identify the compression algorithm
        fileobj = io.BufferedReader(io.open(fileobj, 'rb'))
        max_len = max(len(x) for x in file_sigs.keys())
        start = fileobj.peek(max_len)
        for sig in file_sigs.keys():
            if start.startswith(sig):
                algo = file_sigs[sig]
                break  # Stop iterating once a good signature is found

    # Filter all **kwargs by the args accepted by the compression algorithm
    algo_args = set(getfullargspec(algo).args)
    good_args = set(kwargs.keys()).intersection(algo_args)
    _kwargs = {arg: kwargs[arg] for arg in good_args}

    # Open the file using parameters defined above and store in namespace
    if write_mode is True:
        handle = algo(fileobj, **_kwargs)
    else:
        try:  # For algorithms that need to be explicitly given a fileobj
            handle = algo(fileobj=fileobj, **_kwargs)
        except TypeError:  # For algorithms that detect file objects
            handle = algo(fileobj, **_kwargs)

    return handle
