======
string
======

.. automodule:: arandomness.string

Introduction
------------

The ``string`` subpackage of arandomness contains a couple functions that
analyze or manipulate strings in some way. That's about as specific as this
subpackage gets. Enjoy!

autocorrect
-----------

The ``autocorrect`` function takes a single query string and a list of
"correct" strings and identifies which string in the list the query most
closely matches. There are many far more robust autocorrect algorithms
written in Python than this one, but they all require a list of words
organized by their frequency in a given language. Basically, these
autocorrect algorithms are aimed at correcting words specific to a language and
are thus better suited for use in language processing software, e.g. texting
apps. This algorithm uses any list of strings and is order-agnostic. Thus,
my ``autocorrect`` is better suited for attempting to match queries to small
lists of arbitrary strings.

To help realize this concept, I have used
this function in a program that presented data in a database about programs
available on a given system. The query was the user's request and the
possible strings was simply the list of program names in the database. Thus,
if a user misspelled a program name, the program likely produced the proper
entry.


API Documentation
=================

.. autofunction:: arandomness.string.autocorrect


max_substring
-------------

The ``max_substring`` function takes in a list of strings and finds the
longest substring that they all share. By default, ``max_substring`` starts
at the beginning of each string, but it can be optionally start at a
later position as demonstrated in the docstring examples.

API Documentation
=================

.. autofunction:: arandomness.string.max_substring
