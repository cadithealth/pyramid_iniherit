# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import sys
from . import install

#------------------------------------------------------------------------------
def proxy(argv=sys.argv):
  pcmd = argv[0][argv[0].rindex('i-') + 2:]
  mod  = __import__('pyramid.scripts.' + pcmd)
  main = getattr(getattr(getattr(mod, 'scripts'), pcmd), 'main')
  return main(argv=argv)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
