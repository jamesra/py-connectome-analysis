# .\neuroml\nml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fc073d58d4e38f3767ac54db3caddf39080791b0
# Generated 2013-10-11 13:54:11.899000 by PyXB version 1.1.4
# Namespace http://morphml.org/neuroml/schema

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e495aec0-32ae-11e3-bae7-001fbc00ed03')

# Import bindings for namespaces imported into schema
import neuroml._nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/neuroml/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)

from neuroml._nsgroup import neuroml # {http://morphml.org/neuroml/schema}neuroml
from neuroml._nsgroup import NeuroMLLevel3 # {http://morphml.org/neuroml/schema}NeuroMLLevel3
from neuroml._nsgroup import Level3Cells # {http://morphml.org/neuroml/schema}Level3Cells
from neuroml._nsgroup import Level3Cell # {http://morphml.org/neuroml/schema}Level3Cell
from neuroml._nsgroup import Level3Biophysics # {http://morphml.org/neuroml/schema}Level3Biophysics
