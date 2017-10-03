========
argparse
========

.. automodule:: arandomness.argparse

Introduction
------------

The ``argparse`` subpackage of arandomness contains scripts and actions to
expand the utility of Python's
`argparse <https://docs.python.org/3/library/argparse.html>`_
library.


CheckThreads
------------

CheckThreads is an
`argparse action <https://docs.python.org/3/library/argparse.html#action>`_,
as such, it is called as the value of the ``action`` argument in argparse. For
example:

.. code-block:: Python

    from arandomness.argparse import ThreadCheck
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-t', '--threads',
                        action=ThreadCheck,
                        type=int,
                        default=1,
                        help='number of threads to use')
    args = parser.parse_args()

When ``-t`` is parsed, the value is passed to ``ThreadCheck`` which then
checks that the value is between 1 and the maximum number of threads on the
computer as per
`multiprocessing.cpu_count() <https://docs.python.org/2/library/multiprocessing.html#multiprocessing.cpu_count>`_.

API Documentation
=================

.. autoclass:: arandomness.argparse.CheckThreads
   :members: __call__


ParseCommas
------------

By default, ``argparse`` parses multiple arguments by spaces. While useful,
it can sometimes be more practical, or at least easier to read, arguments
parsed by commas when multiple arguments make use of
`nargs <https://docs.python.org/3/library/argparse.html#nargs>`_.
``ParseCommas`` simply takes a string, splits it by commas, and sets the
resulting list as the value for the argument. For example:

.. code-block:: Python

    from arandomness.argparse import ParseCommas
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-a', '--an-argument',
                        action=ParseCommas,
                        type=str,
                        help='nargs using a string')
    args = parser.parse_args()

So the argument ``hello,world`` would be set as ``['hello', 'world']`` in args.

API Documentation
=================

.. autoclass:: arandomness.argparse.ParseCommas
   :members: __call__
