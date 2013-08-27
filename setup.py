#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Inc., see LICENSE.txt
#------------------------------------------------------------------------------

import os, sys, setuptools
from setuptools import setup

# require python 2.7+
assert(sys.version_info[0] > 2
       or sys.version_info[0] == 2
       and sys.version_info[1] >= 7)

here = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
  try:    return open(os.path.join(here, *parts)).read()
  except: return ''

test_requires = [
  'nose                 >= 1.2.1',
  'coverage             >= 3.5.3',
  ]

requires = [
  'distribute           >= 0.6.24',
  'iniherit             >= 0.1.6',
  'pyramid              >= 1.4.2',
  ]

entrypoints = {
  'console_scripts': [
    'i-pserve           = pyramid_iniherit.scripts:proxy',
    'i-pshell           = pyramid_iniherit.scripts:proxy',
    'i-proutes          = pyramid_iniherit.scripts:proxy',
    'i-pviews           = pyramid_iniherit.scripts:proxy',
    'i-ptweens          = pyramid_iniherit.scripts:proxy',
    'i-prequest         = pyramid_iniherit.scripts:proxy',
    'i-pscheduler       = pyramid_iniherit.scripts:pscheduler',
    'i-alembic          = pyramid_iniherit.scripts:alembic',
    ],
  }

setup(
  name                  = 'pyramid_iniherit',
  version               = '0.1.7',
  description           = '',
  long_description      = read('README.rst'),
  classifiers           = [
    'Development Status :: 4 - Beta',
    #'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'License :: Public Domain',
    ],
  author                = 'Philip J Grabner, Cadit Health Inc',
  author_email          = 'oss@cadit.com',
  url                   = 'http://github.com/cadithealth/pyramid_iniherit',
  keywords              = 'pyramid configuration INI inheritance',
  packages              = setuptools.find_packages(),
  include_package_data  = True,
  zip_safe              = True,
  install_requires      = requires,
  tests_require         = test_requires,
  test_suite            = 'pyramid_iniherit',
  entry_points          = entrypoints,
  license               = 'MIT (http://opensource.org/licenses/MIT)',
  )

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
