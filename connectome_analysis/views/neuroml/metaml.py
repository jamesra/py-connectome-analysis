# .\neuroml\metaml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:03502d70dd8209ce9fce5a0afde96422bc3961b3
# Generated 2013-09-19 16:53:37.909000 by PyXB version 1.2.2
# Namespace http://morphml.org/metadata/schema [xmlns:meta]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:b2b49440-2186-11e3-b32c-10bf480cb10f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _nsgroup as _ImportedBinding_neuroml__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/metadata/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from _nsgroup import Point  # {http://morphml.org/metadata/schema}Point
from _nsgroup import Point3D  # {http://morphml.org/metadata/schema}Point3D
from _nsgroup import Points  # {http://morphml.org/metadata/schema}Points
from _nsgroup import Sphere  # {http://morphml.org/metadata/schema}Sphere
from _nsgroup import RectangularBox  # {http://morphml.org/metadata/schema}RectangularBox
from _nsgroup import CTD_ANON_ as CTD_ANON  # None
from _nsgroup import NonSpatialGrid  # {http://morphml.org/metadata/schema}NonSpatialGrid
from _nsgroup import Polyhedron  # {http://morphml.org/metadata/schema}Polyhedron
from _nsgroup import CTD_ANON_2 as CTD_ANON_  # None
from _nsgroup import Annotation  # {http://morphml.org/metadata/schema}Annotation
from _nsgroup import LengthUnits  # {http://morphml.org/metadata/schema}LengthUnits
from _nsgroup import VolumeUnits  # {http://morphml.org/metadata/schema}VolumeUnits
from _nsgroup import SegmentIdInCell  # {http://morphml.org/metadata/schema}SegmentIdInCell
from _nsgroup import Notes  # {http://morphml.org/metadata/schema}Notes
from _nsgroup import Group  # {http://morphml.org/metadata/schema}Group
from _nsgroup import Property  # {http://morphml.org/metadata/schema}Property
from _nsgroup import Properties  # {http://morphml.org/metadata/schema}Properties
from _nsgroup import PropertyDetail  # {http://morphml.org/metadata/schema}PropertyDetail
from _nsgroup import GroupDetail  # {http://morphml.org/metadata/schema}GroupDetail
from _nsgroup import YesNo  # {http://morphml.org/metadata/schema}YesNo
from _nsgroup import ZeroToOne  # {http://morphml.org/metadata/schema}ZeroToOne
from _nsgroup import Percentage  # {http://morphml.org/metadata/schema}Percentage
from _nsgroup import NonNegativeDouble  # {http://morphml.org/metadata/schema}NonNegativeDouble
from _nsgroup import PositiveDouble  # {http://morphml.org/metadata/schema}PositiveDouble
from _nsgroup import Units  # {http://morphml.org/metadata/schema}Units
from _nsgroup import NeuroMorphoRef  # {http://morphml.org/metadata/schema}NeuroMorphoRef
from _nsgroup import NeuronDBReference  # {http://morphml.org/metadata/schema}NeuronDBReference
from _nsgroup import ModelDBReference  # {http://morphml.org/metadata/schema}ModelDBReference
from _nsgroup import Publication  # {http://morphml.org/metadata/schema}Publication
from _nsgroup import Authors  # {http://morphml.org/metadata/schema}Authors
from _nsgroup import Person  # {http://morphml.org/metadata/schema}Person
from _nsgroup import StatusValue  # {http://morphml.org/metadata/schema}StatusValue
from _nsgroup import Manifold  # {http://morphml.org/metadata/schema}Manifold
from _nsgroup import Polygon  # {http://morphml.org/metadata/schema}Polygon
from _nsgroup import Status  # {http://morphml.org/metadata/schema}Status
