#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Inc., see LICENSE.txt
#------------------------------------------------------------------------------

import os, sys, setuptools
from setuptools import setup, find_packages

# require python 2.7+
if sys.hexversion < 0x02070000:
  raise RuntimeError('This package requires python 2.7 or better')

heredir = os.path.abspath(os.path.dirname(__file__))
def read(*parts, **kw):
  try:    return open(os.path.join(heredir, *parts)).read()
  except: return kw.get('default', '')

test_dependencies = [
  'nose                 >= 1.3.0',
  'coverage             >= 3.5.3',
]

dependencies = [
  'iniherit             >= 0.3.4',
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

classifiers = [
  'Development Status :: 4 - Beta',
  #'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Operating System :: OS Independent',
  'Natural Language :: English',
  'License :: OSI Approved :: MIT License',
  'License :: Public Domain',
]

setup(
  name                  = 'pyramid_iniherit',
  version               = read('VERSION.txt', default='0.0.1').strip(),
  description           = 'Enables pyramid configuration INI file inheritance via the "iniherit" package.',
  long_description      = read('README.rst'),
  classifiers           = classifiers,
  author                = 'Philip J Grabner, Cadit Health Inc',
  author_email          = 'oss@cadit.com',
  url                   = 'http://github.com/cadithealth/pyramid_iniherit',
  keywords              = 'pyramid configuration INI inheritance',
  packages              = find_packages(),
  platforms             = ['any'],
  include_package_data  = True,
  zip_safe              = True,
  install_requires      = dependencies,
  tests_require         = test_dependencies,
  test_suite            = 'pyramid_iniherit',
  entry_points          = entrypoints,
  license               = 'MIT (http://opensource.org/licenses/MIT)',
)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
