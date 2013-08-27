# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

'''
Automatically installs the `iniherit` ConfigParsers as the default
ConfigParsers on import. WARNING: this is generally considered
"dangerous" -- use with extreme caution.

Also installs an adujsted Loader that adds all inherited files to the
:func:`pyramid.scripts.pserve.watch_file` list.
'''

# install overrides into ConfigParser
import iniherit

iniherit.mixin.install_globally()

# install a "watching" file loader
import iniherit.parser

if not hasattr(iniherit.parser, '_real_Loader'):
  iniherit.parser._real_Loader = iniherit.parser.Loader
  class WatchingLoader(iniherit.parser._real_Loader):
    def load(self, name, encoding=None):
      try:
        from pyramid.scripts.pserve import watch_file
        watch_file(name)
      except: pass
      return iniherit.parser._real_Loader.load(self, name, encoding)
  iniherit.parser.Loader = WatchingLoader

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
