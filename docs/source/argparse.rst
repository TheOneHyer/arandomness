========
argparse
========

.. automodule:: arandomness.argparse

Introduction
------------

The ``argparse`` subpackage of arandomness contains scripts and
`actions <https://docs.python.org/3/library/argparse.html#action>`_ to
expand the utility of Python's
`argparse <https://docs.python.org/3/library/argparse.html>`_
library.


CheckThreads
------------

``CheckThreads`` is an ``argparse`` ``action``, as such, it is called as the
value of the ``action`` argument in ``argparse``. For example:

.. code-block:: Python

    from arandomness.argparse import CheckThreads
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-t', '--threads',
                        action=CheckThreads,
                        type=int,
                        default=1,
                        help='number of threads to use')
    args = parser.parse_args()

When ``-t`` is parsed, the value is passed to ``CheckThreads`` which then
checks that the value is between 1 and the maximum number of threads on the
computer as per
`multiprocessing.cpu_count() <https://docs.python.org/2/library/multiprocessing.html#multiprocessing.cpu_count>`_.

API Documentation
=================

.. autoclass:: arandomness.argparse.CheckThreads
   :members: __call__


CopyRight
---------

``CopyRight`` is an ``argparse`` ``action`` that simply takes in text,
strips it of leading and trailing whitespace, prints it, and exits the
program. Its functionality is analogous to
``argparse``'s `version <https://docs.python.org/3/library/argparse
.html#action>`_. The action can take in arbitrary text and is only named
``CopyRight`` for code readability.

.. code-block:: Python

    from arandomness.argparse import CopyRight
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--copyright',
                        action=CopyRight,
                        copyright_text='This is my copyright',
                        help='print copyright and exit')
    args = parser.parse_args()

API Documentation
=================

.. autoclass:: arandomness.argparse.CopyRight
   :members: __call__


Open
----

``Open`` is an ``argparse`` ``action`` that seamlessly handles reading and
writing compressed files using the
`gzip <https://docs.python.org/2/library/gzip.html>`_,
`bz2 <https://docs.python.org/2/library/bz2.html>`_, and
`lzma <https://docs.python.org/3/library/lzma.html>`_ libraries. To do this,
``Open`` actually exposes the arguments of each to libraries ``*File``
function to the command line after automatically selecting the proper
library based on the arguments it receives. Essentially, this ``action``
operates in a read mode and a write/append mode. In read mode, when mode is
equal to any read mode supported by the appropriate library such as ``r`` or
``rb``, ``Open`` reads the first few bytes of the file to see what
compression format the file uses and then opens the file with the
corresponding in decompression algorithm. In write mode, basically when mode
is set to anything else, ``Open`` just checks the file extension and maps it
to the corresponding compression algorithm. If ``Open`` does not recognize
the first few bytes of a file or a file extension, it defaults to reading
and writing in plain text.

As aforementioned, ``Open`` exposes the arguments of the underlying library.
It does this by collecting arbitrary arguments, filtering them by the
supported arguments of the ``*File`` functions, and only passing those
arguments to the function. For example, ``GzipFile`` and ``BZ2File`` can
control the level on compression via the argument ``compresslevel`` while
``LZMAFile`` uses ``preset`` to control compression levels. In order to use
these arguments at the ``argparse`` level, simply add them as options to
``Open`` as follows:

.. code-block:: Python

    from arandomness.argparse import Open
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gzip',
                        action=Open,
                        mode='r',
                        type=str,
                        compresslevel=9,
                        help='compressed file to read')
    parser.add_argument('--bz2',
                        action=Open,
                        mode='w',
                        type=str,
                        compresslevel=9
                        help='compressed file to write')
    parser.add_argument('--lzma',
                        action=Open,
                        mode='w',
                        type=str,
                        preset=9,
                        help='compressed file to write')
    args = parser.parse_args(['-i', 'input.gz', '-o', 'output.xz'])

As stated, this works for any argument and arguments that aren't supported
by the ``*File`` are silently ignored.

Common use example:

.. code-block:: Python

    from arandomness.argparse import Open
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--input',
                        action=Open,
                        mode='r',
                        type=str,
                        help='compressed file to read')
    parser.add_argument('-o', '--output',
                        action=Open,
                        mode='w',
                        type=str,
                        help='compressed file to write')
    args = parser.parse_args(['-i', 'input.gz', '-o', 'output.xz'])

API Documentation
=================

.. autoclass:: arandomness.argparse.Open
   :members: __call__


ParseSeparator
------------

By default, ``argparse`` parses multiple arguments by spaces. While useful,
it can sometimes be more practical, or at least easier to read, arguments
parsed by commas or some other separator character when multiple arguments 
make use of `nargs <https://docs.python.org/3/library/argparse.html#nargs>`_.
``ParseSeparator`` simply takes a string, splits it by the user-defined 
separator, and sets the resulting list as the value for the argument. For 
example:

.. code-block:: Python

    from arandomness.argparse import ParseSeparator
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-a', '--an_argument',
                        action=ParseSeparator,
                        type=str,
                        sep=',',
                        help='nargs using a string')
    args = parser.parse_args(['hello,world'])
    print(args.an_argument)

So the argument ``hello,world`` would be set as ``['hello', 'world']`` in args.

API Documentation
=================

.. autoclass:: arandomness.argparse.ParseSeparator
   :members: __call__
