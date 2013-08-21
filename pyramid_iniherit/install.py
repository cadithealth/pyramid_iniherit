# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: Philip J Grabner <grabner@cadit.com>
# date: 2013/08/21
# copy: (C) Copyright 2013 Cadit Health Inc., All Rights Reserved.
#------------------------------------------------------------------------------

'''
Automatically installs the `iniherit` ConfigParsers as the default
ConfigParsers on import.  WARNING: this is generally considered
"dangerous" -- use with extreme caution.
'''

import iniherit
iniherit.mixin.install_globally()

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
