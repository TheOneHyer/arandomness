.. arandomness documentation master file, created by
   sphinx-quickstart on Mon Oct  2 13:29:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================================
arandomness: an arandom assortment of random modules
====================================================

:Authors: Alex Hyer
:Date: |today|
:Version: |version|

.. image:: images/arandomness_logo_160.png

.. automodule:: arandomness


Introduction
============

arandomness is a package containing modules that I find myself re-writing for
many programs. I've organized these modules into this amalgamative package as
they are generally too diverse to fit into independent libraries. In
general, I find the modules in arandomness to be very useful for many
unrelated applications and wished to have them readily accessible in a
unified, production-level library with proper unit tests. I hope you find
something in this library useful!


Installation
============

::

    pip install arandomness


Contents
========

.. toctree::
   :maxdepth: 2

   argparse.rst
   str.rst
   trees.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


Copyright
=========

arandomness operates under the :download:`GPLv3 License <LICENSE.txt>` and may
be edited and redistributed as per that license.
