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
__version__ = '0.1.0a4'


class OmniTree(object):
    """A many-to-many tree for organizing and manipulating hierarchical data

    Attributes:

        children (list): list of OmniTree instances that are children to this
                         node

        parents (list): list of OmniTree instances that are parents to this
                        node
    """

    def __init__(self, label, children=None, parents=None,):
        """Initialize node and inform connected nodes"""

        self._children = []
        self._parents = []
        self.label = label

        # Assign children and notify them if needed
        if children is not None:
            self._children = children
            for child in self._children:
                child.add_parent([self])

        # Assign parents and notify them if needed
        if parents is not None:
            self._parents = parents
            for parent in self._parents:
                parent.add_children([self])

    def add_children(self, children):
        """Adds new children nodes after filtering for duplicates

        Args:
            children (list): list of OmniTree nodes to add as children
        """

        self._children += [c for c in children if c not in self._children]

    def add_parents(self, parents):
        """Adds new parent nodes after filtering for duplicates

        Args:
            parents (list): list of OmniTree nodes to add as parents
        """

        self._parents += [p for p in parents if p not in self._parents]

    def find_branches(self):
        """"""

        branches = []
        if self._children == []:  # Current node is a leaf/end node
            return [self.label]
        else:
            for child in self._children:
                branches.append([self.label] + child.find_paths())
            return branches

    def find_unique_branches(self):
        """"""

        branches = []
        if self._children == []:  # Current node is a leaf/end node
            return [self.label]
        else:
            for child in self._children:
                for branch in child.find_paths():
                    branches.append([self.label] + branch)
            return branches
