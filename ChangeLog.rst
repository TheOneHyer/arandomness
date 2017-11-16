Changelog
=========


(unreleased)
------------
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


