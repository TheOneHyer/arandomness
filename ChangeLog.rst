Changelog
=========


(unreleased)
------------
- Added Documentation and Examples to copen. [TheOneHyer]
- Renamed files Open to copen. [TheOneHyer]

  The Open class of the files subpackage has not been renamed to copen
  across the board to improve readability of code.
- Examples Added to COpen. [TheOneHyer]

  COpen now has a working read and write example.
- Streamlined COpen Codebase. [TheOneHyer]

  Excess code removed from COpen.
- Renamed Open to COpen and Removed Redundant Code. [TheOneHyer]

  Open in argparse subpackage is now called COpen to improve readability
  of code. COpen now calls Open from files, which also needs a rename.
- Fixed files Open. [TheOneHyer]

  The files subpackage Open is now passing tests.
  As is, it appears to work, but it needs to be tested
  for the ability to work while streaming. All versions
  now moved to beta as a result.
- Added files Subpackage and Open. [TheOneHyer]

  Added a new subpackage called files with the
  module Open. These are for steps regarding both
  supporting and streams and increasing the
  apllicability of Open.
- Streamlined Open Code. [TheOneHyer]

  Open's code now has less redundancy and more documentation.
  More testing for piping support is needed in test_Open.
- Added BUffering to Open. [TheOneHyer]

  Open now buffers read mode input with the goal
  of eventually supporting piping. These current changes
  past py.test but will require more testing.
- Renamed string Subpackage to str. [TheOneHyer]

  In compliance with arandomness only supporting Python 3.X,
  the string package has been renamed to str. This more clearly
  communicates that this subpackage extends Python 3's str
  libraries and not bytes.
- Changed to Alpha Version. [TheOneHyer]
- Merge pull request #1 from cnthornton/master. [Alex Hyer]

  Mods to ParseCommas and Open argparse extensions - will be edited quickly
- Fixed ParseSeparator testing script. [Christopher Thornton]
- Added support for piping in Open.py. [Christopher Thornton]
- Renamed and generalized ParseCommas so that it will split arguments by
  any arbitray character. [Christopher Thornton]
- Released Version 0.1.0. [TheOneHyer]


0.1.0 (2017-11-16)
------------------
- Finished Open, test_Open, and Open Documentation. [TheOneHyer]

  Finished Open function, unit tests, and RTD documentation
  for Open.
- Added Open and test_Open. [TheOneHyer]

  Added Open, the argparse action for opening and writing to multiple
  compressed file types seemlessly. Added test for gzip functionality,
  which worked. Still need to test other compressed formats and add
  documentation.
- Added Open Alpha. [TheOneHyer]

  Added new Argparse Action for opening compressed files.
  I'm totally abusing rc versioning.
- Fixed Typo in CopyRight Documentation. [TheOneHyer]
- Added Documentation for CopyRight on RTD. [TheOneHyer]
- Added CopyRight. [TheOneHyer]

  CopyRight added to print copyright messages and exit. Has a
  working unit test. Upped version numbers of small __init__s.
- Updated OmniTree Docs. [TheOneHyer]

  OmniTree RTD updated.
- OmniTree: Deprecated. [TheOneHyer]

  OmniTree now deprecated because it is basically a graph.
- Updated Documentation of OmniTree. [TheOneHyer]

  Added some more documentation and spruced up the rest
  on OmniTree.
- OmniTree: Finalized find_branches. [TheOneHyer]

  OmniTree find_branches now contains the find_branches
  and find_unique_branches functions rolled into one.
  Contains 'labels' and 'unique' options to control
  the functions behavior.
- Added find_loops to OmniTree. [TheOneHyer]

  OmniTree can now identify loops.
- Changed ThreadCheck to CheckThreads in Docs. [TheOneHyer]

  Documentation had incorrect class name.
- Added Branch Function to OmniTree. [TheOneHyer]

  OmniTree now has beta-testing functions for finding and return
  tree structure. These methods are not yet final.
- Added Documentation to argparse and omnitree. [TheOneHyer]

  OmniTree, CheckThreads, and ParseCommas have additional
  and/or rearranged docs.
- Added add_children and add_parents to OmniTree. [TheOneHyer]

  OmntiTree now has methods for attaching additional nodes
  and avoiding duplciate node entries.
- Changed conf.py and Added OmniTree Skeleton. [TheOneHyer]

  OmntiTree now has some skeletal code. conf.py altered to make
  docs look better.
- Finished string.rst. [TheOneHyer]

  string subpackaged now documented.
- Changed Example Code. [TheOneHyer]

  Docstrings example now have RST formatting for better rendering.
- Added argparse.rst. [TheOneHyer]

  Argparse subpackage docs now complete.
- Added Trees Package. [TheOneHyer]

  Created tress __init__ and empty omnitree.
- Added index.rst. [TheOneHyer]

  Made proper front page to docs.
- Added Sphinx Skeleton. [TheOneHyer]

  Sphinx config created to provided basis for docs.
- Fixed test_autocorrect import. [TheOneHyer]

  imports in __init__ of string are rearranged
  to prevent conflict. test_autocorrect and
  autocorrect now work properly.
- Added autocorrect and unit test. [TheOneHyer]

  autocorrect funtion added. It's unit test works except
  for a weird problem with relative imports.
- Added string subpackage and max_substring. [TheOneHyer]

  Added string package for string-related functions
  with max_substring function. Unit test for
  max_substring added adn functional.
- Added CheckThreads and unit test. [TheOneHyer]

  CheckThreads ensures users use a valid number of threads.
  Unit test fully functional.
- Added test_ParseCommas. [TheOneHyer]

  Added first unit test, test_ParseCommas works with
  py.test.
- Added tests and argparse packages. [TheOneHyer]

  Added two packages with __init__ and a single
  module, ParseCommas, for later testing.
- Added .gitignore. [TheOneHyer]
- Fixed setup.py. [TheOneHyer]
- Fixed setup.py. [TheOneHyer]
- Fixed setup.py. [TheOneHyer]
- Added setup.py. [TheOneHyer]
- Initial commit. [Alex Hyer]


