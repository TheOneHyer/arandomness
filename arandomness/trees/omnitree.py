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
__version__ = '0.1.0a2'


class OmniTree(object):
    """A many-to-many tree for organizing and manipulating hierarchical data

    Attributes:

        children (list): list of OmniTree instances that are children to this
                         node

        parents (list): list of OmniTree instances that are parents to this
                        node
    """

    def __init__(self, children=None, parents=None,):
        """Initialize node and inform connected nodes

        Args:
            children (list): list of OmniTree instances to set as children of
                             this node at initialization

            parents (list): list of OmniTree instances to set as parents of
                            this node at initialization
        """

        self.children = []
        self.parents = []

        if children is not None:
            self.children = children
            for child in self.children:
                child.add_parent([self])

        if parents is not None:
            self.parents = parents
            for parent in self.parents:
                parent.add_children([self])

    def add_children(self, children):
        """Adds new children nodes after filtering for duplicates

        Args:
            children (list): list of OmniTree nodes to add as children
        """

        self.children += [c for c in children if c not in self.children]

    def add_parents(self, parents):
        """Adds new parent nodes after filtering for duplicates

        Args:
            parents (list): list of OmniTree nodes to add as parents
        """

        self.parents += [p for p in parents if p not in self.parents]
