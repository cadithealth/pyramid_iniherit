# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import sys
from . import install
from resolve import resolve

#------------------------------------------------------------------------------
def proxy(argv=sys.argv):
  pcmd = argv[0][argv[0].rindex('i-') + 2:]
  return resolve('pyramid.scripts.' + pcmd + ':main')(argv=argv)

#------------------------------------------------------------------------------
def pscheduler():
  return resolve('pyramid_scheduler.pscheduler:main')()

#------------------------------------------------------------------------------
def alembic():
  return resolve('alembic.config:main')()

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
