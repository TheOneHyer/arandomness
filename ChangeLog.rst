Changelog
=========


(unreleased)
------------
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


