#! /usr/bin/env python

"""A many-to-many tree with self-aware features

Copyright:
    omnitree.py  A many-to-many tree with self-aware features
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

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Planning'
__version__ = '0.1.0a1'


class OmniTree(object):
    """A many-to-many tree for organizing and manipulating related data

    Attributes:

        parents (list): list of OmniTree instances that are parents to this
                        instance
    """

    def __init__(self, parents):
        """"""

        self.children = []
        self.parents = parents

        for parent in parents:
            parent.add_child(self)
