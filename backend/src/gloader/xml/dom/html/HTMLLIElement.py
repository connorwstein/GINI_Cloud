########################################################################
#
# File Name:            HTMLLIElement
#
#

### This file is automatically generated by GenerateHtml.py.
### DO NOT EDIT!

"""
WWW: http://4suite.com/4DOM         e-mail: support@4suite.com

Copyright (c) 2000 Fourthought Inc, USA.   All Rights Reserved.
See  http://4suite.com/COPYRIGHT  for license and copyright information
"""

import string
from xml.dom import Node
from xml.dom.html.HTMLElement import HTMLElement

class HTMLLIElement(HTMLElement):

    def __init__(self, ownerDocument, nodeName="LI"):
        HTMLElement.__init__(self, ownerDocument, nodeName)

    ### Attribute Methods ###

    def _get_type(self):
        return self.getAttribute("TYPE")

    def _set_type(self, value):
        self.setAttribute("TYPE", value)

    def _get_value(self):
        value = self.getAttribute("VALUE")
        if value:
            return int(value)
        return 0

    def _set_value(self, value):
        self.setAttribute("VALUE", str(value))

    ### Attribute Access Mappings ###

    _readComputedAttrs = HTMLElement._readComputedAttrs.copy()
    _readComputedAttrs.update({
        "type" : _get_type,
        "value" : _get_value
        })

    _writeComputedAttrs = HTMLElement._writeComputedAttrs.copy()
    _writeComputedAttrs.update({
        "type" : _set_type,
        "value" : _set_value
        })

    _readOnlyAttrs = filter(lambda k,m=_writeComputedAttrs: not m.has_key(k),
                     HTMLElement._readOnlyAttrs + _readComputedAttrs.keys())
