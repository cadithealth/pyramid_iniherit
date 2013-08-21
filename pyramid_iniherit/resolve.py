# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

import sys
PY3 = sys.version_info[0] == 3

#------------------------------------------------------------------------------
if PY3:
  def isstr(obj):
    return isinstance(obj, str)
else:
  def isstr(obj):
    return isinstance(obj, basestring)

#------------------------------------------------------------------------------
def resolve(spec):
  if not isstr(spec):
    return spec
  if ':' in spec:
    spec, attr = spec.split(':', 1)
    return getattr(resolve(spec), attr)
  spec = spec.split('.')
  used = spec.pop(0)
  found = __import__(used)
  for cur in spec:
    used += '.' + cur
    try:
      found = getattr(found, cur)
    except AttributeError:
      __import__(used)
      found = getattr(found, cur)
  return found

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
