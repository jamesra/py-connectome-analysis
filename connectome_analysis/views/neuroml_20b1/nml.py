# .\nml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d7b033b75eceea8c86821a4d9e6decb1e67b2355
# Generated 2013-09-23 10:28:39.371000 by PyXB version 1.2.2
# Namespace http://www.neuroml.org/schema/neuroml2

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:95259a8f-2475-11e3-9d0b-10bf480cb10f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.neuroml.org/schema/neuroml2', create_if_missing=True)
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


# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}NmlId
class NmlId (pyxb.binding.datatypes.string):

    """An id attribute for elements which need to be identified uniquely (normally just within their parent element)."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NmlId')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 16, 4)
    _Documentation = u'An id attribute for elements which need to be identified uniquely (normally just within their parent element).'
NmlId._CF_pattern = pyxb.binding.facets.CF_pattern()
NmlId._CF_pattern.addPattern(pattern=u'[a-zA-Z0-9_]*')
NmlId._InitializeFacetMap(NmlId._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'NmlId', NmlId)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity
class Nml2Quantity (pyxb.binding.datatypes.string):

    """A value for a physical quantity in NeuroML 2, e.g. 20, -60.0mV or 5nA"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 27, 4)
    _Documentation = u'A value for a physical quantity in NeuroML 2, e.g. 20, -60.0mV or 5nA'
Nml2Quantity._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*([_a-zA-Z0-9])*')
Nml2Quantity._InitializeFacetMap(Nml2Quantity._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity', Nml2Quantity)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_none
class Nml2Quantity_none (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_none')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 38, 4)
    _Documentation = None
Nml2Quantity_none._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_none._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?')
Nml2Quantity_none._InitializeFacetMap(Nml2Quantity_none._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_none', Nml2Quantity_none)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_voltage
class Nml2Quantity_voltage (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_voltage')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 46, 4)
    _Documentation = None
Nml2Quantity_voltage._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_voltage._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(V|mV)')
Nml2Quantity_voltage._InitializeFacetMap(Nml2Quantity_voltage._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_voltage', Nml2Quantity_voltage)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_length
class Nml2Quantity_length (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_length')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 54, 4)
    _Documentation = None
Nml2Quantity_length._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_length._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(m|cm|um)')
Nml2Quantity_length._InitializeFacetMap(Nml2Quantity_length._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_length', Nml2Quantity_length)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_resistance
class Nml2Quantity_resistance (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_resistance')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 62, 4)
    _Documentation = None
Nml2Quantity_resistance._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_resistance._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(ohm|Kohm|Mohm)')
Nml2Quantity_resistance._InitializeFacetMap(Nml2Quantity_resistance._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_resistance', Nml2Quantity_resistance)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_conductance
class Nml2Quantity_conductance (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_conductance')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 70, 4)
    _Documentation = None
Nml2Quantity_conductance._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_conductance._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(S|mS|uS|nS|pS)')
Nml2Quantity_conductance._InitializeFacetMap(Nml2Quantity_conductance._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_conductance', Nml2Quantity_conductance)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_conductanceDensity
class Nml2Quantity_conductanceDensity (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_conductanceDensity')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 78, 4)
    _Documentation = None
Nml2Quantity_conductanceDensity._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_conductanceDensity._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(S_per_m2|mS_per_cm2|S_per_cm2)')
Nml2Quantity_conductanceDensity._InitializeFacetMap(Nml2Quantity_conductanceDensity._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_conductanceDensity', Nml2Quantity_conductanceDensity)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_time
class Nml2Quantity_time (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_time')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 86, 4)
    _Documentation = None
Nml2Quantity_time._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_time._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(s|ms)')
Nml2Quantity_time._InitializeFacetMap(Nml2Quantity_time._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_time', Nml2Quantity_time)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_pertime
class Nml2Quantity_pertime (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_pertime')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 94, 4)
    _Documentation = None
Nml2Quantity_pertime._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_pertime._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(per_s|per_ms|Hz)')
Nml2Quantity_pertime._InitializeFacetMap(Nml2Quantity_pertime._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_pertime', Nml2Quantity_pertime)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_capacitance
class Nml2Quantity_capacitance (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_capacitance')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 102, 4)
    _Documentation = None
Nml2Quantity_capacitance._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_capacitance._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(F|uF|nF|pF)')
Nml2Quantity_capacitance._InitializeFacetMap(Nml2Quantity_capacitance._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_capacitance', Nml2Quantity_capacitance)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_specificCapacitance
class Nml2Quantity_specificCapacitance (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_specificCapacitance')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 110, 4)
    _Documentation = None
Nml2Quantity_specificCapacitance._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_specificCapacitance._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(F_per_m2|uF_per_cm2)')
Nml2Quantity_specificCapacitance._InitializeFacetMap(Nml2Quantity_specificCapacitance._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_specificCapacitance', Nml2Quantity_specificCapacitance)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_concentration
class Nml2Quantity_concentration (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_concentration')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 118, 4)
    _Documentation = None
Nml2Quantity_concentration._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_concentration._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(mol_per_m3|mol_per_cm3|M|mM)')
Nml2Quantity_concentration._InitializeFacetMap(Nml2Quantity_concentration._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_concentration', Nml2Quantity_concentration)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_current
class Nml2Quantity_current (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_current')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 126, 4)
    _Documentation = None
Nml2Quantity_current._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_current._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(A|uA|nA|pA)')
Nml2Quantity_current._InitializeFacetMap(Nml2Quantity_current._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_current', Nml2Quantity_current)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Nml2Quantity_temperature
class Nml2Quantity_temperature (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Nml2Quantity_temperature')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 134, 4)
    _Documentation = None
Nml2Quantity_temperature._CF_pattern = pyxb.binding.facets.CF_pattern()
Nml2Quantity_temperature._CF_pattern.addPattern(pattern=u'-?([0-9]*(\\.[0-9]+)?)([eE]-?[0-9]+)?[\\s]*(degC)')
Nml2Quantity_temperature._InitializeFacetMap(Nml2Quantity_temperature._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'Nml2Quantity_temperature', Nml2Quantity_temperature)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}MetaId
class MetaId (pyxb.binding.datatypes.string):

    """An id string for pointing to an entry in an annotation element related to a MIRIAM resource. Based on metaid of SBML"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MetaId')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 143, 4)
    _Documentation = u'An id string for pointing to an entry in an annotation element related to a MIRIAM resource. Based on metaid of SBML'
MetaId._CF_pattern = pyxb.binding.facets.CF_pattern()
MetaId._CF_pattern.addPattern(pattern=u'[a-zA-Z0-9_]*')
MetaId._InitializeFacetMap(MetaId._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'MetaId', MetaId)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}NeuroLexId
class NeuroLexId (pyxb.binding.datatypes.string):

    """An id string for pointing to an entry in the NeuroLex ontology. Use of this attribute is a shorthand for a full
            RDF based reference to the MIRIAM Resource urn:miriam:neurolex, with an bqbiol:is qualifier
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NeuroLexId')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 155, 4)
    _Documentation = u'An id string for pointing to an entry in the NeuroLex ontology. Use of this attribute is a shorthand for a full\n            RDF based reference to the MIRIAM Resource urn:miriam:neurolex, with an bqbiol:is qualifier\n            '
NeuroLexId._CF_pattern = pyxb.binding.facets.CF_pattern()
NeuroLexId._CF_pattern.addPattern(pattern=u'[a-zA-Z0-9_]*')
NeuroLexId._InitializeFacetMap(NeuroLexId._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'NeuroLexId', NeuroLexId)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}SegmentId
class SegmentId (pyxb.binding.datatypes.nonNegativeInteger):

    """An id attribute for segments: integer >=0 only!"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SegmentId')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 169, 4)
    _Documentation = u'An id attribute for segments: integer >=0 only!'
SegmentId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'SegmentId', SegmentId)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Notes
class Notes (pyxb.binding.datatypes.string):

    """Textual human readable notes related to the element in question. It's useful to put these into
         the NeuroML files instead of XML comments, as the notes can be extracted and repeated in the files to which the NeuroML is mapped.
            """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Notes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 191, 4)
    _Documentation = u"Textual human readable notes related to the element in question. It's useful to put these into\n         the NeuroML files instead of XML comments, as the notes can be extracted and repeated in the files to which the NeuroML is mapped.\n            "
Notes._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'Notes', Notes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}ZeroToOne
class ZeroToOne (pyxb.binding.datatypes.double):

    """Double restricted to between 1 and 0"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ZeroToOne')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 225, 4)
    _Documentation = u'Double restricted to between 1 and 0'
ZeroToOne._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ZeroToOne, value=pyxb.binding.datatypes.double(1.0))
ZeroToOne._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ZeroToOne, value=pyxb.binding.datatypes.double(0.0))
ZeroToOne._InitializeFacetMap(ZeroToOne._CF_maxInclusive,
   ZeroToOne._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ZeroToOne', ZeroToOne)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}channelTypes
class channelTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'channelTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 435, 4)
    _Documentation = None
channelTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=channelTypes, enum_prefix=None)
channelTypes.ionChannelPassive = channelTypes._CF_enumeration.addEnumeration(unicode_value=u'ionChannelPassive', tag=u'ionChannelPassive')
channelTypes.ionChannelHH = channelTypes._CF_enumeration.addEnumeration(unicode_value=u'ionChannelHH', tag=u'ionChannelHH')
channelTypes.ionChannelKS = channelTypes._CF_enumeration.addEnumeration(unicode_value=u'ionChannelKS', tag=u'ionChannelKS')
channelTypes._InitializeFacetMap(channelTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'channelTypes', channelTypes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}gateTypes
class gateTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'gateTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 444, 4)
    _Documentation = None
gateTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=gateTypes, enum_prefix=None)
gateTypes.gateHHrates = gateTypes._CF_enumeration.addEnumeration(unicode_value=u'gateHHrates', tag=u'gateHHrates')
gateTypes.gateHHratesTau = gateTypes._CF_enumeration.addEnumeration(unicode_value=u'gateHHratesTau', tag=u'gateHHratesTau')
gateTypes.gateHHtauInf = gateTypes._CF_enumeration.addEnumeration(unicode_value=u'gateHHtauInf', tag=u'gateHHtauInf')
gateTypes.gateHHratesInf = gateTypes._CF_enumeration.addEnumeration(unicode_value=u'gateHHratesInf', tag=u'gateHHratesInf')
gateTypes.gateKS = gateTypes._CF_enumeration.addEnumeration(unicode_value=u'gateKS', tag=u'gateKS')
gateTypes._InitializeFacetMap(gateTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'gateTypes', gateTypes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}BlockTypes
class BlockTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BlockTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 662, 4)
    _Documentation = None
BlockTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BlockTypes, enum_prefix=None)
BlockTypes.voltageConcDepBlockMechanism = BlockTypes._CF_enumeration.addEnumeration(unicode_value=u'voltageConcDepBlockMechanism', tag=u'voltageConcDepBlockMechanism')
BlockTypes._InitializeFacetMap(BlockTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BlockTypes', BlockTypes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}PlasticityTypes
class PlasticityTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PlasticityTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 680, 4)
    _Documentation = None
PlasticityTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PlasticityTypes, enum_prefix=None)
PlasticityTypes.tsodyksMarkramDepMechanism = PlasticityTypes._CF_enumeration.addEnumeration(unicode_value=u'tsodyksMarkramDepMechanism', tag=u'tsodyksMarkramDepMechanism')
PlasticityTypes.tsodyksMarkramDepFacMechanism = PlasticityTypes._CF_enumeration.addEnumeration(unicode_value=u'tsodyksMarkramDepFacMechanism', tag=u'tsodyksMarkramDepFacMechanism')
PlasticityTypes._InitializeFacetMap(PlasticityTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PlasticityTypes', PlasticityTypes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}Metric
class Metric (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Allowed metrics for InhomogeneousParam"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Metric')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 908, 4)
    _Documentation = u'Allowed metrics for InhomogeneousParam'
Metric._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Metric, enum_prefix=None)
Metric.Path_Length_from_root = Metric._CF_enumeration.addEnumeration(unicode_value=u'Path Length from root', tag=u'Path_Length_from_root')
Metric._InitializeFacetMap(Metric._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'Metric', Metric)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}networkTypes
class networkTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'networkTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1381, 4)
    _Documentation = None
networkTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=networkTypes, enum_prefix=None)
networkTypes.network = networkTypes._CF_enumeration.addEnumeration(unicode_value=u'network', tag=u'network')
networkTypes.networkWithTemperature = networkTypes._CF_enumeration.addEnumeration(unicode_value=u'networkWithTemperature', tag=u'networkWithTemperature')
networkTypes._InitializeFacetMap(networkTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'networkTypes', networkTypes)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}allowedSpaces
class allowedSpaces (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'allowedSpaces')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1413, 4)
    _Documentation = None
allowedSpaces._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=allowedSpaces, enum_prefix=None)
allowedSpaces.Euclidean_1D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Euclidean_1D', tag=u'Euclidean_1D')
allowedSpaces.Euclidean_2D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Euclidean_2D', tag=u'Euclidean_2D')
allowedSpaces.Euclidean_3D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Euclidean_3D', tag=u'Euclidean_3D')
allowedSpaces.Grid_1D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Grid_1D', tag=u'Grid_1D')
allowedSpaces.Grid_2D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Grid_2D', tag=u'Grid_2D')
allowedSpaces.Grid_3D = allowedSpaces._CF_enumeration.addEnumeration(unicode_value=u'Grid_3D', tag=u'Grid_3D')
allowedSpaces._InitializeFacetMap(allowedSpaces._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'allowedSpaces', allowedSpaces)

# Atomic simple type: {http://www.neuroml.org/schema/neuroml2}populationTypes
class populationTypes (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'populationTypes')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1466, 4)
    _Documentation = None
populationTypes._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=populationTypes, enum_prefix=None)
populationTypes.population = populationTypes._CF_enumeration.addEnumeration(unicode_value=u'population', tag=u'population')
populationTypes.populationList = populationTypes._CF_enumeration.addEnumeration(unicode_value=u'populationList', tag=u'populationList')
populationTypes._InitializeFacetMap(populationTypes._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'populationTypes', populationTypes)

# Complex type {http://www.neuroml.org/schema/neuroml2}Annotation with content type ELEMENT_ONLY
class Annotation (pyxb.binding.basis.complexTypeDefinition):
    """Placeholder for MIRIAM related metadata, among others."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Annotation')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 201, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Annotation', Annotation)


# Complex type {http://www.neuroml.org/schema/neuroml2}ComponentType with content type ELEMENT_ONLY
class ComponentType (pyxb.binding.basis.complexTypeDefinition):
    """Contains an extension to NeuroML by creating custom LEMS ComponentType."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ComponentType')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 210, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_neuroml_orgschemaneuroml2_ComponentType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 218, 8)
    __name._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 218, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute extends uses Python identifier extends
    __extends = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'extends'), 'extends', '__httpwww_neuroml_orgschemaneuroml2_ComponentType_extends', pyxb.binding.datatypes.string)
    __extends._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 219, 8)
    __extends._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 219, 8)
    
    extends = property(__extends.value, __extends.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpwww_neuroml_orgschemaneuroml2_ComponentType_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 220, 8)
    __description._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 220, 8)
    
    description = property(__description.value, __description.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name,
        __extends.name() : __extends,
        __description.name() : __description
    })
Namespace.addCategoryObject('typeBinding', u'ComponentType', ComponentType)


# Complex type {http://www.neuroml.org/schema/neuroml2}IncludeType with content type MIXED
class IncludeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IncludeType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IncludeType')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 295, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'href'), 'href', '__httpwww_neuroml_orgschemaneuroml2_IncludeType_href', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 296, 8)
    __href._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 296, 8)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
Namespace.addCategoryObject('typeBinding', u'IncludeType', IncludeType)


# Complex type {http://www.neuroml.org/schema/neuroml2}Point3DWithDiam with content type EMPTY
class Point3DWithDiam (pyxb.binding.basis.complexTypeDefinition):
    """A 3D point with diameter."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Point3DWithDiam')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 863, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpwww_neuroml_orgschemaneuroml2_Point3DWithDiam_x', pyxb.binding.datatypes.double, required=True)
    __x._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 867, 8)
    __x._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 867, 8)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpwww_neuroml_orgschemaneuroml2_Point3DWithDiam_y', pyxb.binding.datatypes.double, required=True)
    __y._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 868, 8)
    __y._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 868, 8)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpwww_neuroml_orgschemaneuroml2_Point3DWithDiam_z', pyxb.binding.datatypes.double, required=True)
    __z._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 869, 8)
    __z._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 869, 8)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute diameter uses Python identifier diameter
    __diameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'diameter'), 'diameter', '__httpwww_neuroml_orgschemaneuroml2_Point3DWithDiam_diameter', pyxb.binding.datatypes.double, required=True)
    __diameter._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 870, 8)
    __diameter._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 870, 8)
    
    diameter = property(__diameter.value, __diameter.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z,
        __diameter.name() : __diameter
    })
Namespace.addCategoryObject('typeBinding', u'Point3DWithDiam', Point3DWithDiam)


# Complex type {http://www.neuroml.org/schema/neuroml2}ProximalDetails with content type EMPTY
class ProximalDetails (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ProximalDetails with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProximalDetails')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 918, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute translationStart uses Python identifier translationStart
    __translationStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'translationStart'), 'translationStart', '__httpwww_neuroml_orgschemaneuroml2_ProximalDetails_translationStart', pyxb.binding.datatypes.double, required=True)
    __translationStart._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 919, 8)
    __translationStart._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 919, 8)
    
    translationStart = property(__translationStart.value, __translationStart.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __translationStart.name() : __translationStart
    })
Namespace.addCategoryObject('typeBinding', u'ProximalDetails', ProximalDetails)


# Complex type {http://www.neuroml.org/schema/neuroml2}DistalDetails with content type EMPTY
class DistalDetails (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}DistalDetails with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DistalDetails')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 922, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute normalizationEnd uses Python identifier normalizationEnd
    __normalizationEnd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'normalizationEnd'), 'normalizationEnd', '__httpwww_neuroml_orgschemaneuroml2_DistalDetails_normalizationEnd', pyxb.binding.datatypes.double, required=True)
    __normalizationEnd._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 923, 8)
    __normalizationEnd._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 923, 8)
    
    normalizationEnd = property(__normalizationEnd.value, __normalizationEnd.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __normalizationEnd.name() : __normalizationEnd
    })
Namespace.addCategoryObject('typeBinding', u'DistalDetails', DistalDetails)


# Complex type {http://www.neuroml.org/schema/neuroml2}Path with content type ELEMENT_ONLY
class Path (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Path with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Path')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 934, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}from uses Python identifier from_
    __from = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpwww_neuroml_orgschemaneuroml2_Path_httpwww_neuroml_orgschemaneuroml2from', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 936, 12), )

    
    from_ = property(__from.value, __from.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}to uses Python identifier to
    __to = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpwww_neuroml_orgschemaneuroml2_Path_httpwww_neuroml_orgschemaneuroml2to', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 937, 12), )

    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        __from.name() : __from,
        __to.name() : __to
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Path', Path)


# Complex type {http://www.neuroml.org/schema/neuroml2}SubTree with content type ELEMENT_ONLY
class SubTree (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SubTree with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SubTree')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 941, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}from uses Python identifier from_
    __from = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpwww_neuroml_orgschemaneuroml2_SubTree_httpwww_neuroml_orgschemaneuroml2from', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 943, 12), )

    
    from_ = property(__from.value, __from.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}to uses Python identifier to
    __to = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpwww_neuroml_orgschemaneuroml2_SubTree_httpwww_neuroml_orgschemaneuroml2to', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 944, 12), )

    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        __from.name() : __from,
        __to.name() : __to
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SubTree', SubTree)


# Complex type {http://www.neuroml.org/schema/neuroml2}MembraneProperties with content type ELEMENT_ONLY
class MembraneProperties (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}MembraneProperties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MembraneProperties')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 979, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}channelPopulation uses Python identifier channelPopulation
    __channelPopulation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'channelPopulation'), 'channelPopulation', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2channelPopulation', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 983, 12), )

    
    channelPopulation = property(__channelPopulation.value, __channelPopulation.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}channelDensity uses Python identifier channelDensity
    __channelDensity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'channelDensity'), 'channelDensity', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2channelDensity', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 984, 12), )

    
    channelDensity = property(__channelDensity.value, __channelDensity.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}channelDensityNernst uses Python identifier channelDensityNernst
    __channelDensityNernst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'channelDensityNernst'), 'channelDensityNernst', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2channelDensityNernst', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 985, 12), )

    
    channelDensityNernst = property(__channelDensityNernst.value, __channelDensityNernst.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}spikeThresh uses Python identifier spikeThresh
    __spikeThresh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spikeThresh'), 'spikeThresh', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2spikeThresh', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 987, 12), )

    
    spikeThresh = property(__spikeThresh.value, __spikeThresh.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}specificCapacitance uses Python identifier specificCapacitance
    __specificCapacitance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'specificCapacitance'), 'specificCapacitance', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2specificCapacitance', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 988, 12), )

    
    specificCapacitance = property(__specificCapacitance.value, __specificCapacitance.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}initMembPotential uses Python identifier initMembPotential
    __initMembPotential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'initMembPotential'), 'initMembPotential', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2initMembPotential', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 990, 12), )

    
    initMembPotential = property(__initMembPotential.value, __initMembPotential.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}reversalPotential uses Python identifier reversalPotential
    __reversalPotential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reversalPotential'), 'reversalPotential', '__httpwww_neuroml_orgschemaneuroml2_MembraneProperties_httpwww_neuroml_orgschemaneuroml2reversalPotential', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 992, 12), )

    
    reversalPotential = property(__reversalPotential.value, __reversalPotential.set, None, None)

    _ElementMap.update({
        __channelPopulation.name() : __channelPopulation,
        __channelDensity.name() : __channelDensity,
        __channelDensityNernst.name() : __channelDensityNernst,
        __spikeThresh.name() : __spikeThresh,
        __specificCapacitance.name() : __specificCapacitance,
        __initMembPotential.name() : __initMembPotential,
        __reversalPotential.name() : __reversalPotential
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MembraneProperties', MembraneProperties)


# Complex type {http://www.neuroml.org/schema/neuroml2}VariableParameter with content type ELEMENT_ONLY
class VariableParameter (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}VariableParameter with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VariableParameter')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1103, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}inhomogeneousValue uses Python identifier inhomogeneousValue
    __inhomogeneousValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousValue'), 'inhomogeneousValue', '__httpwww_neuroml_orgschemaneuroml2_VariableParameter_httpwww_neuroml_orgschemaneuroml2inhomogeneousValue', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1106, 12), )

    
    inhomogeneousValue = property(__inhomogeneousValue.value, __inhomogeneousValue.set, None, None)

    
    # Attribute parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parameter'), 'parameter', '__httpwww_neuroml_orgschemaneuroml2_VariableParameter_parameter', pyxb.binding.datatypes.string, required=True)
    __parameter._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1108, 8)
    __parameter._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1108, 8)
    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_VariableParameter_segmentGroup', pyxb.binding.datatypes.string, required=True)
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1109, 8)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1109, 8)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    _ElementMap.update({
        __inhomogeneousValue.name() : __inhomogeneousValue
    })
    _AttributeMap.update({
        __parameter.name() : __parameter,
        __segmentGroup.name() : __segmentGroup
    })
Namespace.addCategoryObject('typeBinding', u'VariableParameter', VariableParameter)


# Complex type {http://www.neuroml.org/schema/neuroml2}InhomogeneousValue with content type EMPTY
class InhomogeneousValue (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}InhomogeneousValue with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InhomogeneousValue')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1113, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute inhomogeneousParam uses Python identifier inhomogeneousParam
    __inhomogeneousParam = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'inhomogeneousParam'), 'inhomogeneousParam', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousValue_inhomogeneousParam', pyxb.binding.datatypes.string, required=True)
    __inhomogeneousParam._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1114, 8)
    __inhomogeneousParam._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1114, 8)
    
    inhomogeneousParam = property(__inhomogeneousParam.value, __inhomogeneousParam.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousValue_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1115, 8)
    __value._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1115, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __inhomogeneousParam.name() : __inhomogeneousParam,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', u'InhomogeneousValue', InhomogeneousValue)


# Complex type {http://www.neuroml.org/schema/neuroml2}IntracellularProperties with content type ELEMENT_ONLY
class IntracellularProperties (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IntracellularProperties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IntracellularProperties')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1175, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}species uses Python identifier species
    __species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_IntracellularProperties_httpwww_neuroml_orgschemaneuroml2species', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1178, 12), )

    
    species = property(__species.value, __species.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}resistivity uses Python identifier resistivity
    __resistivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resistivity'), 'resistivity', '__httpwww_neuroml_orgschemaneuroml2_IntracellularProperties_httpwww_neuroml_orgschemaneuroml2resistivity', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1179, 12), )

    
    resistivity = property(__resistivity.value, __resistivity.set, None, None)

    _ElementMap.update({
        __species.name() : __species,
        __resistivity.name() : __resistivity
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IntracellularProperties', IntracellularProperties)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExtracellularPropertiesLocal with content type ELEMENT_ONLY
class ExtracellularPropertiesLocal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExtracellularPropertiesLocal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExtracellularPropertiesLocal')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1198, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}species uses Python identifier species
    __species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_ExtracellularPropertiesLocal_httpwww_neuroml_orgschemaneuroml2species', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1201, 12), )

    
    species = property(__species.value, __species.set, None, None)

    _ElementMap.update({
        __species.name() : __species
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ExtracellularPropertiesLocal', ExtracellularPropertiesLocal)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpaceStructure with content type EMPTY
class SpaceStructure (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpaceStructure with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpaceStructure')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1403, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xSpacing uses Python identifier xSpacing
    __xSpacing = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'xSpacing'), 'xSpacing', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_xSpacing', pyxb.binding.datatypes.float)
    __xSpacing._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1404, 8)
    __xSpacing._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1404, 8)
    
    xSpacing = property(__xSpacing.value, __xSpacing.set, None, None)

    
    # Attribute ySpacing uses Python identifier ySpacing
    __ySpacing = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ySpacing'), 'ySpacing', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_ySpacing', pyxb.binding.datatypes.float)
    __ySpacing._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1405, 8)
    __ySpacing._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1405, 8)
    
    ySpacing = property(__ySpacing.value, __ySpacing.set, None, None)

    
    # Attribute zSpacing uses Python identifier zSpacing
    __zSpacing = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'zSpacing'), 'zSpacing', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_zSpacing', pyxb.binding.datatypes.float)
    __zSpacing._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1406, 8)
    __zSpacing._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1406, 8)
    
    zSpacing = property(__zSpacing.value, __zSpacing.set, None, None)

    
    # Attribute xStart uses Python identifier xStart
    __xStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'xStart'), 'xStart', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_xStart', pyxb.binding.datatypes.float, unicode_default=u'0')
    __xStart._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1407, 8)
    __xStart._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1407, 8)
    
    xStart = property(__xStart.value, __xStart.set, None, None)

    
    # Attribute yStart uses Python identifier yStart
    __yStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'yStart'), 'yStart', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_yStart', pyxb.binding.datatypes.float, unicode_default=u'0')
    __yStart._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1408, 8)
    __yStart._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1408, 8)
    
    yStart = property(__yStart.value, __yStart.set, None, None)

    
    # Attribute zStart uses Python identifier zStart
    __zStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'zStart'), 'zStart', '__httpwww_neuroml_orgschemaneuroml2_SpaceStructure_zStart', pyxb.binding.datatypes.float, unicode_default=u'0')
    __zStart._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1409, 8)
    __zStart._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1409, 8)
    
    zStart = property(__zStart.value, __zStart.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xSpacing.name() : __xSpacing,
        __ySpacing.name() : __ySpacing,
        __zSpacing.name() : __zSpacing,
        __xStart.name() : __xStart,
        __yStart.name() : __yStart,
        __zStart.name() : __zStart
    })
Namespace.addCategoryObject('typeBinding', u'SpaceStructure', SpaceStructure)


# Complex type {http://www.neuroml.org/schema/neuroml2}UnstructuredLayout with content type EMPTY
class UnstructuredLayout (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}UnstructuredLayout with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UnstructuredLayout')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1488, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_neuroml_orgschemaneuroml2_UnstructuredLayout_number', pyxb.binding.datatypes.nonNegativeInteger)
    __number._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1489, 8)
    __number._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1489, 8)
    
    number = property(__number.value, __number.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number
    })
Namespace.addCategoryObject('typeBinding', u'UnstructuredLayout', UnstructuredLayout)


# Complex type {http://www.neuroml.org/schema/neuroml2}GridLayout with content type EMPTY
class GridLayout (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GridLayout with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GridLayout')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1499, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute xSize uses Python identifier xSize
    __xSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'xSize'), 'xSize', '__httpwww_neuroml_orgschemaneuroml2_GridLayout_xSize', pyxb.binding.datatypes.nonNegativeInteger)
    __xSize._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1500, 8)
    __xSize._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1500, 8)
    
    xSize = property(__xSize.value, __xSize.set, None, None)

    
    # Attribute ySize uses Python identifier ySize
    __ySize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ySize'), 'ySize', '__httpwww_neuroml_orgschemaneuroml2_GridLayout_ySize', pyxb.binding.datatypes.nonNegativeInteger)
    __ySize._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1501, 8)
    __ySize._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1501, 8)
    
    ySize = property(__ySize.value, __ySize.set, None, None)

    
    # Attribute zSize uses Python identifier zSize
    __zSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'zSize'), 'zSize', '__httpwww_neuroml_orgschemaneuroml2_GridLayout_zSize', pyxb.binding.datatypes.nonNegativeInteger)
    __zSize._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1502, 8)
    __zSize._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1502, 8)
    
    zSize = property(__zSize.value, __zSize.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __xSize.name() : __xSize,
        __ySize.name() : __ySize,
        __zSize.name() : __zSize
    })
Namespace.addCategoryObject('typeBinding', u'GridLayout', GridLayout)


# Complex type {http://www.neuroml.org/schema/neuroml2}Instance with content type ELEMENT_ONLY
class Instance (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Instance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Instance')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1506, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'location'), 'location', '__httpwww_neuroml_orgschemaneuroml2_Instance_httpwww_neuroml_orgschemaneuroml2location', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1508, 12), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Instance_id', pyxb.binding.datatypes.nonNegativeInteger)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1510, 8)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1510, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute i uses Python identifier i
    __i = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'i'), 'i', '__httpwww_neuroml_orgschemaneuroml2_Instance_i', pyxb.binding.datatypes.nonNegativeInteger)
    __i._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1511, 8)
    __i._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1511, 8)
    
    i = property(__i.value, __i.set, None, None)

    
    # Attribute j uses Python identifier j
    __j = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'j'), 'j', '__httpwww_neuroml_orgschemaneuroml2_Instance_j', pyxb.binding.datatypes.nonNegativeInteger)
    __j._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1512, 8)
    __j._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1512, 8)
    
    j = property(__j.value, __j.set, None, None)

    
    # Attribute k uses Python identifier k
    __k = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'k'), 'k', '__httpwww_neuroml_orgschemaneuroml2_Instance_k', pyxb.binding.datatypes.nonNegativeInteger)
    __k._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1513, 8)
    __k._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1513, 8)
    
    k = property(__k.value, __k.set, None, None)

    _ElementMap.update({
        __location.name() : __location
    })
    _AttributeMap.update({
        __id.name() : __id,
        __i.name() : __i,
        __j.name() : __j,
        __k.name() : __k
    })
Namespace.addCategoryObject('typeBinding', u'Instance', Instance)


# Complex type {http://www.neuroml.org/schema/neuroml2}Location with content type EMPTY
class Location (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Location with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Location')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1516, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpwww_neuroml_orgschemaneuroml2_Location_x', pyxb.binding.datatypes.float)
    __x._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1517, 8)
    __x._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1517, 8)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpwww_neuroml_orgschemaneuroml2_Location_y', pyxb.binding.datatypes.float)
    __y._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1518, 8)
    __y._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1518, 8)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpwww_neuroml_orgschemaneuroml2_Location_z', pyxb.binding.datatypes.float)
    __z._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1519, 8)
    __z._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1519, 8)
    
    z = property(__z.value, __z.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z
    })
Namespace.addCategoryObject('typeBinding', u'Location', Location)


# Complex type {http://www.neuroml.org/schema/neuroml2}SynapticConnection with content type EMPTY
class SynapticConnection (pyxb.binding.basis.complexTypeDefinition):
    """Single explicit connection. Introduced to test connections in LEMS. Will probably be removed in favour of
            connections wrapped in projection element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SynapticConnection')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1538, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpwww_neuroml_orgschemaneuroml2_SynapticConnection_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1543, 8)
    __from._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1543, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpwww_neuroml_orgschemaneuroml2_SynapticConnection_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1544, 8)
    __to._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1544, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute synapse uses Python identifier synapse
    __synapse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse'), 'synapse', '__httpwww_neuroml_orgschemaneuroml2_SynapticConnection_synapse', pyxb.binding.datatypes.string)
    __synapse._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1545, 8)
    __synapse._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1545, 8)
    
    synapse = property(__synapse.value, __synapse.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to,
        __synapse.name() : __synapse
    })
Namespace.addCategoryObject('typeBinding', u'SynapticConnection', SynapticConnection)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExplicitInput with content type EMPTY
class ExplicitInput (pyxb.binding.basis.complexTypeDefinition):
    """Single explicit input. Introduced to test inputs in LEMS. Will probably be removed in favour of
            inputs wrapped in inputList element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExplicitInput')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1579, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'target'), 'target', '__httpwww_neuroml_orgschemaneuroml2_ExplicitInput_target', pyxb.binding.datatypes.string)
    __target._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1584, 8)
    __target._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1584, 8)
    
    target = property(__target.value, __target.set, None, None)

    
    # Attribute input uses Python identifier input
    __input = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'input'), 'input', '__httpwww_neuroml_orgschemaneuroml2_ExplicitInput_input', pyxb.binding.datatypes.string)
    __input._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1585, 8)
    __input._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1585, 8)
    
    input = property(__input.value, __input.set, None, None)

    
    # Attribute destination uses Python identifier destination
    __destination = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'destination'), 'destination', '__httpwww_neuroml_orgschemaneuroml2_ExplicitInput_destination', pyxb.binding.datatypes.string)
    __destination._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1586, 8)
    __destination._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1586, 8)
    
    destination = property(__destination.value, __destination.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __target.name() : __target,
        __input.name() : __input,
        __destination.name() : __destination
    })
Namespace.addCategoryObject('typeBinding', u'ExplicitInput', ExplicitInput)


# Complex type {http://www.neuroml.org/schema/neuroml2}Q10Settings with content type EMPTY
class Q10Settings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Q10Settings with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Q10Settings')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 537, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_Q10Settings_type', NmlId, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 538, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 538, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute fixedQ10 uses Python identifier fixedQ10
    __fixedQ10 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixedQ10'), 'fixedQ10', '__httpwww_neuroml_orgschemaneuroml2_Q10Settings_fixedQ10', Nml2Quantity_none)
    __fixedQ10._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 539, 8)
    __fixedQ10._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 539, 8)
    
    fixedQ10 = property(__fixedQ10.value, __fixedQ10.set, None, None)

    
    # Attribute q10Factor uses Python identifier q10Factor
    __q10Factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'q10Factor'), 'q10Factor', '__httpwww_neuroml_orgschemaneuroml2_Q10Settings_q10Factor', Nml2Quantity_none)
    __q10Factor._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 540, 8)
    __q10Factor._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 540, 8)
    
    q10Factor = property(__q10Factor.value, __q10Factor.set, None, None)

    
    # Attribute experimentalTemp uses Python identifier experimentalTemp
    __experimentalTemp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'experimentalTemp'), 'experimentalTemp', '__httpwww_neuroml_orgschemaneuroml2_Q10Settings_experimentalTemp', Nml2Quantity_temperature)
    __experimentalTemp._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 541, 8)
    __experimentalTemp._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 541, 8)
    
    experimentalTemp = property(__experimentalTemp.value, __experimentalTemp.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __fixedQ10.name() : __fixedQ10,
        __q10Factor.name() : __q10Factor,
        __experimentalTemp.name() : __experimentalTemp
    })
Namespace.addCategoryObject('typeBinding', u'Q10Settings', Q10Settings)


# Complex type {http://www.neuroml.org/schema/neuroml2}HHRate with content type EMPTY
class HHRate (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}HHRate with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HHRate')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 544, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_HHRate_type', NmlId, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 545, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 545, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpwww_neuroml_orgschemaneuroml2_HHRate_rate', Nml2Quantity_pertime)
    __rate._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 546, 8)
    __rate._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 546, 8)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpwww_neuroml_orgschemaneuroml2_HHRate_midpoint', Nml2Quantity_voltage)
    __midpoint._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 547, 8)
    __midpoint._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 547, 8)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpwww_neuroml_orgschemaneuroml2_HHRate_scale', Nml2Quantity_voltage)
    __scale._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 548, 8)
    __scale._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 548, 8)
    
    scale = property(__scale.value, __scale.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __rate.name() : __rate,
        __midpoint.name() : __midpoint,
        __scale.name() : __scale
    })
Namespace.addCategoryObject('typeBinding', u'HHRate', HHRate)


# Complex type {http://www.neuroml.org/schema/neuroml2}HHVariable with content type EMPTY
class HHVariable (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}HHVariable with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HHVariable')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 551, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_HHVariable_type', NmlId, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 552, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 552, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpwww_neuroml_orgschemaneuroml2_HHVariable_rate', pyxb.binding.datatypes.float)
    __rate._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 553, 8)
    __rate._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 553, 8)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpwww_neuroml_orgschemaneuroml2_HHVariable_midpoint', Nml2Quantity_voltage)
    __midpoint._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 554, 8)
    __midpoint._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 554, 8)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpwww_neuroml_orgschemaneuroml2_HHVariable_scale', Nml2Quantity_voltage)
    __scale._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 555, 8)
    __scale._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 555, 8)
    
    scale = property(__scale.value, __scale.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __rate.name() : __rate,
        __midpoint.name() : __midpoint,
        __scale.name() : __scale
    })
Namespace.addCategoryObject('typeBinding', u'HHVariable', HHVariable)


# Complex type {http://www.neuroml.org/schema/neuroml2}HHTime with content type EMPTY
class HHTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}HHTime with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HHTime')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 558, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_HHTime_type', NmlId, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 559, 8)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 559, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpwww_neuroml_orgschemaneuroml2_HHTime_rate', Nml2Quantity_time)
    __rate._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 560, 8)
    __rate._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 560, 8)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpwww_neuroml_orgschemaneuroml2_HHTime_midpoint', Nml2Quantity_voltage)
    __midpoint._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 561, 8)
    __midpoint._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 561, 8)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpwww_neuroml_orgschemaneuroml2_HHTime_scale', Nml2Quantity_voltage)
    __scale._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 562, 8)
    __scale._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 562, 8)
    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau'), 'tau', '__httpwww_neuroml_orgschemaneuroml2_HHTime_tau', Nml2Quantity_time)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 563, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 563, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __rate.name() : __rate,
        __midpoint.name() : __midpoint,
        __scale.name() : __scale,
        __tau.name() : __tau
    })
Namespace.addCategoryObject('typeBinding', u'HHTime', HHTime)


# Complex type {http://www.neuroml.org/schema/neuroml2}BlockMechanism with content type EMPTY
class BlockMechanism (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BlockMechanism with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BlockMechanism')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 668, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_BlockMechanism_type', BlockTypes, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 669, 6)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 669, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute species uses Python identifier species
    __species = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_BlockMechanism_species', NmlId, required=True)
    __species._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 671, 6)
    __species._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 671, 6)
    
    species = property(__species.value, __species.set, None, None)

    
    # Attribute blockConcentration uses Python identifier blockConcentration
    __blockConcentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'blockConcentration'), 'blockConcentration', '__httpwww_neuroml_orgschemaneuroml2_BlockMechanism_blockConcentration', Nml2Quantity_concentration, required=True)
    __blockConcentration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 672, 6)
    __blockConcentration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 672, 6)
    
    blockConcentration = property(__blockConcentration.value, __blockConcentration.set, None, None)

    
    # Attribute scalingConc uses Python identifier scalingConc
    __scalingConc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scalingConc'), 'scalingConc', '__httpwww_neuroml_orgschemaneuroml2_BlockMechanism_scalingConc', Nml2Quantity_concentration, required=True)
    __scalingConc._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 674, 6)
    __scalingConc._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 674, 6)
    
    scalingConc = property(__scalingConc.value, __scalingConc.set, None, None)

    
    # Attribute scalingVolt uses Python identifier scalingVolt
    __scalingVolt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scalingVolt'), 'scalingVolt', '__httpwww_neuroml_orgschemaneuroml2_BlockMechanism_scalingVolt', Nml2Quantity_voltage, required=True)
    __scalingVolt._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 676, 6)
    __scalingVolt._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 676, 6)
    
    scalingVolt = property(__scalingVolt.value, __scalingVolt.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __species.name() : __species,
        __blockConcentration.name() : __blockConcentration,
        __scalingConc.name() : __scalingConc,
        __scalingVolt.name() : __scalingVolt
    })
Namespace.addCategoryObject('typeBinding', u'BlockMechanism', BlockMechanism)


# Complex type {http://www.neuroml.org/schema/neuroml2}PlasticityMechanism with content type EMPTY
class PlasticityMechanism (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}PlasticityMechanism with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PlasticityMechanism')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 687, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_PlasticityMechanism_type', PlasticityTypes, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 688, 6)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 688, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute initReleaseProb uses Python identifier initReleaseProb
    __initReleaseProb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'initReleaseProb'), 'initReleaseProb', '__httpwww_neuroml_orgschemaneuroml2_PlasticityMechanism_initReleaseProb', ZeroToOne, required=True)
    __initReleaseProb._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 689, 6)
    __initReleaseProb._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 689, 6)
    
    initReleaseProb = property(__initReleaseProb.value, __initReleaseProb.set, None, None)

    
    # Attribute tauRec uses Python identifier tauRec
    __tauRec = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauRec'), 'tauRec', '__httpwww_neuroml_orgschemaneuroml2_PlasticityMechanism_tauRec', Nml2Quantity_time, required=True)
    __tauRec._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 691, 6)
    __tauRec._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 691, 6)
    
    tauRec = property(__tauRec.value, __tauRec.set, None, None)

    
    # Attribute tauFac uses Python identifier tauFac
    __tauFac = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauFac'), 'tauFac', '__httpwww_neuroml_orgschemaneuroml2_PlasticityMechanism_tauFac', Nml2Quantity_time)
    __tauFac._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 693, 6)
    __tauFac._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 693, 6)
    
    tauFac = property(__tauFac.value, __tauFac.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __initReleaseProb.name() : __initReleaseProb,
        __tauRec.name() : __tauRec,
        __tauFac.name() : __tauFac
    })
Namespace.addCategoryObject('typeBinding', u'PlasticityMechanism', PlasticityMechanism)


# Complex type {http://www.neuroml.org/schema/neuroml2}SegmentParent with content type EMPTY
class SegmentParent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SegmentParent with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SegmentParent')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 857, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_SegmentParent_segment', SegmentId, required=True)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 858, 8)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 858, 8)
    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Attribute fractionAlong uses Python identifier fractionAlong
    __fractionAlong = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fractionAlong'), 'fractionAlong', '__httpwww_neuroml_orgschemaneuroml2_SegmentParent_fractionAlong', ZeroToOne, unicode_default=u'1')
    __fractionAlong._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 859, 8)
    __fractionAlong._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 859, 8)
    
    fractionAlong = property(__fractionAlong.value, __fractionAlong.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __segment.name() : __segment,
        __fractionAlong.name() : __fractionAlong
    })
Namespace.addCategoryObject('typeBinding', u'SegmentParent', SegmentParent)


# Complex type {http://www.neuroml.org/schema/neuroml2}Member with content type EMPTY
class Member (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Member with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Member')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 926, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_Member_segment', SegmentId, required=True)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 927, 8)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 927, 8)
    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __segment.name() : __segment
    })
Namespace.addCategoryObject('typeBinding', u'Member', Member)


# Complex type {http://www.neuroml.org/schema/neuroml2}Include with content type EMPTY
class Include (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Include with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Include')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 930, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_Include_segmentGroup', NmlId, required=True)
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 931, 8)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 931, 8)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __segmentGroup.name() : __segmentGroup
    })
Namespace.addCategoryObject('typeBinding', u'Include', Include)


# Complex type {http://www.neuroml.org/schema/neuroml2}SegmentEndPoint with content type EMPTY
class SegmentEndPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SegmentEndPoint with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SegmentEndPoint')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 948, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_SegmentEndPoint_segment', SegmentId, required=True)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 949, 8)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 949, 8)
    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __segment.name() : __segment
    })
Namespace.addCategoryObject('typeBinding', u'SegmentEndPoint', SegmentEndPoint)


# Complex type {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup with content type EMPTY
class ValueAcrossSegOrSegGroup (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueAcrossSegOrSegGroup')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1092, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpwww_neuroml_orgschemaneuroml2_ValueAcrossSegOrSegGroup_value', Nml2Quantity)
    __value._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1094, 8)
    __value._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1094, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_ValueAcrossSegOrSegGroup_segmentGroup', NmlId, unicode_default=u'all')
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1097, 8)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1097, 8)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_ValueAcrossSegOrSegGroup_segment', NmlId)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1098, 8)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1098, 8)
    
    segment = property(__segment.value, __segment.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __segmentGroup.name() : __segmentGroup,
        __segment.name() : __segment
    })
Namespace.addCategoryObject('typeBinding', u'ValueAcrossSegOrSegGroup', ValueAcrossSegOrSegGroup)


# Complex type {http://www.neuroml.org/schema/neuroml2}Layout with content type ELEMENT_ONLY
class Layout (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Layout with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Layout')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1474, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.neuroml.org/schema/neuroml2}random uses Python identifier random
    __random = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'random'), 'random', '__httpwww_neuroml_orgschemaneuroml2_Layout_httpwww_neuroml_orgschemaneuroml2random', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1477, 12), )

    
    random = property(__random.value, __random.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}grid uses Python identifier grid
    __grid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'grid'), 'grid', '__httpwww_neuroml_orgschemaneuroml2_Layout_httpwww_neuroml_orgschemaneuroml2grid', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1478, 12), )

    
    grid = property(__grid.value, __grid.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}unstructured uses Python identifier unstructured
    __unstructured = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'unstructured'), 'unstructured', '__httpwww_neuroml_orgschemaneuroml2_Layout_httpwww_neuroml_orgschemaneuroml2unstructured', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1479, 12), )

    
    unstructured = property(__unstructured.value, __unstructured.set, None, None)

    
    # Attribute space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'space'), 'space', '__httpwww_neuroml_orgschemaneuroml2_Layout_space', NmlId)
    __space._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1482, 8)
    __space._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1482, 8)
    
    space = property(__space.value, __space.set, None, None)

    _ElementMap.update({
        __random.name() : __random,
        __grid.name() : __grid,
        __unstructured.name() : __unstructured
    })
    _AttributeMap.update({
        __space.name() : __space
    })
Namespace.addCategoryObject('typeBinding', u'Layout', Layout)


# Complex type {http://www.neuroml.org/schema/neuroml2}RandomLayout with content type EMPTY
class RandomLayout (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.neuroml.org/schema/neuroml2}RandomLayout with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RandomLayout')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1493, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_neuroml_orgschemaneuroml2_RandomLayout_number', pyxb.binding.datatypes.nonNegativeInteger)
    __number._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1494, 8)
    __number._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1494, 8)
    
    number = property(__number.value, __number.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'region'), 'region', '__httpwww_neuroml_orgschemaneuroml2_RandomLayout_region', NmlId)
    __region._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1495, 8)
    __region._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1495, 8)
    
    region = property(__region.value, __region.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __number.name() : __number,
        __region.name() : __region
    })
Namespace.addCategoryObject('typeBinding', u'RandomLayout', RandomLayout)


# Complex type {http://www.neuroml.org/schema/neuroml2}Connection with content type EMPTY
class Connection (pyxb.binding.basis.complexTypeDefinition):
    """Subject to change as it gets tested with LEMS!!"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Connection')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1564, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Connection_id', pyxb.binding.datatypes.nonNegativeInteger)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1568, 8)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1568, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute preCellId uses Python identifier preCellId
    __preCellId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'preCellId'), 'preCellId', '__httpwww_neuroml_orgschemaneuroml2_Connection_preCellId', pyxb.binding.datatypes.string)
    __preCellId._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1569, 8)
    __preCellId._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1569, 8)
    
    preCellId = property(__preCellId.value, __preCellId.set, None, None)

    
    # Attribute preSegmentId uses Python identifier preSegmentId
    __preSegmentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'preSegmentId'), 'preSegmentId', '__httpwww_neuroml_orgschemaneuroml2_Connection_preSegmentId', SegmentId)
    __preSegmentId._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1570, 8)
    __preSegmentId._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1570, 8)
    
    preSegmentId = property(__preSegmentId.value, __preSegmentId.set, None, None)

    
    # Attribute preFractionAlong uses Python identifier preFractionAlong
    __preFractionAlong = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'preFractionAlong'), 'preFractionAlong', '__httpwww_neuroml_orgschemaneuroml2_Connection_preFractionAlong', ZeroToOne)
    __preFractionAlong._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1571, 8)
    __preFractionAlong._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1571, 8)
    
    preFractionAlong = property(__preFractionAlong.value, __preFractionAlong.set, None, None)

    
    # Attribute postCellId uses Python identifier postCellId
    __postCellId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'postCellId'), 'postCellId', '__httpwww_neuroml_orgschemaneuroml2_Connection_postCellId', pyxb.binding.datatypes.string)
    __postCellId._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1572, 8)
    __postCellId._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1572, 8)
    
    postCellId = property(__postCellId.value, __postCellId.set, None, None)

    
    # Attribute postSegmentId uses Python identifier postSegmentId
    __postSegmentId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'postSegmentId'), 'postSegmentId', '__httpwww_neuroml_orgschemaneuroml2_Connection_postSegmentId', SegmentId)
    __postSegmentId._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1573, 8)
    __postSegmentId._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1573, 8)
    
    postSegmentId = property(__postSegmentId.value, __postSegmentId.set, None, None)

    
    # Attribute postFractionAlong uses Python identifier postFractionAlong
    __postFractionAlong = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'postFractionAlong'), 'postFractionAlong', '__httpwww_neuroml_orgschemaneuroml2_Connection_postFractionAlong', ZeroToOne)
    __postFractionAlong._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1574, 8)
    __postFractionAlong._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1574, 8)
    
    postFractionAlong = property(__postFractionAlong.value, __postFractionAlong.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __preCellId.name() : __preCellId,
        __preSegmentId.name() : __preSegmentId,
        __preFractionAlong.name() : __preFractionAlong,
        __postCellId.name() : __postCellId,
        __postSegmentId.name() : __postSegmentId,
        __postFractionAlong.name() : __postFractionAlong
    })
Namespace.addCategoryObject('typeBinding', u'Connection', Connection)


# Complex type {http://www.neuroml.org/schema/neuroml2}Input with content type EMPTY
class Input (pyxb.binding.basis.complexTypeDefinition):
    """Subject to change as it gets tested with LEMS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Input')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1605, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Input_id', pyxb.binding.datatypes.nonNegativeInteger)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1609, 8)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1609, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'target'), 'target', '__httpwww_neuroml_orgschemaneuroml2_Input_target', pyxb.binding.datatypes.string)
    __target._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1610, 8)
    __target._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1610, 8)
    
    target = property(__target.value, __target.set, None, None)

    
    # Attribute destination uses Python identifier destination
    __destination = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'destination'), 'destination', '__httpwww_neuroml_orgschemaneuroml2_Input_destination', NmlId)
    __destination._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1611, 8)
    __destination._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1611, 8)
    
    destination = property(__destination.value, __destination.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __target.name() : __target,
        __destination.name() : __destination
    })
Namespace.addCategoryObject('typeBinding', u'Input', Input)


# Complex type {http://www.neuroml.org/schema/neuroml2}BaseWithoutId with content type EMPTY
class BaseWithoutId (pyxb.binding.basis.complexTypeDefinition):
    """Base element without ID specified *yet*, e.g. for an element with a particular requirement on its id which does not comply with NmlId (e.g. Segment needs nonNegativeInteger)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseWithoutId')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1814, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute neuroLexId uses Python identifier neuroLexId
    __neuroLexId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'neuroLexId'), 'neuroLexId', '__httpwww_neuroml_orgschemaneuroml2_BaseWithoutId_neuroLexId', NeuroLexId)
    __neuroLexId._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1820, 8)
    __neuroLexId._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1820, 8)
    
    neuroLexId = property(__neuroLexId.value, __neuroLexId.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __neuroLexId.name() : __neuroLexId
    })
Namespace.addCategoryObject('typeBinding', u'BaseWithoutId', BaseWithoutId)


# Complex type {http://www.neuroml.org/schema/neuroml2}Segment with content type ELEMENT_ONLY
class Segment (BaseWithoutId):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Segment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Segment')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 839, 4)
    _ElementMap = BaseWithoutId._ElementMap.copy()
    _AttributeMap = BaseWithoutId._AttributeMap.copy()
    # Base type is BaseWithoutId
    
    # Element {http://www.neuroml.org/schema/neuroml2}parent uses Python identifier parent
    __parent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'parent'), 'parent', '__httpwww_neuroml_orgschemaneuroml2_Segment_httpwww_neuroml_orgschemaneuroml2parent', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 844, 20), )

    
    parent = property(__parent.value, __parent.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}proximal uses Python identifier proximal
    __proximal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'proximal'), 'proximal', '__httpwww_neuroml_orgschemaneuroml2_Segment_httpwww_neuroml_orgschemaneuroml2proximal', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 845, 20), )

    
    proximal = property(__proximal.value, __proximal.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}distal uses Python identifier distal
    __distal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'distal'), 'distal', '__httpwww_neuroml_orgschemaneuroml2_Segment_httpwww_neuroml_orgschemaneuroml2distal', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 846, 20), )

    
    distal = property(__distal.value, __distal.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Segment_id', SegmentId, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 849, 16)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 849, 16)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_neuroml_orgschemaneuroml2_Segment_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 850, 16)
    __name._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 850, 16)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    _ElementMap.update({
        __parent.name() : __parent,
        __proximal.name() : __proximal,
        __distal.name() : __distal
    })
    _AttributeMap.update({
        __id.name() : __id,
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'Segment', Segment)


# Complex type {http://www.neuroml.org/schema/neuroml2}ReversalPotential with content type EMPTY
class ReversalPotential (ValueAcrossSegOrSegGroup):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ReversalPotential with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReversalPotential')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1119, 4)
    _ElementMap = ValueAcrossSegOrSegGroup._ElementMap.copy()
    _AttributeMap = ValueAcrossSegOrSegGroup._AttributeMap.copy()
    # Base type is ValueAcrossSegOrSegGroup
    
    # Attribute value_ inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute segmentGroup inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute segment inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute species uses Python identifier species
    __species = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_ReversalPotential_species', NmlId)
    __species._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1123, 16)
    __species._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1123, 16)
    
    species = property(__species.value, __species.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __species.name() : __species
    })
Namespace.addCategoryObject('typeBinding', u'ReversalPotential', ReversalPotential)


# Complex type {http://www.neuroml.org/schema/neuroml2}Species with content type EMPTY
class Species (ValueAcrossSegOrSegGroup):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Species with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Species')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1130, 4)
    _ElementMap = ValueAcrossSegOrSegGroup._ElementMap.copy()
    _AttributeMap = ValueAcrossSegOrSegGroup._AttributeMap.copy()
    # Base type is ValueAcrossSegOrSegGroup
    
    # Attribute value_ inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute segmentGroup inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute segment inherited from {http://www.neuroml.org/schema/neuroml2}ValueAcrossSegOrSegGroup
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Species_id', NmlId, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1135, 16)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1135, 16)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute concentrationModel uses Python identifier concentrationModel
    __concentrationModel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'concentrationModel'), 'concentrationModel', '__httpwww_neuroml_orgschemaneuroml2_Species_concentrationModel', NmlId, required=True)
    __concentrationModel._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1137, 16)
    __concentrationModel._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1137, 16)
    
    concentrationModel = property(__concentrationModel.value, __concentrationModel.set, None, None)

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpwww_neuroml_orgschemaneuroml2_Species_ion', NmlId)
    __ion._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1139, 16)
    __ion._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1139, 16)
    
    ion = property(__ion.value, __ion.set, None, u'Specifying the ion here again is redundant, the ion name should be the same as id. Kept for now\n                        until LEMS implementation can select by id. TODO: remove.\n                        ')

    
    # Attribute initialConcentration uses Python identifier initialConcentration
    __initialConcentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'initialConcentration'), 'initialConcentration', '__httpwww_neuroml_orgschemaneuroml2_Species_initialConcentration', Nml2Quantity_concentration, required=True)
    __initialConcentration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1147, 16)
    __initialConcentration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1147, 16)
    
    initialConcentration = property(__initialConcentration.value, __initialConcentration.set, None, None)

    
    # Attribute initialExtConcentration uses Python identifier initialExtConcentration
    __initialExtConcentration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'initialExtConcentration'), 'initialExtConcentration', '__httpwww_neuroml_orgschemaneuroml2_Species_initialExtConcentration', Nml2Quantity_concentration, required=True)
    __initialExtConcentration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1148, 16)
    __initialExtConcentration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1148, 16)
    
    initialExtConcentration = property(__initialExtConcentration.value, __initialExtConcentration.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __concentrationModel.name() : __concentrationModel,
        __ion.name() : __ion,
        __initialConcentration.name() : __initialConcentration,
        __initialExtConcentration.name() : __initialExtConcentration
    })
Namespace.addCategoryObject('typeBinding', u'Species', Species)


# Complex type {http://www.neuroml.org/schema/neuroml2}Base with content type EMPTY
class Base (BaseWithoutId):
    """Anything which can have a unique (within its parent) id of the form NmlId (spaceless combination of letters, numbers and underscore)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Base')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1824, 4)
    _ElementMap = BaseWithoutId._ElementMap.copy()
    _AttributeMap = BaseWithoutId._AttributeMap.copy()
    # Base type is BaseWithoutId
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpwww_neuroml_orgschemaneuroml2_Base_id', NmlId, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1833, 16)
    __id._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1833, 16)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'Base', Base)


# Complex type {http://www.neuroml.org/schema/neuroml2}GateHHUndetermined with content type ELEMENT_ONLY
class GateHHUndetermined (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GateHHUndetermined with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GateHHUndetermined')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 456, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 460, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}q10Settings uses Python identifier q10Settings
    __q10Settings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), 'q10Settings', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2q10Settings', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 461, 20), )

    
    q10Settings = property(__q10Settings.value, __q10Settings.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}forwardRate uses Python identifier forwardRate
    __forwardRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), 'forwardRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2forwardRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 462, 20), )

    
    forwardRate = property(__forwardRate.value, __forwardRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}reverseRate uses Python identifier reverseRate
    __reverseRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), 'reverseRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2reverseRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 463, 20), )

    
    reverseRate = property(__reverseRate.value, __reverseRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}timeCourse uses Python identifier timeCourse
    __timeCourse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), 'timeCourse', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2timeCourse', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 464, 20), )

    
    timeCourse = property(__timeCourse.value, __timeCourse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}steadyState uses Python identifier steadyState
    __steadyState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), 'steadyState', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_httpwww_neuroml_orgschemaneuroml2steadyState', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 465, 20), )

    
    steadyState = property(__steadyState.value, __steadyState.set, None, None)

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_instances', pyxb.binding.datatypes.integer, unicode_default=u'1')
    __instances._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 467, 16)
    __instances._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 467, 16)
    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_GateHHUndetermined_type', gateTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 468, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 468, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __notes.name() : __notes,
        __q10Settings.name() : __q10Settings,
        __forwardRate.name() : __forwardRate,
        __reverseRate.name() : __reverseRate,
        __timeCourse.name() : __timeCourse,
        __steadyState.name() : __steadyState
    })
    _AttributeMap.update({
        __instances.name() : __instances,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'GateHHUndetermined', GateHHUndetermined)


# Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRates with content type ELEMENT_ONLY
class GateHHRates (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRates with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GateHHRates')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 473, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 477, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}q10Settings uses Python identifier q10Settings
    __q10Settings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), 'q10Settings', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_httpwww_neuroml_orgschemaneuroml2q10Settings', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 478, 20), )

    
    q10Settings = property(__q10Settings.value, __q10Settings.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}forwardRate uses Python identifier forwardRate
    __forwardRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), 'forwardRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_httpwww_neuroml_orgschemaneuroml2forwardRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 479, 20), )

    
    forwardRate = property(__forwardRate.value, __forwardRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}reverseRate uses Python identifier reverseRate
    __reverseRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), 'reverseRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_httpwww_neuroml_orgschemaneuroml2reverseRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 480, 20), )

    
    reverseRate = property(__reverseRate.value, __reverseRate.set, None, None)

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_instances', pyxb.binding.datatypes.integer, unicode_default=u'1')
    __instances._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 482, 16)
    __instances._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 482, 16)
    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_GateHHRates_type', gateTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 483, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 483, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __notes.name() : __notes,
        __q10Settings.name() : __q10Settings,
        __forwardRate.name() : __forwardRate,
        __reverseRate.name() : __reverseRate
    })
    _AttributeMap.update({
        __instances.name() : __instances,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'GateHHRates', GateHHRates)


# Complex type {http://www.neuroml.org/schema/neuroml2}GateHHTauInf with content type ELEMENT_ONLY
class GateHHTauInf (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GateHHTauInf with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GateHHTauInf')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 489, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 493, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}q10Settings uses Python identifier q10Settings
    __q10Settings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), 'q10Settings', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_httpwww_neuroml_orgschemaneuroml2q10Settings', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 494, 20), )

    
    q10Settings = property(__q10Settings.value, __q10Settings.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}timeCourse uses Python identifier timeCourse
    __timeCourse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), 'timeCourse', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_httpwww_neuroml_orgschemaneuroml2timeCourse', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 495, 20), )

    
    timeCourse = property(__timeCourse.value, __timeCourse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}steadyState uses Python identifier steadyState
    __steadyState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), 'steadyState', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_httpwww_neuroml_orgschemaneuroml2steadyState', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 496, 20), )

    
    steadyState = property(__steadyState.value, __steadyState.set, None, None)

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_instances', pyxb.binding.datatypes.integer, unicode_default=u'1')
    __instances._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 498, 16)
    __instances._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 498, 16)
    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_GateHHTauInf_type', gateTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 499, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 499, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __notes.name() : __notes,
        __q10Settings.name() : __q10Settings,
        __timeCourse.name() : __timeCourse,
        __steadyState.name() : __steadyState
    })
    _AttributeMap.update({
        __instances.name() : __instances,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'GateHHTauInf', GateHHTauInf)


# Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRatesTau with content type ELEMENT_ONLY
class GateHHRatesTau (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRatesTau with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GateHHRatesTau')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 504, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 508, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}q10Settings uses Python identifier q10Settings
    __q10Settings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), 'q10Settings', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_httpwww_neuroml_orgschemaneuroml2q10Settings', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 509, 20), )

    
    q10Settings = property(__q10Settings.value, __q10Settings.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}forwardRate uses Python identifier forwardRate
    __forwardRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), 'forwardRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_httpwww_neuroml_orgschemaneuroml2forwardRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 510, 20), )

    
    forwardRate = property(__forwardRate.value, __forwardRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}reverseRate uses Python identifier reverseRate
    __reverseRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), 'reverseRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_httpwww_neuroml_orgschemaneuroml2reverseRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 511, 20), )

    
    reverseRate = property(__reverseRate.value, __reverseRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}timeCourse uses Python identifier timeCourse
    __timeCourse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), 'timeCourse', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_httpwww_neuroml_orgschemaneuroml2timeCourse', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 512, 20), )

    
    timeCourse = property(__timeCourse.value, __timeCourse.set, None, None)

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_instances', pyxb.binding.datatypes.integer, unicode_default=u'1')
    __instances._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 514, 16)
    __instances._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 514, 16)
    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesTau_type', gateTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 515, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 515, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __notes.name() : __notes,
        __q10Settings.name() : __q10Settings,
        __forwardRate.name() : __forwardRate,
        __reverseRate.name() : __reverseRate,
        __timeCourse.name() : __timeCourse
    })
    _AttributeMap.update({
        __instances.name() : __instances,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'GateHHRatesTau', GateHHRatesTau)


# Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRatesInf with content type ELEMENT_ONLY
class GateHHRatesInf (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}GateHHRatesInf with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GateHHRatesInf')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 520, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 524, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}q10Settings uses Python identifier q10Settings
    __q10Settings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), 'q10Settings', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_httpwww_neuroml_orgschemaneuroml2q10Settings', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 525, 20), )

    
    q10Settings = property(__q10Settings.value, __q10Settings.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}forwardRate uses Python identifier forwardRate
    __forwardRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), 'forwardRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_httpwww_neuroml_orgschemaneuroml2forwardRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 526, 20), )

    
    forwardRate = property(__forwardRate.value, __forwardRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}reverseRate uses Python identifier reverseRate
    __reverseRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), 'reverseRate', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_httpwww_neuroml_orgschemaneuroml2reverseRate', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 527, 20), )

    
    reverseRate = property(__reverseRate.value, __reverseRate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}steadyState uses Python identifier steadyState
    __steadyState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), 'steadyState', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_httpwww_neuroml_orgschemaneuroml2steadyState', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 528, 20), )

    
    steadyState = property(__steadyState.value, __steadyState.set, None, None)

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_instances', pyxb.binding.datatypes.integer, unicode_default=u'1')
    __instances._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 530, 16)
    __instances._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 530, 16)
    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_GateHHRatesInf_type', gateTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 531, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 531, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __notes.name() : __notes,
        __q10Settings.name() : __q10Settings,
        __forwardRate.name() : __forwardRate,
        __reverseRate.name() : __reverseRate,
        __steadyState.name() : __steadyState
    })
    _AttributeMap.update({
        __instances.name() : __instances,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'GateHHRatesInf', GateHHRatesInf)


# Complex type {http://www.neuroml.org/schema/neuroml2}SegmentGroup with content type ELEMENT_ONLY
class SegmentGroup (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SegmentGroup with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SegmentGroup')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 874, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}member uses Python identifier member
    __member = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'member'), 'member', '__httpwww_neuroml_orgschemaneuroml2_SegmentGroup_httpwww_neuroml_orgschemaneuroml2member', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 882, 20), )

    
    member = property(__member.value, __member.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include'), 'include', '__httpwww_neuroml_orgschemaneuroml2_SegmentGroup_httpwww_neuroml_orgschemaneuroml2include', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 883, 20), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'path'), 'path', '__httpwww_neuroml_orgschemaneuroml2_SegmentGroup_httpwww_neuroml_orgschemaneuroml2path', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 884, 20), )

    
    path = property(__path.value, __path.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}subTree uses Python identifier subTree
    __subTree = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'subTree'), 'subTree', '__httpwww_neuroml_orgschemaneuroml2_SegmentGroup_httpwww_neuroml_orgschemaneuroml2subTree', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 885, 20), )

    
    subTree = property(__subTree.value, __subTree.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}inhomogeneousParam uses Python identifier inhomogeneousParam
    __inhomogeneousParam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousParam'), 'inhomogeneousParam', '__httpwww_neuroml_orgschemaneuroml2_SegmentGroup_httpwww_neuroml_orgschemaneuroml2inhomogeneousParam', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 886, 20), )

    
    inhomogeneousParam = property(__inhomogeneousParam.value, __inhomogeneousParam.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __member.name() : __member,
        __include.name() : __include,
        __path.name() : __path,
        __subTree.name() : __subTree,
        __inhomogeneousParam.name() : __inhomogeneousParam
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SegmentGroup', SegmentGroup)


# Complex type {http://www.neuroml.org/schema/neuroml2}InhomogeneousParam with content type ELEMENT_ONLY
class InhomogeneousParam (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}InhomogeneousParam with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InhomogeneousParam')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 894, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}proximal uses Python identifier proximal
    __proximal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'proximal'), 'proximal', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousParam_httpwww_neuroml_orgschemaneuroml2proximal', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 898, 20), )

    
    proximal = property(__proximal.value, __proximal.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}distal uses Python identifier distal
    __distal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'distal'), 'distal', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousParam_httpwww_neuroml_orgschemaneuroml2distal', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 899, 20), )

    
    distal = property(__distal.value, __distal.set, None, None)

    
    # Attribute variable uses Python identifier variable
    __variable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'variable'), 'variable', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousParam_variable', pyxb.binding.datatypes.string, required=True)
    __variable._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 901, 16)
    __variable._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 901, 16)
    
    variable = property(__variable.value, __variable.set, None, None)

    
    # Attribute metric uses Python identifier metric
    __metric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metric'), 'metric', '__httpwww_neuroml_orgschemaneuroml2_InhomogeneousParam_metric', Metric, required=True)
    __metric._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 902, 16)
    __metric._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 902, 16)
    
    metric = property(__metric.value, __metric.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __proximal.name() : __proximal,
        __distal.name() : __distal
    })
    _AttributeMap.update({
        __variable.name() : __variable,
        __metric.name() : __metric
    })
Namespace.addCategoryObject('typeBinding', u'InhomogeneousParam', InhomogeneousParam)


# Complex type {http://www.neuroml.org/schema/neuroml2}ChannelPopulation with content type ELEMENT_ONLY
class ChannelPopulation (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ChannelPopulation with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChannelPopulation')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 997, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'variableParameter'), 'variableParameter', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_httpwww_neuroml_orgschemaneuroml2variableParameter', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1003, 20), )

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, None)

    
    # Attribute ionChannel uses Python identifier ionChannel
    __ionChannel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ionChannel'), 'ionChannel', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_ionChannel', NmlId, required=True)
    __ionChannel._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1006, 16)
    __ionChannel._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1006, 16)
    
    ionChannel = property(__ionChannel.value, __ionChannel.set, None, None)

    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_number', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __number._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1007, 16)
    __number._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1007, 16)
    
    number = property(__number.value, __number.set, None, None)

    
    # Attribute erev uses Python identifier erev
    __erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'erev'), 'erev', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_erev', Nml2Quantity_voltage)
    __erev._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1009, 16)
    __erev._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1009, 16)
    
    erev = property(__erev.value, __erev.set, None, None)

    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_segmentGroup', NmlId, unicode_default=u'all')
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1012, 16)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1012, 16)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_segment', NmlId)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1013, 16)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1013, 16)
    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpwww_neuroml_orgschemaneuroml2_ChannelPopulation_ion', NmlId)
    __ion._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1015, 16)
    __ion._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1015, 16)
    
    ion = property(__ion.value, __ion.set, None, u'Specifying the ion here again is redundant, this will be set in ionChannel. It is added here\n                        TEMPORARILY as selecting all ca or na conducting channel populations/densities in a cell would be difficult otherwise.\n                        It should be removed in the longer term, due to possible inconsistencies in this value and that in the ionChannel\n                        element. TODO: remove.\n                        ')

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __variableParameter.name() : __variableParameter
    })
    _AttributeMap.update({
        __ionChannel.name() : __ionChannel,
        __number.name() : __number,
        __erev.name() : __erev,
        __segmentGroup.name() : __segmentGroup,
        __segment.name() : __segment,
        __ion.name() : __ion
    })
Namespace.addCategoryObject('typeBinding', u'ChannelPopulation', ChannelPopulation)


# Complex type {http://www.neuroml.org/schema/neuroml2}ChannelDensity with content type ELEMENT_ONLY
class ChannelDensity (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ChannelDensity with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChannelDensity')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1030, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'variableParameter'), 'variableParameter', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_httpwww_neuroml_orgschemaneuroml2variableParameter', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1036, 20), )

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, None)

    
    # Attribute ionChannel uses Python identifier ionChannel
    __ionChannel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ionChannel'), 'ionChannel', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_ionChannel', NmlId, required=True)
    __ionChannel._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1039, 16)
    __ionChannel._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1039, 16)
    
    ionChannel = property(__ionChannel.value, __ionChannel.set, None, None)

    
    # Attribute condDensity uses Python identifier condDensity
    __condDensity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'condDensity'), 'condDensity', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_condDensity', Nml2Quantity_conductanceDensity)
    __condDensity._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1040, 16)
    __condDensity._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1040, 16)
    
    condDensity = property(__condDensity.value, __condDensity.set, None, None)

    
    # Attribute erev uses Python identifier erev
    __erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'erev'), 'erev', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_erev', Nml2Quantity_voltage)
    __erev._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1042, 16)
    __erev._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1042, 16)
    
    erev = property(__erev.value, __erev.set, None, None)

    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_segmentGroup', NmlId, unicode_default=u'all')
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1045, 16)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1045, 16)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_segment', NmlId)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1047, 16)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1047, 16)
    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensity_ion', NmlId)
    __ion._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1049, 16)
    __ion._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1049, 16)
    
    ion = property(__ion.value, __ion.set, None, u'Specifying the ion here again is redundant, this will be set in ionChannel. It is added here\n                        TEMPORARILY as selecting all ca or na conducting channel populations/densities in a cell would be difficult otherwise.\n                        It should be removed in the longer term, due to possible inconsistencies in this value and that in the ionChannel\n                        element. TODO: remove.\n                        ')

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __variableParameter.name() : __variableParameter
    })
    _AttributeMap.update({
        __ionChannel.name() : __ionChannel,
        __condDensity.name() : __condDensity,
        __erev.name() : __erev,
        __segmentGroup.name() : __segmentGroup,
        __segment.name() : __segment,
        __ion.name() : __ion
    })
Namespace.addCategoryObject('typeBinding', u'ChannelDensity', ChannelDensity)


# Complex type {http://www.neuroml.org/schema/neuroml2}ChannelDensityNernst with content type EMPTY
class ChannelDensityNernst (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ChannelDensityNernst with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChannelDensityNernst')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1064, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Attribute ionChannel uses Python identifier ionChannel
    __ionChannel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ionChannel'), 'ionChannel', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensityNernst_ionChannel', NmlId, required=True)
    __ionChannel._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1069, 16)
    __ionChannel._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1069, 16)
    
    ionChannel = property(__ionChannel.value, __ionChannel.set, None, None)

    
    # Attribute condDensity uses Python identifier condDensity
    __condDensity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'condDensity'), 'condDensity', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensityNernst_condDensity', Nml2Quantity_conductanceDensity)
    __condDensity._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1070, 16)
    __condDensity._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1070, 16)
    
    condDensity = property(__condDensity.value, __condDensity.set, None, None)

    
    # Attribute segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensityNernst_segmentGroup', NmlId, unicode_default=u'all')
    __segmentGroup._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1073, 16)
    __segmentGroup._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1073, 16)
    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    
    # Attribute segment uses Python identifier segment
    __segment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensityNernst_segment', NmlId)
    __segment._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1075, 16)
    __segment._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1075, 16)
    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpwww_neuroml_orgschemaneuroml2_ChannelDensityNernst_ion', NmlId)
    __ion._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1077, 16)
    __ion._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1077, 16)
    
    ion = property(__ion.value, __ion.set, None, u'Specifying the ion here again is redundant, this will be set in ionChannel. It is added here\n                        TEMPORARILY as selecting all ca or na conducting channel populations/densities in a cell would be difficult otherwise.\n                        It should be removed in the longer term, due to possible inconsistencies in this value and that in the ionChannel\n                        element. TODO: remove.\n                        ')

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ionChannel.name() : __ionChannel,
        __condDensity.name() : __condDensity,
        __segmentGroup.name() : __segmentGroup,
        __segment.name() : __segment,
        __ion.name() : __ion
    })
Namespace.addCategoryObject('typeBinding', u'ChannelDensityNernst', ChannelDensityNernst)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExtracellularProperties with content type ELEMENT_ONLY
class ExtracellularProperties (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExtracellularProperties with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExtracellularProperties')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1184, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}species uses Python identifier species
    __species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_ExtracellularProperties_httpwww_neuroml_orgschemaneuroml2species', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1189, 20), )

    
    species = property(__species.value, __species.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __species.name() : __species
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ExtracellularProperties', ExtracellularProperties)


# Complex type {http://www.neuroml.org/schema/neuroml2}ReactionScheme with content type ELEMENT_ONLY
class ReactionScheme (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ReactionScheme with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReactionScheme')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1206, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'source'), 'source', '__httpwww_neuroml_orgschemaneuroml2_ReactionScheme_source', pyxb.binding.datatypes.string, required=True)
    __source._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1213, 16)
    __source._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1213, 16)
    
    source = property(__source.value, __source.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_ReactionScheme_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1214, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1214, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __source.name() : __source,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'ReactionScheme', ReactionScheme)


# Complex type {http://www.neuroml.org/schema/neuroml2}Space with content type ELEMENT_ONLY
class Space (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Space with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Space')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1390, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}structure uses Python identifier structure
    __structure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'structure'), 'structure', '__httpwww_neuroml_orgschemaneuroml2_Space_httpwww_neuroml_orgschemaneuroml2structure', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1395, 20), )

    
    structure = property(__structure.value, __structure.set, None, None)

    
    # Attribute basedOn uses Python identifier basedOn
    __basedOn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'basedOn'), 'basedOn', '__httpwww_neuroml_orgschemaneuroml2_Space_basedOn', allowedSpaces)
    __basedOn._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1397, 16)
    __basedOn._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1397, 16)
    
    basedOn = property(__basedOn.value, __basedOn.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __structure.name() : __structure
    })
    _AttributeMap.update({
        __basedOn.name() : __basedOn
    })
Namespace.addCategoryObject('typeBinding', u'Space', Space)


# Complex type {http://www.neuroml.org/schema/neuroml2}Region with content type ELEMENT_ONLY
class Region (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Region with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Region')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1425, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Attribute space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'space'), 'space', '__httpwww_neuroml_orgschemaneuroml2_Region_space', NmlId)
    __space._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1433, 16)
    __space._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1433, 16)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __space.name() : __space
    })
Namespace.addCategoryObject('typeBinding', u'Region', Region)


# Complex type {http://www.neuroml.org/schema/neuroml2}CellSet with content type ELEMENT_ONLY
class CellSet (Base):
    """Complex type {http://www.neuroml.org/schema/neuroml2}CellSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CellSet')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1523, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Attribute select uses Python identifier select
    __select = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'select'), 'select', '__httpwww_neuroml_orgschemaneuroml2_CellSet_select', pyxb.binding.datatypes.string, required=True)
    __select._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1531, 16)
    __select._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1531, 16)
    
    select = property(__select.value, __select.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __select.name() : __select
    })
Namespace.addCategoryObject('typeBinding', u'CellSet', CellSet)


# Complex type {http://www.neuroml.org/schema/neuroml2}Projection with content type ELEMENT_ONLY
class Projection (Base):
    """Subject to change as it gets tested with LEMS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Projection')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1548, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}connection uses Python identifier connection
    __connection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'connection'), 'connection', '__httpwww_neuroml_orgschemaneuroml2_Projection_httpwww_neuroml_orgschemaneuroml2connection', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1555, 20), )

    
    connection = property(__connection.value, __connection.set, None, None)

    
    # Attribute presynapticPopulation uses Python identifier presynapticPopulation
    __presynapticPopulation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'presynapticPopulation'), 'presynapticPopulation', '__httpwww_neuroml_orgschemaneuroml2_Projection_presynapticPopulation', NmlId)
    __presynapticPopulation._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1557, 16)
    __presynapticPopulation._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1557, 16)
    
    presynapticPopulation = property(__presynapticPopulation.value, __presynapticPopulation.set, None, None)

    
    # Attribute postsynapticPopulation uses Python identifier postsynapticPopulation
    __postsynapticPopulation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'postsynapticPopulation'), 'postsynapticPopulation', '__httpwww_neuroml_orgschemaneuroml2_Projection_postsynapticPopulation', NmlId)
    __postsynapticPopulation._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1558, 16)
    __postsynapticPopulation._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1558, 16)
    
    postsynapticPopulation = property(__postsynapticPopulation.value, __postsynapticPopulation.set, None, None)

    
    # Attribute synapse uses Python identifier synapse
    __synapse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse'), 'synapse', '__httpwww_neuroml_orgschemaneuroml2_Projection_synapse', NmlId)
    __synapse._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1559, 16)
    __synapse._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1559, 16)
    
    synapse = property(__synapse.value, __synapse.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __connection.name() : __connection
    })
    _AttributeMap.update({
        __presynapticPopulation.name() : __presynapticPopulation,
        __postsynapticPopulation.name() : __postsynapticPopulation,
        __synapse.name() : __synapse
    })
Namespace.addCategoryObject('typeBinding', u'Projection', Projection)


# Complex type {http://www.neuroml.org/schema/neuroml2}InputList with content type ELEMENT_ONLY
class InputList (Base):
    """Subject to change as it gets tested with LEMS"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'InputList')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1590, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'input'), 'input', '__httpwww_neuroml_orgschemaneuroml2_InputList_httpwww_neuroml_orgschemaneuroml2input', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1597, 20), )

    
    input = property(__input.value, __input.set, None, None)

    
    # Attribute population uses Python identifier population
    __population = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'population'), 'population', '__httpwww_neuroml_orgschemaneuroml2_InputList_population', NmlId)
    __population._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1599, 16)
    __population._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1599, 16)
    
    population = property(__population.value, __population.set, None, None)

    
    # Attribute component uses Python identifier component
    __component = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'component'), 'component', '__httpwww_neuroml_orgschemaneuroml2_InputList_component', NmlId)
    __component._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1600, 16)
    __component._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1600, 16)
    
    component = property(__component.value, __component.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    _ElementMap.update({
        __input.name() : __input
    })
    _AttributeMap.update({
        __population.name() : __population,
        __component.name() : __component
    })
Namespace.addCategoryObject('typeBinding', u'InputList', InputList)


# Complex type {http://www.neuroml.org/schema/neuroml2}Standalone with content type ELEMENT_ONLY
class Standalone (Base):
    """Elements which can stand alone and be referenced by id, e.g. cell, morphology."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Standalone')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1842, 4)
    _ElementMap = Base._ElementMap.copy()
    _AttributeMap = Base._AttributeMap.copy()
    # Base type is Base
    
    # Element {http://www.neuroml.org/schema/neuroml2}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_neuroml_orgschemaneuroml2_Standalone_httpwww_neuroml_orgschemaneuroml2notes', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'annotation'), 'annotation', '__httpwww_neuroml_orgschemaneuroml2_Standalone_httpwww_neuroml_orgschemaneuroml2annotation', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20), )

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid uses Python identifier metaid
    __metaid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'metaid'), 'metaid', '__httpwww_neuroml_orgschemaneuroml2_Standalone_metaid', MetaId)
    __metaid._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1855, 16)
    __metaid._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1855, 16)
    
    metaid = property(__metaid.value, __metaid.set, None, None)

    _ElementMap.update({
        __notes.name() : __notes,
        __annotation.name() : __annotation
    })
    _AttributeMap.update({
        __metaid.name() : __metaid
    })
Namespace.addCategoryObject('typeBinding', u'Standalone', Standalone)


# Complex type {http://www.neuroml.org/schema/neuroml2}NeuroMLDocument with content type ELEMENT_ONLY
class NeuroMLDocument (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}NeuroMLDocument with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NeuroMLDocument')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 247, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'include'), 'include', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2include', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 255, 20), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}extracellularProperties uses Python identifier extracellularProperties
    __extracellularProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), 'extracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2extracellularProperties', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 257, 20), )

    
    extracellularProperties = property(__extracellularProperties.value, __extracellularProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}intracellularProperties uses Python identifier intracellularProperties
    __intracellularProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties'), 'intracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2intracellularProperties', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 258, 20), )

    
    intracellularProperties = property(__intracellularProperties.value, __intracellularProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}morphology uses Python identifier morphology
    __morphology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'morphology'), 'morphology', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2morphology', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 260, 20), )

    
    morphology = property(__morphology.value, __morphology.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}ionChannel uses Python identifier ionChannel
    __ionChannel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ionChannel'), 'ionChannel', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2ionChannel', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 262, 20), )

    
    ionChannel = property(__ionChannel.value, __ionChannel.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}biophysicalProperties uses Python identifier biophysicalProperties
    __biophysicalProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties'), 'biophysicalProperties', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2biophysicalProperties', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 269, 20), )

    
    biophysicalProperties = property(__biophysicalProperties.value, __biophysicalProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}network uses Python identifier network
    __network = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'network'), 'network', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2network', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 281, 20), )

    
    network = property(__network.value, __network.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}ComponentType uses Python identifier ComponentType
    __ComponentType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ComponentType'), 'ComponentType', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2ComponentType', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 283, 20), )

    
    ComponentType = property(__ComponentType.value, __ComponentType.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}cell uses Python identifier cell
    __cell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cell'), 'cell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2cell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 304, 12), )

    
    cell = property(__cell.value, __cell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}baseCell uses Python identifier baseCell
    __baseCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'baseCell'), 'baseCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2baseCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 305, 12), )

    
    baseCell = property(__baseCell.value, __baseCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}iafTauCell uses Python identifier iafTauCell
    __iafTauCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iafTauCell'), 'iafTauCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2iafTauCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 306, 12), )

    
    iafTauCell = property(__iafTauCell.value, __iafTauCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}iafTauRefCell uses Python identifier iafTauRefCell
    __iafTauRefCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iafTauRefCell'), 'iafTauRefCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2iafTauRefCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 308, 12), )

    
    iafTauRefCell = property(__iafTauRefCell.value, __iafTauRefCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}iafCell uses Python identifier iafCell
    __iafCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iafCell'), 'iafCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2iafCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 310, 12), )

    
    iafCell = property(__iafCell.value, __iafCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}iafRefCell uses Python identifier iafRefCell
    __iafRefCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'iafRefCell'), 'iafRefCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2iafRefCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 312, 12), )

    
    iafRefCell = property(__iafRefCell.value, __iafRefCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}izhikevichCell uses Python identifier izhikevichCell
    __izhikevichCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'izhikevichCell'), 'izhikevichCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2izhikevichCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 314, 12), )

    
    izhikevichCell = property(__izhikevichCell.value, __izhikevichCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}adExIaFCell uses Python identifier adExIaFCell
    __adExIaFCell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'adExIaFCell'), 'adExIaFCell', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2adExIaFCell', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 315, 12), )

    
    adExIaFCell = property(__adExIaFCell.value, __adExIaFCell.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}IF_curr_alpha uses Python identifier IF_curr_alpha
    __IF_curr_alpha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_alpha'), 'IF_curr_alpha', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2IF_curr_alpha', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 325, 12), )

    
    IF_curr_alpha = property(__IF_curr_alpha.value, __IF_curr_alpha.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}IF_curr_exp uses Python identifier IF_curr_exp
    __IF_curr_exp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_exp'), 'IF_curr_exp', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2IF_curr_exp', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 326, 12), )

    
    IF_curr_exp = property(__IF_curr_exp.value, __IF_curr_exp.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}IF_cond_alpha uses Python identifier IF_cond_alpha
    __IF_cond_alpha = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_alpha'), 'IF_cond_alpha', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2IF_cond_alpha', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 327, 12), )

    
    IF_cond_alpha = property(__IF_cond_alpha.value, __IF_cond_alpha.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}IF_cond_exp uses Python identifier IF_cond_exp
    __IF_cond_exp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_exp'), 'IF_cond_exp', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2IF_cond_exp', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 328, 12), )

    
    IF_cond_exp = property(__IF_cond_exp.value, __IF_cond_exp.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}EIF_cond_exp_isfa_ista uses Python identifier EIF_cond_exp_isfa_ista
    __EIF_cond_exp_isfa_ista = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_exp_isfa_ista'), 'EIF_cond_exp_isfa_ista', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2EIF_cond_exp_isfa_ista', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 329, 12), )

    
    EIF_cond_exp_isfa_ista = property(__EIF_cond_exp_isfa_ista.value, __EIF_cond_exp_isfa_ista.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}EIF_cond_alpha_isfa_ista uses Python identifier EIF_cond_alpha_isfa_ista
    __EIF_cond_alpha_isfa_ista = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_alpha_isfa_ista'), 'EIF_cond_alpha_isfa_ista', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2EIF_cond_alpha_isfa_ista', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 330, 12), )

    
    EIF_cond_alpha_isfa_ista = property(__EIF_cond_alpha_isfa_ista.value, __EIF_cond_alpha_isfa_ista.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}HH_cond_exp uses Python identifier HH_cond_exp
    __HH_cond_exp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'HH_cond_exp'), 'HH_cond_exp', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2HH_cond_exp', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 331, 12), )

    
    HH_cond_exp = property(__HH_cond_exp.value, __HH_cond_exp.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}expOneSynapse uses Python identifier expOneSynapse
    __expOneSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expOneSynapse'), 'expOneSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2expOneSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 343, 12), )

    
    expOneSynapse = property(__expOneSynapse.value, __expOneSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}expTwoSynapse uses Python identifier expTwoSynapse
    __expTwoSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expTwoSynapse'), 'expTwoSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2expTwoSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 344, 12), )

    
    expTwoSynapse = property(__expTwoSynapse.value, __expTwoSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}blockingPlasticSynapse uses Python identifier blockingPlasticSynapse
    __blockingPlasticSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'blockingPlasticSynapse'), 'blockingPlasticSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2blockingPlasticSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 345, 5), )

    
    blockingPlasticSynapse = property(__blockingPlasticSynapse.value, __blockingPlasticSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}expCondSynapse uses Python identifier expCondSynapse
    __expCondSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expCondSynapse'), 'expCondSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2expCondSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 355, 12), )

    
    expCondSynapse = property(__expCondSynapse.value, __expCondSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}alphaCondSynapse uses Python identifier alphaCondSynapse
    __alphaCondSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alphaCondSynapse'), 'alphaCondSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2alphaCondSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 356, 12), )

    
    alphaCondSynapse = property(__alphaCondSynapse.value, __alphaCondSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}expCurrSynapse uses Python identifier expCurrSynapse
    __expCurrSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expCurrSynapse'), 'expCurrSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2expCurrSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 357, 12), )

    
    expCurrSynapse = property(__expCurrSynapse.value, __expCurrSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}alphaCurrSynapse uses Python identifier alphaCurrSynapse
    __alphaCurrSynapse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alphaCurrSynapse'), 'alphaCurrSynapse', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2alphaCurrSynapse', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 358, 12), )

    
    alphaCurrSynapse = property(__alphaCurrSynapse.value, __alphaCurrSynapse.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}pulseGenerator uses Python identifier pulseGenerator
    __pulseGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pulseGenerator'), 'pulseGenerator', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2pulseGenerator', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 370, 1), )

    
    pulseGenerator = property(__pulseGenerator.value, __pulseGenerator.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}sineGenerator uses Python identifier sineGenerator
    __sineGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sineGenerator'), 'sineGenerator', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2sineGenerator', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 372, 1), )

    
    sineGenerator = property(__sineGenerator.value, __sineGenerator.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}rampGenerator uses Python identifier rampGenerator
    __rampGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'rampGenerator'), 'rampGenerator', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2rampGenerator', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 374, 1), )

    
    rampGenerator = property(__rampGenerator.value, __rampGenerator.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}voltageClamp uses Python identifier voltageClamp
    __voltageClamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'voltageClamp'), 'voltageClamp', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2voltageClamp', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 376, 1), )

    
    voltageClamp = property(__voltageClamp.value, __voltageClamp.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}spikeArray uses Python identifier spikeArray
    __spikeArray = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spikeArray'), 'spikeArray', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2spikeArray', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 378, 1), )

    
    spikeArray = property(__spikeArray.value, __spikeArray.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}spikeGenerator uses Python identifier spikeGenerator
    __spikeGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spikeGenerator'), 'spikeGenerator', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2spikeGenerator', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 380, 1), )

    
    spikeGenerator = property(__spikeGenerator.value, __spikeGenerator.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}spikeGeneratorRandom uses Python identifier spikeGeneratorRandom
    __spikeGeneratorRandom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorRandom'), 'spikeGeneratorRandom', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2spikeGeneratorRandom', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 382, 1), )

    
    spikeGeneratorRandom = property(__spikeGeneratorRandom.value, __spikeGeneratorRandom.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}spikeGeneratorPoisson uses Python identifier spikeGeneratorPoisson
    __spikeGeneratorPoisson = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorPoisson'), 'spikeGeneratorPoisson', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2spikeGeneratorPoisson', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 384, 1), )

    
    spikeGeneratorPoisson = property(__spikeGeneratorPoisson.value, __spikeGeneratorPoisson.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}SpikeSourcePoisson uses Python identifier SpikeSourcePoisson
    __SpikeSourcePoisson = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SpikeSourcePoisson'), 'SpikeSourcePoisson', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2SpikeSourcePoisson', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 394, 12), )

    
    SpikeSourcePoisson = property(__SpikeSourcePoisson.value, __SpikeSourcePoisson.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}decayingPoolConcentrationModel uses Python identifier decayingPoolConcentrationModel
    __decayingPoolConcentrationModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'decayingPoolConcentrationModel'), 'decayingPoolConcentrationModel', '__httpwww_neuroml_orgschemaneuroml2_NeuroMLDocument_httpwww_neuroml_orgschemaneuroml2decayingPoolConcentrationModel', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 405, 12), )

    
    decayingPoolConcentrationModel = property(__decayingPoolConcentrationModel.value, __decayingPoolConcentrationModel.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __include.name() : __include,
        __extracellularProperties.name() : __extracellularProperties,
        __intracellularProperties.name() : __intracellularProperties,
        __morphology.name() : __morphology,
        __ionChannel.name() : __ionChannel,
        __biophysicalProperties.name() : __biophysicalProperties,
        __network.name() : __network,
        __ComponentType.name() : __ComponentType,
        __cell.name() : __cell,
        __baseCell.name() : __baseCell,
        __iafTauCell.name() : __iafTauCell,
        __iafTauRefCell.name() : __iafTauRefCell,
        __iafCell.name() : __iafCell,
        __iafRefCell.name() : __iafRefCell,
        __izhikevichCell.name() : __izhikevichCell,
        __adExIaFCell.name() : __adExIaFCell,
        __IF_curr_alpha.name() : __IF_curr_alpha,
        __IF_curr_exp.name() : __IF_curr_exp,
        __IF_cond_alpha.name() : __IF_cond_alpha,
        __IF_cond_exp.name() : __IF_cond_exp,
        __EIF_cond_exp_isfa_ista.name() : __EIF_cond_exp_isfa_ista,
        __EIF_cond_alpha_isfa_ista.name() : __EIF_cond_alpha_isfa_ista,
        __HH_cond_exp.name() : __HH_cond_exp,
        __expOneSynapse.name() : __expOneSynapse,
        __expTwoSynapse.name() : __expTwoSynapse,
        __blockingPlasticSynapse.name() : __blockingPlasticSynapse,
        __expCondSynapse.name() : __expCondSynapse,
        __alphaCondSynapse.name() : __alphaCondSynapse,
        __expCurrSynapse.name() : __expCurrSynapse,
        __alphaCurrSynapse.name() : __alphaCurrSynapse,
        __pulseGenerator.name() : __pulseGenerator,
        __sineGenerator.name() : __sineGenerator,
        __rampGenerator.name() : __rampGenerator,
        __voltageClamp.name() : __voltageClamp,
        __spikeArray.name() : __spikeArray,
        __spikeGenerator.name() : __spikeGenerator,
        __spikeGeneratorRandom.name() : __spikeGeneratorRandom,
        __spikeGeneratorPoisson.name() : __spikeGeneratorPoisson,
        __SpikeSourcePoisson.name() : __SpikeSourcePoisson,
        __decayingPoolConcentrationModel.name() : __decayingPoolConcentrationModel
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'NeuroMLDocument', NeuroMLDocument)


# Complex type {http://www.neuroml.org/schema/neuroml2}IonChannel with content type ELEMENT_ONLY
class IonChannel (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IonChannel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IonChannel')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 413, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}gate uses Python identifier gate
    __gate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gate'), 'gate', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_httpwww_neuroml_orgschemaneuroml2gate', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 418, 20), )

    
    gate = property(__gate.value, __gate.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}gateHHrates uses Python identifier gateHHrates
    __gateHHrates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gateHHrates'), 'gateHHrates', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_httpwww_neuroml_orgschemaneuroml2gateHHrates', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 419, 20), )

    
    gateHHrates = property(__gateHHrates.value, __gateHHrates.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}gateHHratesTau uses Python identifier gateHHratesTau
    __gateHHratesTau = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesTau'), 'gateHHratesTau', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_httpwww_neuroml_orgschemaneuroml2gateHHratesTau', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 420, 20), )

    
    gateHHratesTau = property(__gateHHratesTau.value, __gateHHratesTau.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}gateHHtauInf uses Python identifier gateHHtauInf
    __gateHHtauInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gateHHtauInf'), 'gateHHtauInf', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_httpwww_neuroml_orgschemaneuroml2gateHHtauInf', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 421, 20), )

    
    gateHHtauInf = property(__gateHHtauInf.value, __gateHHtauInf.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}gateHHratesInf uses Python identifier gateHHratesInf
    __gateHHratesInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesInf'), 'gateHHratesInf', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_httpwww_neuroml_orgschemaneuroml2gateHHratesInf', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 422, 20), )

    
    gateHHratesInf = property(__gateHHratesInf.value, __gateHHratesInf.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute species uses Python identifier species
    __species = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'species'), 'species', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_species', NmlId)
    __species._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 425, 16)
    __species._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 425, 16)
    
    species = property(__species.value, __species.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_type', channelTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 427, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 427, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute conductance uses Python identifier conductance
    __conductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'conductance'), 'conductance', '__httpwww_neuroml_orgschemaneuroml2_IonChannel_conductance', Nml2Quantity_conductance)
    __conductance._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 429, 16)
    __conductance._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 429, 16)
    
    conductance = property(__conductance.value, __conductance.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __gate.name() : __gate,
        __gateHHrates.name() : __gateHHrates,
        __gateHHratesTau.name() : __gateHHratesTau,
        __gateHHtauInf.name() : __gateHHtauInf,
        __gateHHratesInf.name() : __gateHHratesInf
    })
    _AttributeMap.update({
        __species.name() : __species,
        __type.name() : __type,
        __conductance.name() : __conductance
    })
Namespace.addCategoryObject('typeBinding', u'IonChannel', IonChannel)


# Complex type {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel with content type ELEMENT_ONLY
class DecayingPoolConcentrationModel (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecayingPoolConcentrationModel')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 576, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpwww_neuroml_orgschemaneuroml2_DecayingPoolConcentrationModel_ion', NmlId, required=True)
    __ion._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 581, 16)
    __ion._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 581, 16)
    
    ion = property(__ion.value, __ion.set, None, u"Should not be required, as it's present on the species element!")

    
    # Attribute restingConc uses Python identifier restingConc
    __restingConc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'restingConc'), 'restingConc', '__httpwww_neuroml_orgschemaneuroml2_DecayingPoolConcentrationModel_restingConc', Nml2Quantity_concentration, required=True)
    __restingConc._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 586, 16)
    __restingConc._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 586, 16)
    
    restingConc = property(__restingConc.value, __restingConc.set, None, None)

    
    # Attribute decayConstant uses Python identifier decayConstant
    __decayConstant = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decayConstant'), 'decayConstant', '__httpwww_neuroml_orgschemaneuroml2_DecayingPoolConcentrationModel_decayConstant', Nml2Quantity_time, required=True)
    __decayConstant._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 587, 16)
    __decayConstant._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 587, 16)
    
    decayConstant = property(__decayConstant.value, __decayConstant.set, None, None)

    
    # Attribute shellThickness uses Python identifier shellThickness
    __shellThickness = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shellThickness'), 'shellThickness', '__httpwww_neuroml_orgschemaneuroml2_DecayingPoolConcentrationModel_shellThickness', Nml2Quantity_length, required=True)
    __shellThickness._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 588, 16)
    __shellThickness._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 588, 16)
    
    shellThickness = property(__shellThickness.value, __shellThickness.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __ion.name() : __ion,
        __restingConc.name() : __restingConc,
        __decayConstant.name() : __decayConstant,
        __shellThickness.name() : __shellThickness
    })
Namespace.addCategoryObject('typeBinding', u'DecayingPoolConcentrationModel', DecayingPoolConcentrationModel)


# Complex type {http://www.neuroml.org/schema/neuroml2}BaseSynapse with content type ELEMENT_ONLY
class BaseSynapse (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BaseSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 600, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseSynapse', BaseSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}BaseCell with content type ELEMENT_ONLY
class BaseCell (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BaseCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 701, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BaseCell', BaseCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}Morphology with content type ELEMENT_ONLY
class Morphology (Standalone):
    """Standalone element which is usually inside a single cell, but could be outside and
                              referenced by id.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Morphology')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 819, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'segment'), 'segment', '__httpwww_neuroml_orgschemaneuroml2_Morphology_httpwww_neuroml_orgschemaneuroml2segment', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 831, 20), )

    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}segmentGroup uses Python identifier segmentGroup
    __segmentGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'segmentGroup'), 'segmentGroup', '__httpwww_neuroml_orgschemaneuroml2_Morphology_httpwww_neuroml_orgschemaneuroml2segmentGroup', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 832, 20), )

    
    segmentGroup = property(__segmentGroup.value, __segmentGroup.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __segment.name() : __segment,
        __segmentGroup.name() : __segmentGroup
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Morphology', Morphology)


# Complex type {http://www.neuroml.org/schema/neuroml2}BiophysicalProperties with content type ELEMENT_ONLY
class BiophysicalProperties (Standalone):
    """Standalone element which is usually inside a single cell, but could be outside and
                              referenced by id.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BiophysicalProperties')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 958, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}membraneProperties uses Python identifier membraneProperties
    __membraneProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'membraneProperties'), 'membraneProperties', '__httpwww_neuroml_orgschemaneuroml2_BiophysicalProperties_httpwww_neuroml_orgschemaneuroml2membraneProperties', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 968, 20), )

    
    membraneProperties = property(__membraneProperties.value, __membraneProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}intracellularProperties uses Python identifier intracellularProperties
    __intracellularProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties'), 'intracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_BiophysicalProperties_httpwww_neuroml_orgschemaneuroml2intracellularProperties', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 969, 20), )

    
    intracellularProperties = property(__intracellularProperties.value, __intracellularProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}extracellularProperties uses Python identifier extracellularProperties
    __extracellularProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), 'extracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_BiophysicalProperties_httpwww_neuroml_orgschemaneuroml2extracellularProperties', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 970, 20), )

    
    extracellularProperties = property(__extracellularProperties.value, __extracellularProperties.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __membraneProperties.name() : __membraneProperties,
        __intracellularProperties.name() : __intracellularProperties,
        __extracellularProperties.name() : __extracellularProperties
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BiophysicalProperties', BiophysicalProperties)


# Complex type {http://www.neuroml.org/schema/neuroml2}PulseGenerator with content type ELEMENT_ONLY
class PulseGenerator (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}PulseGenerator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PulseGenerator')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1229, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpwww_neuroml_orgschemaneuroml2_PulseGenerator_delay', Nml2Quantity_time, required=True)
    __delay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1232, 14)
    __delay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1232, 14)
    
    delay = property(__delay.value, __delay.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpwww_neuroml_orgschemaneuroml2_PulseGenerator_duration', Nml2Quantity_time, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1234, 14)
    __duration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1234, 14)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute amplitude uses Python identifier amplitude
    __amplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'amplitude'), 'amplitude', '__httpwww_neuroml_orgschemaneuroml2_PulseGenerator_amplitude', Nml2Quantity_current, required=True)
    __amplitude._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1236, 14)
    __amplitude._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1236, 14)
    
    amplitude = property(__amplitude.value, __amplitude.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delay.name() : __delay,
        __duration.name() : __duration,
        __amplitude.name() : __amplitude
    })
Namespace.addCategoryObject('typeBinding', u'PulseGenerator', PulseGenerator)


# Complex type {http://www.neuroml.org/schema/neuroml2}SineGenerator with content type ELEMENT_ONLY
class SineGenerator (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SineGenerator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SineGenerator')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1243, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpwww_neuroml_orgschemaneuroml2_SineGenerator_delay', Nml2Quantity_time, required=True)
    __delay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1246, 14)
    __delay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1246, 14)
    
    delay = property(__delay.value, __delay.set, None, None)

    
    # Attribute phase uses Python identifier phase
    __phase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'phase'), 'phase', '__httpwww_neuroml_orgschemaneuroml2_SineGenerator_phase', Nml2Quantity_none, required=True)
    __phase._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1248, 7)
    __phase._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1248, 7)
    
    phase = property(__phase.value, __phase.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpwww_neuroml_orgschemaneuroml2_SineGenerator_duration', Nml2Quantity_time, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1250, 14)
    __duration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1250, 14)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute amplitude uses Python identifier amplitude
    __amplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'amplitude'), 'amplitude', '__httpwww_neuroml_orgschemaneuroml2_SineGenerator_amplitude', Nml2Quantity_current, required=True)
    __amplitude._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1252, 14)
    __amplitude._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1252, 14)
    
    amplitude = property(__amplitude.value, __amplitude.set, None, None)

    
    # Attribute period uses Python identifier period
    __period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'period'), 'period', '__httpwww_neuroml_orgschemaneuroml2_SineGenerator_period', Nml2Quantity_time, required=True)
    __period._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1255, 7)
    __period._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1255, 7)
    
    period = property(__period.value, __period.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delay.name() : __delay,
        __phase.name() : __phase,
        __duration.name() : __duration,
        __amplitude.name() : __amplitude,
        __period.name() : __period
    })
Namespace.addCategoryObject('typeBinding', u'SineGenerator', SineGenerator)


# Complex type {http://www.neuroml.org/schema/neuroml2}RampGenerator with content type ELEMENT_ONLY
class RampGenerator (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}RampGenerator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RampGenerator')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1261, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpwww_neuroml_orgschemaneuroml2_RampGenerator_delay', Nml2Quantity_time, required=True)
    __delay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1264, 14)
    __delay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1264, 14)
    
    delay = property(__delay.value, __delay.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpwww_neuroml_orgschemaneuroml2_RampGenerator_duration', Nml2Quantity_time, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1266, 14)
    __duration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1266, 14)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute startAmplitude uses Python identifier startAmplitude
    __startAmplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'startAmplitude'), 'startAmplitude', '__httpwww_neuroml_orgschemaneuroml2_RampGenerator_startAmplitude', Nml2Quantity_current, required=True)
    __startAmplitude._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1268, 14)
    __startAmplitude._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1268, 14)
    
    startAmplitude = property(__startAmplitude.value, __startAmplitude.set, None, None)

    
    # Attribute finishAmplitude uses Python identifier finishAmplitude
    __finishAmplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'finishAmplitude'), 'finishAmplitude', '__httpwww_neuroml_orgschemaneuroml2_RampGenerator_finishAmplitude', Nml2Quantity_current, required=True)
    __finishAmplitude._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1271, 14)
    __finishAmplitude._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1271, 14)
    
    finishAmplitude = property(__finishAmplitude.value, __finishAmplitude.set, None, None)

    
    # Attribute baselineAmplitude uses Python identifier baselineAmplitude
    __baselineAmplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'baselineAmplitude'), 'baselineAmplitude', '__httpwww_neuroml_orgschemaneuroml2_RampGenerator_baselineAmplitude', Nml2Quantity_current, required=True)
    __baselineAmplitude._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1274, 14)
    __baselineAmplitude._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1274, 14)
    
    baselineAmplitude = property(__baselineAmplitude.value, __baselineAmplitude.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delay.name() : __delay,
        __duration.name() : __duration,
        __startAmplitude.name() : __startAmplitude,
        __finishAmplitude.name() : __finishAmplitude,
        __baselineAmplitude.name() : __baselineAmplitude
    })
Namespace.addCategoryObject('typeBinding', u'RampGenerator', RampGenerator)


# Complex type {http://www.neuroml.org/schema/neuroml2}VoltageClamp with content type ELEMENT_ONLY
class VoltageClamp (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}VoltageClamp with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'VoltageClamp')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1281, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpwww_neuroml_orgschemaneuroml2_VoltageClamp_delay', Nml2Quantity_time, required=True)
    __delay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1284, 14)
    __delay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1284, 14)
    
    delay = property(__delay.value, __delay.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpwww_neuroml_orgschemaneuroml2_VoltageClamp_duration', Nml2Quantity_time, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1286, 14)
    __duration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1286, 14)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute targetVoltage uses Python identifier targetVoltage
    __targetVoltage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'targetVoltage'), 'targetVoltage', '__httpwww_neuroml_orgschemaneuroml2_VoltageClamp_targetVoltage', Nml2Quantity_voltage, required=True)
    __targetVoltage._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1288, 7)
    __targetVoltage._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1288, 7)
    
    targetVoltage = property(__targetVoltage.value, __targetVoltage.set, None, None)

    
    # Attribute seriesResistance uses Python identifier seriesResistance
    __seriesResistance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'seriesResistance'), 'seriesResistance', '__httpwww_neuroml_orgschemaneuroml2_VoltageClamp_seriesResistance', Nml2Quantity_resistance, required=True)
    __seriesResistance._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1291, 7)
    __seriesResistance._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1291, 7)
    
    seriesResistance = property(__seriesResistance.value, __seriesResistance.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __delay.name() : __delay,
        __duration.name() : __duration,
        __targetVoltage.name() : __targetVoltage,
        __seriesResistance.name() : __seriesResistance
    })
Namespace.addCategoryObject('typeBinding', u'VoltageClamp', VoltageClamp)


# Complex type {http://www.neuroml.org/schema/neuroml2}Spike with content type ELEMENT_ONLY
class Spike (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Spike with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Spike')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1298, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute time uses Python identifier time
    __time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__httpwww_neuroml_orgschemaneuroml2_Spike_time', Nml2Quantity_time, required=True)
    __time._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1301, 3)
    __time._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1301, 3)
    
    time = property(__time.value, __time.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __time.name() : __time
    })
Namespace.addCategoryObject('typeBinding', u'Spike', Spike)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpikeArray with content type ELEMENT_ONLY
class SpikeArray (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpikeArray with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpikeArray')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1307, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}spike uses Python identifier spike
    __spike = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'spike'), 'spike', '__httpwww_neuroml_orgschemaneuroml2_SpikeArray_httpwww_neuroml_orgschemaneuroml2spike', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1311, 12), )

    
    spike = property(__spike.value, __spike.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __spike.name() : __spike
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SpikeArray', SpikeArray)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGenerator with content type ELEMENT_ONLY
class SpikeGenerator (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGenerator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpikeGenerator')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1318, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute period uses Python identifier period
    __period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'period'), 'period', '__httpwww_neuroml_orgschemaneuroml2_SpikeGenerator_period', Nml2Quantity_time, required=True)
    __period._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1321, 3)
    __period._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1321, 3)
    
    period = property(__period.value, __period.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __period.name() : __period
    })
Namespace.addCategoryObject('typeBinding', u'SpikeGenerator', SpikeGenerator)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGeneratorRandom with content type ELEMENT_ONLY
class SpikeGeneratorRandom (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGeneratorRandom with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpikeGeneratorRandom')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1327, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute maxISI uses Python identifier maxISI
    __maxISI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxISI'), 'maxISI', '__httpwww_neuroml_orgschemaneuroml2_SpikeGeneratorRandom_maxISI', Nml2Quantity_time, required=True)
    __maxISI._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1330, 3)
    __maxISI._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1330, 3)
    
    maxISI = property(__maxISI.value, __maxISI.set, None, None)

    
    # Attribute minISI uses Python identifier minISI
    __minISI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'minISI'), 'minISI', '__httpwww_neuroml_orgschemaneuroml2_SpikeGeneratorRandom_minISI', Nml2Quantity_time, required=True)
    __minISI._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1332, 3)
    __minISI._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1332, 3)
    
    minISI = property(__minISI.value, __minISI.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __maxISI.name() : __maxISI,
        __minISI.name() : __minISI
    })
Namespace.addCategoryObject('typeBinding', u'SpikeGeneratorRandom', SpikeGeneratorRandom)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGeneratorPoisson with content type ELEMENT_ONLY
class SpikeGeneratorPoisson (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpikeGeneratorPoisson with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpikeGeneratorPoisson')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1338, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute averageRate uses Python identifier averageRate
    __averageRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'averageRate'), 'averageRate', '__httpwww_neuroml_orgschemaneuroml2_SpikeGeneratorPoisson_averageRate', Nml2Quantity_pertime, required=True)
    __averageRate._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1341, 3)
    __averageRate._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1341, 3)
    
    averageRate = property(__averageRate.value, __averageRate.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __averageRate.name() : __averageRate
    })
Namespace.addCategoryObject('typeBinding', u'SpikeGeneratorPoisson', SpikeGeneratorPoisson)


# Complex type {http://www.neuroml.org/schema/neuroml2}Network with content type ELEMENT_ONLY
class Network (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Network with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Network')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1354, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}space uses Python identifier space
    __space = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'space'), 'space', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2space', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1359, 20), )

    
    space = property(__space.value, __space.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'region'), 'region', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2region', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1360, 20), )

    
    region = property(__region.value, __region.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}extracellularProperties uses Python identifier extracellularProperties
    __extracellularProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), 'extracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2extracellularProperties', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1361, 20), )

    
    extracellularProperties = property(__extracellularProperties.value, __extracellularProperties.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}population uses Python identifier population
    __population = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'population'), 'population', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2population', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1362, 20), )

    
    population = property(__population.value, __population.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}cellSet uses Python identifier cellSet
    __cellSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cellSet'), 'cellSet', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2cellSet', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1363, 20), )

    
    cellSet = property(__cellSet.value, __cellSet.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}synapticConnection uses Python identifier synapticConnection
    __synapticConnection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synapticConnection'), 'synapticConnection', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2synapticConnection', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1365, 20), )

    
    synapticConnection = property(__synapticConnection.value, __synapticConnection.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}projection uses Python identifier projection
    __projection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'projection'), 'projection', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2projection', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1366, 20), )

    
    projection = property(__projection.value, __projection.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}explicitInput uses Python identifier explicitInput
    __explicitInput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'explicitInput'), 'explicitInput', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2explicitInput', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1368, 20), )

    
    explicitInput = property(__explicitInput.value, __explicitInput.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}inputList uses Python identifier inputList
    __inputList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'inputList'), 'inputList', '__httpwww_neuroml_orgschemaneuroml2_Network_httpwww_neuroml_orgschemaneuroml2inputList', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1369, 20), )

    
    inputList = property(__inputList.value, __inputList.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_Network_type', networkTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1372, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1372, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute temperature uses Python identifier temperature
    __temperature = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'temperature'), 'temperature', '__httpwww_neuroml_orgschemaneuroml2_Network_temperature', Nml2Quantity_temperature)
    __temperature._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1373, 16)
    __temperature._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1373, 16)
    
    temperature = property(__temperature.value, __temperature.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __space.name() : __space,
        __region.name() : __region,
        __extracellularProperties.name() : __extracellularProperties,
        __population.name() : __population,
        __cellSet.name() : __cellSet,
        __synapticConnection.name() : __synapticConnection,
        __projection.name() : __projection,
        __explicitInput.name() : __explicitInput,
        __inputList.name() : __inputList
    })
    _AttributeMap.update({
        __type.name() : __type,
        __temperature.name() : __temperature
    })
Namespace.addCategoryObject('typeBinding', u'Network', Network)


# Complex type {http://www.neuroml.org/schema/neuroml2}Population with content type ELEMENT_ONLY
class Population (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Population with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Population')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1440, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element {http://www.neuroml.org/schema/neuroml2}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpwww_neuroml_orgschemaneuroml2_Population_httpwww_neuroml_orgschemaneuroml2layout', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1445, 20), )

    
    layout = property(__layout.value, __layout.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}instance uses Python identifier instance
    __instance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'instance'), 'instance', '__httpwww_neuroml_orgschemaneuroml2_Population_httpwww_neuroml_orgschemaneuroml2instance', True, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1446, 20), )

    
    instance = property(__instance.value, __instance.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cell uses Python identifier cell
    __cell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cell'), 'cell', '__httpwww_neuroml_orgschemaneuroml2_Population_cell', NmlId)
    __cell._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1449, 16)
    __cell._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1449, 16)
    
    cell = property(__cell.value, __cell.set, None, None)

    
    # Attribute network uses Python identifier network
    __network = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'network'), 'network', '__httpwww_neuroml_orgschemaneuroml2_Population_network', NmlId)
    __network._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1450, 16)
    __network._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1450, 16)
    
    network = property(__network.value, __network.set, None, None)

    
    # Attribute component uses Python identifier component
    __component = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'component'), 'component', '__httpwww_neuroml_orgschemaneuroml2_Population_component', NmlId)
    __component._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1451, 16)
    __component._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1451, 16)
    
    component = property(__component.value, __component.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__httpwww_neuroml_orgschemaneuroml2_Population_size', pyxb.binding.datatypes.integer)
    __size._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1453, 16)
    __size._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1453, 16)
    
    size = property(__size.value, __size.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_Population_type', populationTypes)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1455, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1455, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute extracellularProperties uses Python identifier extracellularProperties
    __extracellularProperties = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'extracellularProperties'), 'extracellularProperties', '__httpwww_neuroml_orgschemaneuroml2_Population_extracellularProperties', NmlId)
    __extracellularProperties._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1457, 16)
    __extracellularProperties._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1457, 16)
    
    extracellularProperties = property(__extracellularProperties.value, __extracellularProperties.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __layout.name() : __layout,
        __instance.name() : __instance
    })
    _AttributeMap.update({
        __cell.name() : __cell,
        __network.name() : __network,
        __component.name() : __component,
        __size.name() : __size,
        __type.name() : __type,
        __extracellularProperties.name() : __extracellularProperties
    })
Namespace.addCategoryObject('typeBinding', u'Population', Population)


# Complex type {http://www.neuroml.org/schema/neuroml2}SpikeSourcePoisson with content type ELEMENT_ONLY
class SpikeSourcePoisson (Standalone):
    """Complex type {http://www.neuroml.org/schema/neuroml2}SpikeSourcePoisson with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpikeSourcePoisson')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1793, 4)
    _ElementMap = Standalone._ElementMap.copy()
    _AttributeMap = Standalone._AttributeMap.copy()
    # Base type is Standalone
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute start uses Python identifier start
    __start = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'start'), 'start', '__httpwww_neuroml_orgschemaneuroml2_SpikeSourcePoisson_start', Nml2Quantity_time, required=True)
    __start._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1798, 16)
    __start._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1798, 16)
    
    start = property(__start.value, __start.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpwww_neuroml_orgschemaneuroml2_SpikeSourcePoisson_duration', Nml2Quantity_time, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1799, 16)
    __duration._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1799, 16)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpwww_neuroml_orgschemaneuroml2_SpikeSourcePoisson_rate', Nml2Quantity_pertime, required=True)
    __rate._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1800, 16)
    __rate._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1800, 16)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __start.name() : __start,
        __duration.name() : __duration,
        __rate.name() : __rate
    })
Namespace.addCategoryObject('typeBinding', u'SpikeSourcePoisson', SpikeSourcePoisson)


# Complex type {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse with content type ELEMENT_ONLY
class BaseConductanceBasedSynapse (BaseSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BaseConductanceBasedSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 609, 4)
    _ElementMap = BaseSynapse._ElementMap.copy()
    _AttributeMap = BaseSynapse._AttributeMap.copy()
    # Base type is BaseSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute gbase uses Python identifier gbase
    __gbase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gbase'), 'gbase', '__httpwww_neuroml_orgschemaneuroml2_BaseConductanceBasedSynapse_gbase', Nml2Quantity_conductance, required=True)
    __gbase._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 614, 16)
    __gbase._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 614, 16)
    
    gbase = property(__gbase.value, __gbase.set, None, None)

    
    # Attribute erev uses Python identifier erev
    __erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'erev'), 'erev', '__httpwww_neuroml_orgschemaneuroml2_BaseConductanceBasedSynapse_erev', Nml2Quantity_voltage, required=True)
    __erev._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 615, 16)
    __erev._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 615, 16)
    
    erev = property(__erev.value, __erev.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __gbase.name() : __gbase,
        __erev.name() : __erev
    })
Namespace.addCategoryObject('typeBinding', u'BaseConductanceBasedSynapse', BaseConductanceBasedSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}IaFTauCell with content type ELEMENT_ONLY
class IaFTauCell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IaFTauCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IaFTauCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 709, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute leakReversal uses Python identifier leakReversal
    __leakReversal = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'leakReversal'), 'leakReversal', '__httpwww_neuroml_orgschemaneuroml2_IaFTauCell_leakReversal', Nml2Quantity_voltage, required=True)
    __leakReversal._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 712, 16)
    __leakReversal._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 712, 16)
    
    leakReversal = property(__leakReversal.value, __leakReversal.set, None, None)

    
    # Attribute thresh uses Python identifier thresh
    __thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'thresh'), 'thresh', '__httpwww_neuroml_orgschemaneuroml2_IaFTauCell_thresh', Nml2Quantity_voltage, required=True)
    __thresh._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 713, 16)
    __thresh._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 713, 16)
    
    thresh = property(__thresh.value, __thresh.set, None, None)

    
    # Attribute reset uses Python identifier reset_
    __reset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reset'), 'reset_', '__httpwww_neuroml_orgschemaneuroml2_IaFTauCell_reset', Nml2Quantity_voltage, required=True)
    __reset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 714, 16)
    __reset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 714, 16)
    
    reset_ = property(__reset.value, __reset.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau'), 'tau', '__httpwww_neuroml_orgschemaneuroml2_IaFTauCell_tau', Nml2Quantity_time, required=True)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 715, 16)
    __tau._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 715, 16)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __leakReversal.name() : __leakReversal,
        __thresh.name() : __thresh,
        __reset.name() : __reset,
        __tau.name() : __tau
    })
Namespace.addCategoryObject('typeBinding', u'IaFTauCell', IaFTauCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}IaFCell with content type ELEMENT_ONLY
class IaFCell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IaFCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IaFCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 728, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute leakReversal uses Python identifier leakReversal
    __leakReversal = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'leakReversal'), 'leakReversal', '__httpwww_neuroml_orgschemaneuroml2_IaFCell_leakReversal', Nml2Quantity_voltage, required=True)
    __leakReversal._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 731, 16)
    __leakReversal._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 731, 16)
    
    leakReversal = property(__leakReversal.value, __leakReversal.set, None, None)

    
    # Attribute thresh uses Python identifier thresh
    __thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'thresh'), 'thresh', '__httpwww_neuroml_orgschemaneuroml2_IaFCell_thresh', Nml2Quantity_voltage, required=True)
    __thresh._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 732, 16)
    __thresh._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 732, 16)
    
    thresh = property(__thresh.value, __thresh.set, None, None)

    
    # Attribute reset uses Python identifier reset_
    __reset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reset'), 'reset_', '__httpwww_neuroml_orgschemaneuroml2_IaFCell_reset', Nml2Quantity_voltage, required=True)
    __reset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 733, 16)
    __reset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 733, 16)
    
    reset_ = property(__reset.value, __reset.set, None, None)

    
    # Attribute C uses Python identifier C
    __C = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'C'), 'C', '__httpwww_neuroml_orgschemaneuroml2_IaFCell_C', Nml2Quantity_capacitance, required=True)
    __C._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 734, 16)
    __C._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 734, 16)
    
    C = property(__C.value, __C.set, None, None)

    
    # Attribute leakConductance uses Python identifier leakConductance
    __leakConductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'leakConductance'), 'leakConductance', '__httpwww_neuroml_orgschemaneuroml2_IaFCell_leakConductance', Nml2Quantity_conductance, required=True)
    __leakConductance._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 735, 16)
    __leakConductance._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 735, 16)
    
    leakConductance = property(__leakConductance.value, __leakConductance.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __leakReversal.name() : __leakReversal,
        __thresh.name() : __thresh,
        __reset.name() : __reset,
        __C.name() : __C,
        __leakConductance.name() : __leakConductance
    })
Namespace.addCategoryObject('typeBinding', u'IaFCell', IaFCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}IzhikevichCell with content type ELEMENT_ONLY
class IzhikevichCell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IzhikevichCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IzhikevichCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 748, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute v0 uses Python identifier v0
    __v0 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v0'), 'v0', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_v0', Nml2Quantity_voltage, required=True)
    __v0._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 751, 16)
    __v0._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 751, 16)
    
    v0 = property(__v0.value, __v0.set, None, None)

    
    # Attribute thresh uses Python identifier thresh
    __thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'thresh'), 'thresh', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_thresh', Nml2Quantity_voltage, required=True)
    __thresh._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 752, 16)
    __thresh._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 752, 16)
    
    thresh = property(__thresh.value, __thresh.set, None, None)

    
    # Attribute a uses Python identifier a
    __a = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'a'), 'a', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_a', Nml2Quantity_none, required=True)
    __a._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 753, 16)
    __a._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 753, 16)
    
    a = property(__a.value, __a.set, None, None)

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_b', Nml2Quantity_none, required=True)
    __b._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 754, 16)
    __b._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 754, 16)
    
    b = property(__b.value, __b.set, None, None)

    
    # Attribute c uses Python identifier c
    __c = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'c'), 'c', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_c', Nml2Quantity_none, required=True)
    __c._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 755, 16)
    __c._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 755, 16)
    
    c = property(__c.value, __c.set, None, None)

    
    # Attribute d uses Python identifier d
    __d = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'd'), 'd', '__httpwww_neuroml_orgschemaneuroml2_IzhikevichCell_d', Nml2Quantity_none, required=True)
    __d._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 756, 16)
    __d._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 756, 16)
    
    d = property(__d.value, __d.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __v0.name() : __v0,
        __thresh.name() : __thresh,
        __a.name() : __a,
        __b.name() : __b,
        __c.name() : __c,
        __d.name() : __d
    })
Namespace.addCategoryObject('typeBinding', u'IzhikevichCell', IzhikevichCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}AdExIaFCell with content type ELEMENT_ONLY
class AdExIaFCell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}AdExIaFCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AdExIaFCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 764, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute C uses Python identifier C
    __C = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'C'), 'C', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_C', Nml2Quantity_capacitance, required=True)
    __C._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 767, 16)
    __C._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 767, 16)
    
    C = property(__C.value, __C.set, None, None)

    
    # Attribute gL uses Python identifier gL
    __gL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gL'), 'gL', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_gL', Nml2Quantity_conductance, required=True)
    __gL._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 768, 16)
    __gL._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 768, 16)
    
    gL = property(__gL.value, __gL.set, None, None)

    
    # Attribute EL uses Python identifier EL
    __EL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'EL'), 'EL', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_EL', Nml2Quantity_voltage, required=True)
    __EL._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 769, 16)
    __EL._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 769, 16)
    
    EL = property(__EL.value, __EL.set, None, None)

    
    # Attribute reset uses Python identifier reset_
    __reset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reset'), 'reset_', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_reset', Nml2Quantity_voltage, required=True)
    __reset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 770, 16)
    __reset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 770, 16)
    
    reset_ = property(__reset.value, __reset.set, None, None)

    
    # Attribute VT uses Python identifier VT
    __VT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'VT'), 'VT', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_VT', Nml2Quantity_voltage, required=True)
    __VT._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 771, 16)
    __VT._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 771, 16)
    
    VT = property(__VT.value, __VT.set, None, None)

    
    # Attribute thresh uses Python identifier thresh
    __thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'thresh'), 'thresh', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_thresh', Nml2Quantity_voltage, required=True)
    __thresh._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 772, 16)
    __thresh._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 772, 16)
    
    thresh = property(__thresh.value, __thresh.set, None, None)

    
    # Attribute delT uses Python identifier delT
    __delT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delT'), 'delT', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_delT', Nml2Quantity_voltage, required=True)
    __delT._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 773, 16)
    __delT._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 773, 16)
    
    delT = property(__delT.value, __delT.set, None, None)

    
    # Attribute tauw uses Python identifier tauw
    __tauw = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauw'), 'tauw', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_tauw', Nml2Quantity_time, required=True)
    __tauw._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 774, 16)
    __tauw._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 774, 16)
    
    tauw = property(__tauw.value, __tauw.set, None, None)

    
    # Attribute refract uses Python identifier refract
    __refract = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'refract'), 'refract', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_refract', Nml2Quantity_time, required=True)
    __refract._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 775, 16)
    __refract._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 775, 16)
    
    refract = property(__refract.value, __refract.set, None, None)

    
    # Attribute a uses Python identifier a
    __a = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'a'), 'a', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_a', Nml2Quantity_conductance, required=True)
    __a._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 776, 16)
    __a._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 776, 16)
    
    a = property(__a.value, __a.set, None, None)

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpwww_neuroml_orgschemaneuroml2_AdExIaFCell_b', Nml2Quantity_current, required=True)
    __b._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 777, 16)
    __b._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 777, 16)
    
    b = property(__b.value, __b.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __C.name() : __C,
        __gL.name() : __gL,
        __EL.name() : __EL,
        __reset.name() : __reset,
        __VT.name() : __VT,
        __thresh.name() : __thresh,
        __delT.name() : __delT,
        __tauw.name() : __tauw,
        __refract.name() : __refract,
        __a.name() : __a,
        __b.name() : __b
    })
Namespace.addCategoryObject('typeBinding', u'AdExIaFCell', AdExIaFCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}Cell with content type ELEMENT_ONLY
class Cell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}Cell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Cell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 786, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element {http://www.neuroml.org/schema/neuroml2}morphology uses Python identifier morphology
    __morphology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'morphology'), 'morphology', '__httpwww_neuroml_orgschemaneuroml2_Cell_httpwww_neuroml_orgschemaneuroml2morphology', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 792, 20), )

    
    morphology = property(__morphology.value, __morphology.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}biophysicalProperties uses Python identifier biophysicalProperties
    __biophysicalProperties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties'), 'biophysicalProperties', '__httpwww_neuroml_orgschemaneuroml2_Cell_httpwww_neuroml_orgschemaneuroml2biophysicalProperties', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 793, 20), )

    
    biophysicalProperties = property(__biophysicalProperties.value, __biophysicalProperties.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute morphology uses Python identifier morphology_
    __morphology_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'morphology'), 'morphology_', '__httpwww_neuroml_orgschemaneuroml2_Cell_morphology', NmlId, unicode_default=u'1')
    __morphology_._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 797, 16)
    __morphology_._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 797, 16)
    
    morphology_ = property(__morphology_.value, __morphology_.set, None, u'Should only be used if morphology element is outside the cell.\n                                          This points to the id of the morphology\n                        ')

    
    # Attribute biophysicalProperties uses Python identifier biophysicalProperties_
    __biophysicalProperties_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'biophysicalProperties'), 'biophysicalProperties_', '__httpwww_neuroml_orgschemaneuroml2_Cell_biophysicalProperties', NmlId, unicode_default=u'1')
    __biophysicalProperties_._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 805, 16)
    __biophysicalProperties_._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 805, 16)
    
    biophysicalProperties_ = property(__biophysicalProperties_.value, __biophysicalProperties_.set, None, u'Should only be used if biophysicalProperties element is outside the cell.\n                                          This points to the id of the biophysicalProperties\n                        ')

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __morphology.name() : __morphology,
        __biophysicalProperties.name() : __biophysicalProperties
    })
    _AttributeMap.update({
        __morphology_.name() : __morphology_,
        __biophysicalProperties_.name() : __biophysicalProperties_
    })
Namespace.addCategoryObject('typeBinding', u'Cell', Cell)


# Complex type {http://www.neuroml.org/schema/neuroml2}ConcentrationModel_D with content type ELEMENT_ONLY
class ConcentrationModel_D (DecayingPoolConcentrationModel):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ConcentrationModel_D with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConcentrationModel_D')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1164, 4)
    _ElementMap = DecayingPoolConcentrationModel._ElementMap.copy()
    _AttributeMap = DecayingPoolConcentrationModel._AttributeMap.copy()
    # Base type is DecayingPoolConcentrationModel
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute ion inherited from {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel
    
    # Attribute restingConc inherited from {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel
    
    # Attribute decayConstant inherited from {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel
    
    # Attribute shellThickness inherited from {http://www.neuroml.org/schema/neuroml2}DecayingPoolConcentrationModel
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_neuroml_orgschemaneuroml2_ConcentrationModel_D_type', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default=u'decayingPoolConcentrationModel', required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1169, 16)
    __type._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1169, 16)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'ConcentrationModel_D', ConcentrationModel_D)


# Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNCell with content type ELEMENT_ONLY
class basePyNNCell (BaseCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'basePyNNCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1620, 4)
    _ElementMap = BaseCell._ElementMap.copy()
    _AttributeMap = BaseCell._AttributeMap.copy()
    # Base type is BaseCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm uses Python identifier cm
    __cm = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cm'), 'cm', '__httpwww_neuroml_orgschemaneuroml2_basePyNNCell_cm', pyxb.binding.datatypes.double)
    __cm._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1624, 16)
    __cm._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1624, 16)
    
    cm = property(__cm.value, __cm.set, None, None)

    
    # Attribute i_offset uses Python identifier i_offset
    __i_offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'i_offset'), 'i_offset', '__httpwww_neuroml_orgschemaneuroml2_basePyNNCell_i_offset', pyxb.binding.datatypes.double)
    __i_offset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1625, 16)
    __i_offset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1625, 16)
    
    i_offset = property(__i_offset.value, __i_offset.set, None, None)

    
    # Attribute tau_syn_E uses Python identifier tau_syn_E
    __tau_syn_E = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_syn_E'), 'tau_syn_E', '__httpwww_neuroml_orgschemaneuroml2_basePyNNCell_tau_syn_E', pyxb.binding.datatypes.double)
    __tau_syn_E._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1626, 16)
    __tau_syn_E._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1626, 16)
    
    tau_syn_E = property(__tau_syn_E.value, __tau_syn_E.set, None, None)

    
    # Attribute tau_syn_I uses Python identifier tau_syn_I
    __tau_syn_I = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_syn_I'), 'tau_syn_I', '__httpwww_neuroml_orgschemaneuroml2_basePyNNCell_tau_syn_I', pyxb.binding.datatypes.double)
    __tau_syn_I._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1627, 16)
    __tau_syn_I._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1627, 16)
    
    tau_syn_I = property(__tau_syn_I.value, __tau_syn_I.set, None, None)

    
    # Attribute v_init uses Python identifier v_init
    __v_init = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_init'), 'v_init', '__httpwww_neuroml_orgschemaneuroml2_basePyNNCell_v_init', pyxb.binding.datatypes.double)
    __v_init._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1628, 16)
    __v_init._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1628, 16)
    
    v_init = property(__v_init.value, __v_init.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __cm.name() : __cm,
        __i_offset.name() : __i_offset,
        __tau_syn_E.name() : __tau_syn_E,
        __tau_syn_I.name() : __tau_syn_I,
        __v_init.name() : __v_init
    })
Namespace.addCategoryObject('typeBinding', u'basePyNNCell', basePyNNCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse with content type ELEMENT_ONLY
class BasePynnSynapse (BaseSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BasePynnSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1742, 4)
    _ElementMap = BaseSynapse._ElementMap.copy()
    _AttributeMap = BaseSynapse._AttributeMap.copy()
    # Base type is BaseSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute tau_syn uses Python identifier tau_syn
    __tau_syn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_syn'), 'tau_syn', '__httpwww_neuroml_orgschemaneuroml2_BasePynnSynapse_tau_syn', pyxb.binding.datatypes.double)
    __tau_syn._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1746, 16)
    __tau_syn._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1746, 16)
    
    tau_syn = property(__tau_syn.value, __tau_syn.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tau_syn.name() : __tau_syn
    })
Namespace.addCategoryObject('typeBinding', u'BasePynnSynapse', BasePynnSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExpOneSynapse with content type ELEMENT_ONLY
class ExpOneSynapse (BaseConductanceBasedSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExpOneSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExpOneSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 622, 4)
    _ElementMap = BaseConductanceBasedSynapse._ElementMap.copy()
    _AttributeMap = BaseConductanceBasedSynapse._AttributeMap.copy()
    # Base type is BaseConductanceBasedSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute gbase inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute erev inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute tauDecay uses Python identifier tauDecay
    __tauDecay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauDecay'), 'tauDecay', '__httpwww_neuroml_orgschemaneuroml2_ExpOneSynapse_tauDecay', Nml2Quantity_time, required=True)
    __tauDecay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 627, 16)
    __tauDecay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 627, 16)
    
    tauDecay = property(__tauDecay.value, __tauDecay.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tauDecay.name() : __tauDecay
    })
Namespace.addCategoryObject('typeBinding', u'ExpOneSynapse', ExpOneSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExpTwoSynapse with content type ELEMENT_ONLY
class ExpTwoSynapse (BaseConductanceBasedSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExpTwoSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExpTwoSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 634, 4)
    _ElementMap = BaseConductanceBasedSynapse._ElementMap.copy()
    _AttributeMap = BaseConductanceBasedSynapse._AttributeMap.copy()
    # Base type is BaseConductanceBasedSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute gbase inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute erev inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute tauDecay uses Python identifier tauDecay
    __tauDecay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauDecay'), 'tauDecay', '__httpwww_neuroml_orgschemaneuroml2_ExpTwoSynapse_tauDecay', Nml2Quantity_time, required=True)
    __tauDecay._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 639, 16)
    __tauDecay._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 639, 16)
    
    tauDecay = property(__tauDecay.value, __tauDecay.set, None, None)

    
    # Attribute tauRise uses Python identifier tauRise
    __tauRise = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tauRise'), 'tauRise', '__httpwww_neuroml_orgschemaneuroml2_ExpTwoSynapse_tauRise', Nml2Quantity_time, required=True)
    __tauRise._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 640, 16)
    __tauRise._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 640, 16)
    
    tauRise = property(__tauRise.value, __tauRise.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tauDecay.name() : __tauDecay,
        __tauRise.name() : __tauRise
    })
Namespace.addCategoryObject('typeBinding', u'ExpTwoSynapse', ExpTwoSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}IaFTauRefCell with content type ELEMENT_ONLY
class IaFTauRefCell (IaFTauCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IaFTauRefCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IaFTauRefCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 720, 4)
    _ElementMap = IaFTauCell._ElementMap.copy()
    _AttributeMap = IaFTauCell._AttributeMap.copy()
    # Base type is IaFTauCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute leakReversal inherited from {http://www.neuroml.org/schema/neuroml2}IaFTauCell
    
    # Attribute thresh inherited from {http://www.neuroml.org/schema/neuroml2}IaFTauCell
    
    # Attribute reset_ inherited from {http://www.neuroml.org/schema/neuroml2}IaFTauCell
    
    # Attribute tau inherited from {http://www.neuroml.org/schema/neuroml2}IaFTauCell
    
    # Attribute refract uses Python identifier refract
    __refract = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'refract'), 'refract', '__httpwww_neuroml_orgschemaneuroml2_IaFTauRefCell_refract', Nml2Quantity_time, required=True)
    __refract._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 723, 3)
    __refract._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 723, 3)
    
    refract = property(__refract.value, __refract.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __refract.name() : __refract
    })
Namespace.addCategoryObject('typeBinding', u'IaFTauRefCell', IaFTauRefCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}IaFRefCell with content type ELEMENT_ONLY
class IaFRefCell (IaFCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IaFRefCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IaFRefCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 740, 4)
    _ElementMap = IaFCell._ElementMap.copy()
    _AttributeMap = IaFCell._AttributeMap.copy()
    # Base type is IaFCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute leakReversal inherited from {http://www.neuroml.org/schema/neuroml2}IaFCell
    
    # Attribute thresh inherited from {http://www.neuroml.org/schema/neuroml2}IaFCell
    
    # Attribute reset_ inherited from {http://www.neuroml.org/schema/neuroml2}IaFCell
    
    # Attribute C inherited from {http://www.neuroml.org/schema/neuroml2}IaFCell
    
    # Attribute leakConductance inherited from {http://www.neuroml.org/schema/neuroml2}IaFCell
    
    # Attribute refract uses Python identifier refract
    __refract = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'refract'), 'refract', '__httpwww_neuroml_orgschemaneuroml2_IaFRefCell_refract', Nml2Quantity_time, required=True)
    __refract._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 743, 3)
    __refract._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 743, 3)
    
    refract = property(__refract.value, __refract.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __refract.name() : __refract
    })
Namespace.addCategoryObject('typeBinding', u'IaFRefCell', IaFRefCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell with content type ELEMENT_ONLY
class basePyNNIaFCell (basePyNNCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'basePyNNIaFCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1634, 4)
    _ElementMap = basePyNNCell._ElementMap.copy()
    _AttributeMap = basePyNNCell._AttributeMap.copy()
    # Base type is basePyNNCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m uses Python identifier tau_m
    __tau_m = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_m'), 'tau_m', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCell_tau_m', pyxb.binding.datatypes.double)
    __tau_m._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1638, 16)
    __tau_m._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1638, 16)
    
    tau_m = property(__tau_m.value, __tau_m.set, None, None)

    
    # Attribute tau_refrac uses Python identifier tau_refrac
    __tau_refrac = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_refrac'), 'tau_refrac', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCell_tau_refrac', pyxb.binding.datatypes.double)
    __tau_refrac._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1639, 16)
    __tau_refrac._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1639, 16)
    
    tau_refrac = property(__tau_refrac.value, __tau_refrac.set, None, None)

    
    # Attribute v_reset uses Python identifier v_reset
    __v_reset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_reset'), 'v_reset', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCell_v_reset', pyxb.binding.datatypes.double)
    __v_reset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1640, 16)
    __v_reset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1640, 16)
    
    v_reset = property(__v_reset.value, __v_reset.set, None, None)

    
    # Attribute v_rest uses Python identifier v_rest
    __v_rest = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_rest'), 'v_rest', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCell_v_rest', pyxb.binding.datatypes.double)
    __v_rest._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1641, 16)
    __v_rest._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1641, 16)
    
    v_rest = property(__v_rest.value, __v_rest.set, None, None)

    
    # Attribute v_thresh uses Python identifier v_thresh
    __v_thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_thresh'), 'v_thresh', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCell_v_thresh', pyxb.binding.datatypes.double)
    __v_thresh._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1642, 16)
    __v_thresh._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1642, 16)
    
    v_thresh = property(__v_thresh.value, __v_thresh.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tau_m.name() : __tau_m,
        __tau_refrac.name() : __tau_refrac,
        __v_reset.name() : __v_reset,
        __v_rest.name() : __v_rest,
        __v_thresh.name() : __v_thresh
    })
Namespace.addCategoryObject('typeBinding', u'basePyNNIaFCell', basePyNNIaFCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}HH_cond_exp with content type ELEMENT_ONLY
class HH_cond_exp (basePyNNCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}HH_cond_exp with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HH_cond_exp')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1724, 4)
    _ElementMap = basePyNNCell._ElementMap.copy()
    _AttributeMap = basePyNNCell._AttributeMap.copy()
    # Base type is basePyNNCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_offset uses Python identifier v_offset
    __v_offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_offset'), 'v_offset', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_v_offset', pyxb.binding.datatypes.double)
    __v_offset._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1728, 16)
    __v_offset._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1728, 16)
    
    v_offset = property(__v_offset.value, __v_offset.set, None, None)

    
    # Attribute e_rev_E uses Python identifier e_rev_E
    __e_rev_E = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_E'), 'e_rev_E', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_e_rev_E', pyxb.binding.datatypes.double)
    __e_rev_E._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1729, 16)
    __e_rev_E._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1729, 16)
    
    e_rev_E = property(__e_rev_E.value, __e_rev_E.set, None, None)

    
    # Attribute e_rev_I uses Python identifier e_rev_I
    __e_rev_I = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_I'), 'e_rev_I', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_e_rev_I', pyxb.binding.datatypes.double)
    __e_rev_I._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1730, 16)
    __e_rev_I._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1730, 16)
    
    e_rev_I = property(__e_rev_I.value, __e_rev_I.set, None, None)

    
    # Attribute e_rev_K uses Python identifier e_rev_K
    __e_rev_K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_K'), 'e_rev_K', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_e_rev_K', pyxb.binding.datatypes.double)
    __e_rev_K._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1731, 16)
    __e_rev_K._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1731, 16)
    
    e_rev_K = property(__e_rev_K.value, __e_rev_K.set, None, None)

    
    # Attribute e_rev_Na uses Python identifier e_rev_Na
    __e_rev_Na = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_Na'), 'e_rev_Na', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_e_rev_Na', pyxb.binding.datatypes.double)
    __e_rev_Na._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1732, 16)
    __e_rev_Na._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1732, 16)
    
    e_rev_Na = property(__e_rev_Na.value, __e_rev_Na.set, None, None)

    
    # Attribute e_rev_leak uses Python identifier e_rev_leak
    __e_rev_leak = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_leak'), 'e_rev_leak', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_e_rev_leak', pyxb.binding.datatypes.double)
    __e_rev_leak._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1733, 16)
    __e_rev_leak._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1733, 16)
    
    e_rev_leak = property(__e_rev_leak.value, __e_rev_leak.set, None, None)

    
    # Attribute g_leak uses Python identifier g_leak
    __g_leak = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'g_leak'), 'g_leak', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_g_leak', pyxb.binding.datatypes.double)
    __g_leak._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1734, 16)
    __g_leak._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1734, 16)
    
    g_leak = property(__g_leak.value, __g_leak.set, None, None)

    
    # Attribute gbar_K uses Python identifier gbar_K
    __gbar_K = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gbar_K'), 'gbar_K', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_gbar_K', pyxb.binding.datatypes.double)
    __gbar_K._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1735, 16)
    __gbar_K._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1735, 16)
    
    gbar_K = property(__gbar_K.value, __gbar_K.set, None, None)

    
    # Attribute gbar_Na uses Python identifier gbar_Na
    __gbar_Na = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gbar_Na'), 'gbar_Na', '__httpwww_neuroml_orgschemaneuroml2_HH_cond_exp_gbar_Na', pyxb.binding.datatypes.double)
    __gbar_Na._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1736, 16)
    __gbar_Na._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1736, 16)
    
    gbar_Na = property(__gbar_Na.value, __gbar_Na.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __v_offset.name() : __v_offset,
        __e_rev_E.name() : __e_rev_E,
        __e_rev_I.name() : __e_rev_I,
        __e_rev_K.name() : __e_rev_K,
        __e_rev_Na.name() : __e_rev_Na,
        __e_rev_leak.name() : __e_rev_leak,
        __g_leak.name() : __g_leak,
        __gbar_K.name() : __gbar_K,
        __gbar_Na.name() : __gbar_Na
    })
Namespace.addCategoryObject('typeBinding', u'HH_cond_exp', HH_cond_exp)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExpCondSynapse with content type ELEMENT_ONLY
class ExpCondSynapse (BasePynnSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExpCondSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExpCondSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1752, 4)
    _ElementMap = BasePynnSynapse._ElementMap.copy()
    _AttributeMap = BasePynnSynapse._AttributeMap.copy()
    # Base type is BasePynnSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute tau_syn inherited from {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse
    
    # Attribute e_rev uses Python identifier e_rev
    __e_rev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev'), 'e_rev', '__httpwww_neuroml_orgschemaneuroml2_ExpCondSynapse_e_rev', pyxb.binding.datatypes.double)
    __e_rev._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1756, 16)
    __e_rev._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1756, 16)
    
    e_rev = property(__e_rev.value, __e_rev.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __e_rev.name() : __e_rev
    })
Namespace.addCategoryObject('typeBinding', u'ExpCondSynapse', ExpCondSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}AlphaCondSynapse with content type ELEMENT_ONLY
class AlphaCondSynapse (BasePynnSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}AlphaCondSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AlphaCondSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1762, 4)
    _ElementMap = BasePynnSynapse._ElementMap.copy()
    _AttributeMap = BasePynnSynapse._AttributeMap.copy()
    # Base type is BasePynnSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute tau_syn inherited from {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse
    
    # Attribute e_rev uses Python identifier e_rev
    __e_rev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev'), 'e_rev', '__httpwww_neuroml_orgschemaneuroml2_AlphaCondSynapse_e_rev', pyxb.binding.datatypes.double)
    __e_rev._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1766, 16)
    __e_rev._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1766, 16)
    
    e_rev = property(__e_rev.value, __e_rev.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __e_rev.name() : __e_rev
    })
Namespace.addCategoryObject('typeBinding', u'AlphaCondSynapse', AlphaCondSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}ExpCurrSynapse with content type ELEMENT_ONLY
class ExpCurrSynapse (BasePynnSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}ExpCurrSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExpCurrSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1772, 4)
    _ElementMap = BasePynnSynapse._ElementMap.copy()
    _AttributeMap = BasePynnSynapse._AttributeMap.copy()
    # Base type is BasePynnSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute tau_syn inherited from {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ExpCurrSynapse', ExpCurrSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}AlphaCurrSynapse with content type ELEMENT_ONLY
class AlphaCurrSynapse (BasePynnSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}AlphaCurrSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AlphaCurrSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1782, 4)
    _ElementMap = BasePynnSynapse._ElementMap.copy()
    _AttributeMap = BasePynnSynapse._AttributeMap.copy()
    # Base type is BasePynnSynapse
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute tau_syn inherited from {http://www.neuroml.org/schema/neuroml2}BasePynnSynapse
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AlphaCurrSynapse', AlphaCurrSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}BlockingPlasticSynapse with content type ELEMENT_ONLY
class BlockingPlasticSynapse (ExpTwoSynapse):
    """Complex type {http://www.neuroml.org/schema/neuroml2}BlockingPlasticSynapse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BlockingPlasticSynapse')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 647, 4)
    _ElementMap = ExpTwoSynapse._ElementMap.copy()
    _AttributeMap = ExpTwoSynapse._AttributeMap.copy()
    # Base type is ExpTwoSynapse
    
    # Element {http://www.neuroml.org/schema/neuroml2}plasticityMechanism uses Python identifier plasticityMechanism
    __plasticityMechanism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'plasticityMechanism'), 'plasticityMechanism', '__httpwww_neuroml_orgschemaneuroml2_BlockingPlasticSynapse_httpwww_neuroml_orgschemaneuroml2plasticityMechanism', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 651, 16), )

    
    plasticityMechanism = property(__plasticityMechanism.value, __plasticityMechanism.set, None, None)

    
    # Element {http://www.neuroml.org/schema/neuroml2}blockMechanism uses Python identifier blockMechanism
    __blockMechanism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'blockMechanism'), 'blockMechanism', '__httpwww_neuroml_orgschemaneuroml2_BlockingPlasticSynapse_httpwww_neuroml_orgschemaneuroml2blockMechanism', False, pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 654, 2), )

    
    blockMechanism = property(__blockMechanism.value, __blockMechanism.set, None, None)

    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute gbase inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute erev inherited from {http://www.neuroml.org/schema/neuroml2}BaseConductanceBasedSynapse
    
    # Attribute tauDecay inherited from {http://www.neuroml.org/schema/neuroml2}ExpTwoSynapse
    
    # Attribute tauRise inherited from {http://www.neuroml.org/schema/neuroml2}ExpTwoSynapse
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        __plasticityMechanism.name() : __plasticityMechanism,
        __blockMechanism.name() : __blockMechanism
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BlockingPlasticSynapse', BlockingPlasticSynapse)


# Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell with content type ELEMENT_ONLY
class basePyNNIaFCondCell (basePyNNIaFCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'basePyNNIaFCondCell')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1648, 4)
    _ElementMap = basePyNNIaFCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCell._AttributeMap.copy()
    # Base type is basePyNNIaFCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute e_rev_E uses Python identifier e_rev_E
    __e_rev_E = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_E'), 'e_rev_E', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCondCell_e_rev_E', pyxb.binding.datatypes.double)
    __e_rev_E._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1652, 16)
    __e_rev_E._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1652, 16)
    
    e_rev_E = property(__e_rev_E.value, __e_rev_E.set, None, None)

    
    # Attribute e_rev_I uses Python identifier e_rev_I
    __e_rev_I = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'e_rev_I'), 'e_rev_I', '__httpwww_neuroml_orgschemaneuroml2_basePyNNIaFCondCell_e_rev_I', pyxb.binding.datatypes.double)
    __e_rev_I._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1653, 16)
    __e_rev_I._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1653, 16)
    
    e_rev_I = property(__e_rev_I.value, __e_rev_I.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __e_rev_E.name() : __e_rev_E,
        __e_rev_I.name() : __e_rev_I
    })
Namespace.addCategoryObject('typeBinding', u'basePyNNIaFCondCell', basePyNNIaFCondCell)


# Complex type {http://www.neuroml.org/schema/neuroml2}IF_curr_alpha with content type ELEMENT_ONLY
class IF_curr_alpha (basePyNNIaFCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IF_curr_alpha with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IF_curr_alpha')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1661, 4)
    _ElementMap = basePyNNIaFCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCell._AttributeMap.copy()
    # Base type is basePyNNIaFCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IF_curr_alpha', IF_curr_alpha)


# Complex type {http://www.neuroml.org/schema/neuroml2}IF_curr_exp with content type ELEMENT_ONLY
class IF_curr_exp (basePyNNIaFCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IF_curr_exp with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IF_curr_exp')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1670, 4)
    _ElementMap = basePyNNIaFCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCell._AttributeMap.copy()
    # Base type is basePyNNIaFCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IF_curr_exp', IF_curr_exp)


# Complex type {http://www.neuroml.org/schema/neuroml2}IF_cond_alpha with content type ELEMENT_ONLY
class IF_cond_alpha (basePyNNIaFCondCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IF_cond_alpha with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IF_cond_alpha')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1679, 4)
    _ElementMap = basePyNNIaFCondCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCondCell._AttributeMap.copy()
    # Base type is basePyNNIaFCondCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute e_rev_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute e_rev_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IF_cond_alpha', IF_cond_alpha)


# Complex type {http://www.neuroml.org/schema/neuroml2}IF_cond_exp with content type ELEMENT_ONLY
class IF_cond_exp (basePyNNIaFCondCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}IF_cond_exp with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IF_cond_exp')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1688, 4)
    _ElementMap = basePyNNIaFCondCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCondCell._AttributeMap.copy()
    # Base type is basePyNNIaFCondCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute e_rev_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute e_rev_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IF_cond_exp', IF_cond_exp)


# Complex type {http://www.neuroml.org/schema/neuroml2}EIF_cond_exp_isfa_ista with content type ELEMENT_ONLY
class EIF_cond_exp_isfa_ista (basePyNNIaFCondCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}EIF_cond_exp_isfa_ista with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_exp_isfa_ista')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1697, 4)
    _ElementMap = basePyNNIaFCondCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCondCell._AttributeMap.copy()
    # Base type is basePyNNIaFCondCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute e_rev_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute e_rev_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute a uses Python identifier a
    __a = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'a'), 'a', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_exp_isfa_ista_a', pyxb.binding.datatypes.double)
    __a._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1701, 16)
    __a._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1701, 16)
    
    a = property(__a.value, __a.set, None, None)

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_exp_isfa_ista_b', pyxb.binding.datatypes.double)
    __b._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1702, 16)
    __b._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1702, 16)
    
    b = property(__b.value, __b.set, None, None)

    
    # Attribute delta_T uses Python identifier delta_T
    __delta_T = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delta_T'), 'delta_T', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_exp_isfa_ista_delta_T', pyxb.binding.datatypes.double)
    __delta_T._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1703, 16)
    __delta_T._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1703, 16)
    
    delta_T = property(__delta_T.value, __delta_T.set, None, None)

    
    # Attribute tau_w uses Python identifier tau_w
    __tau_w = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_w'), 'tau_w', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_exp_isfa_ista_tau_w', pyxb.binding.datatypes.double)
    __tau_w._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1704, 16)
    __tau_w._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1704, 16)
    
    tau_w = property(__tau_w.value, __tau_w.set, None, None)

    
    # Attribute v_spike uses Python identifier v_spike
    __v_spike = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_spike'), 'v_spike', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_exp_isfa_ista_v_spike', pyxb.binding.datatypes.double)
    __v_spike._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1705, 16)
    __v_spike._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1705, 16)
    
    v_spike = property(__v_spike.value, __v_spike.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __a.name() : __a,
        __b.name() : __b,
        __delta_T.name() : __delta_T,
        __tau_w.name() : __tau_w,
        __v_spike.name() : __v_spike
    })
Namespace.addCategoryObject('typeBinding', u'EIF_cond_exp_isfa_ista', EIF_cond_exp_isfa_ista)


# Complex type {http://www.neuroml.org/schema/neuroml2}EIF_cond_alpha_isfa_ista with content type ELEMENT_ONLY
class EIF_cond_alpha_isfa_ista (basePyNNIaFCondCell):
    """Complex type {http://www.neuroml.org/schema/neuroml2}EIF_cond_alpha_isfa_ista with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_alpha_isfa_ista')
    _XSDLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1710, 4)
    _ElementMap = basePyNNIaFCondCell._ElementMap.copy()
    _AttributeMap = basePyNNIaFCondCell._AttributeMap.copy()
    # Base type is basePyNNIaFCondCell
    
    # Element notes ({http://www.neuroml.org/schema/neuroml2}notes) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Element annotation ({http://www.neuroml.org/schema/neuroml2}annotation) inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    
    # Attribute cm inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute i_offset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_syn_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute v_init inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNCell
    
    # Attribute tau_m inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute tau_refrac inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_reset inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_rest inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute v_thresh inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCell
    
    # Attribute e_rev_E inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute e_rev_I inherited from {http://www.neuroml.org/schema/neuroml2}basePyNNIaFCondCell
    
    # Attribute a uses Python identifier a
    __a = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'a'), 'a', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_alpha_isfa_ista_a', pyxb.binding.datatypes.double)
    __a._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1714, 16)
    __a._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1714, 16)
    
    a = property(__a.value, __a.set, None, None)

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_alpha_isfa_ista_b', pyxb.binding.datatypes.double)
    __b._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1715, 16)
    __b._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1715, 16)
    
    b = property(__b.value, __b.set, None, None)

    
    # Attribute delta_T uses Python identifier delta_T
    __delta_T = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delta_T'), 'delta_T', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_alpha_isfa_ista_delta_T', pyxb.binding.datatypes.double)
    __delta_T._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1716, 16)
    __delta_T._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1716, 16)
    
    delta_T = property(__delta_T.value, __delta_T.set, None, None)

    
    # Attribute tau_w uses Python identifier tau_w
    __tau_w = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_w'), 'tau_w', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_alpha_isfa_ista_tau_w', pyxb.binding.datatypes.double)
    __tau_w._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1717, 16)
    __tau_w._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1717, 16)
    
    tau_w = property(__tau_w.value, __tau_w.set, None, None)

    
    # Attribute v_spike uses Python identifier v_spike
    __v_spike = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_spike'), 'v_spike', '__httpwww_neuroml_orgschemaneuroml2_EIF_cond_alpha_isfa_ista_v_spike', pyxb.binding.datatypes.double)
    __v_spike._DeclarationLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1718, 16)
    __v_spike._UseLocation = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1718, 16)
    
    v_spike = property(__v_spike.value, __v_spike.set, None, None)

    
    # Attribute neuroLexId inherited from {http://www.neuroml.org/schema/neuroml2}BaseWithoutId
    
    # Attribute id inherited from {http://www.neuroml.org/schema/neuroml2}Base
    
    # Attribute metaid inherited from {http://www.neuroml.org/schema/neuroml2}Standalone
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __a.name() : __a,
        __b.name() : __b,
        __delta_T.name() : __delta_T,
        __tau_w.name() : __tau_w,
        __v_spike.name() : __v_spike
    })
Namespace.addCategoryObject('typeBinding', u'EIF_cond_alpha_isfa_ista', EIF_cond_alpha_isfa_ista)


neuroml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'neuroml'), NeuroMLDocument, documentation=u'The root NeuroML element.', location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 241, 4))
Namespace.addCategoryObject('elementBinding', neuroml.name().localName(), neuroml)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 206, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 206, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Annotation._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 215, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 215, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ComponentType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
IncludeType._Automaton = _BuildAutomaton_2()




Path._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), SegmentEndPoint, scope=Path, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 936, 12)))

Path._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'to'), SegmentEndPoint, scope=Path, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 937, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 936, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 937, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Path._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 936, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Path._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'to')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 937, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Path._Automaton = _BuildAutomaton_3()




SubTree._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), SegmentEndPoint, scope=SubTree, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 943, 12)))

SubTree._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'to'), SegmentEndPoint, scope=SubTree, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 944, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 943, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 944, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubTree._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 943, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubTree._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'to')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 944, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubTree._Automaton = _BuildAutomaton_4()




MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'channelPopulation'), ChannelPopulation, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 983, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'channelDensity'), ChannelDensity, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 984, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'channelDensityNernst'), ChannelDensityNernst, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 985, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spikeThresh'), ValueAcrossSegOrSegGroup, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 987, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'specificCapacitance'), ValueAcrossSegOrSegGroup, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 988, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'initMembPotential'), ValueAcrossSegOrSegGroup, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 990, 12)))

MembraneProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reversalPotential'), ReversalPotential, scope=MembraneProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 992, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 982, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 983, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 984, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 985, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 987, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 988, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 990, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 992, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'channelPopulation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 983, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'channelDensity')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 984, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'channelDensityNernst')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 985, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spikeThresh')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 987, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'specificCapacitance')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 988, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'initMembPotential')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 990, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MembraneProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reversalPotential')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 992, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MembraneProperties._Automaton = _BuildAutomaton_5()




VariableParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousValue'), InhomogeneousValue, scope=VariableParameter, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1106, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1106, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VariableParameter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousValue')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1106, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VariableParameter._Automaton = _BuildAutomaton_6()




IntracellularProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'species'), Species, scope=IntracellularProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1178, 12)))

IntracellularProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resistivity'), ValueAcrossSegOrSegGroup, scope=IntracellularProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1179, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1178, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1179, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IntracellularProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'species')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1178, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IntracellularProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resistivity')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1179, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IntracellularProperties._Automaton = _BuildAutomaton_7()




ExtracellularPropertiesLocal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'species'), Species, scope=ExtracellularPropertiesLocal, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1201, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1201, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExtracellularPropertiesLocal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'species')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1201, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExtracellularPropertiesLocal._Automaton = _BuildAutomaton_8()




Instance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'location'), Location, scope=Instance, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1508, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Instance._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'location')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1508, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Instance._Automaton = _BuildAutomaton_9()




Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'random'), RandomLayout, scope=Layout, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1477, 12)))

Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grid'), GridLayout, scope=Layout, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1478, 12)))

Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unstructured'), UnstructuredLayout, scope=Layout, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1479, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'random')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1477, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grid')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1478, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unstructured')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1479, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Layout._Automaton = _BuildAutomaton_10()




Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'parent'), SegmentParent, scope=Segment, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 844, 20)))

Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'proximal'), Point3DWithDiam, scope=Segment, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 845, 20)))

Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'distal'), Point3DWithDiam, scope=Segment, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 846, 20)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 844, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 845, 20))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Segment._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'parent')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 844, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Segment._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'proximal')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 845, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Segment._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'distal')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 846, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Segment._Automaton = _BuildAutomaton_11()




GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 460, 20)))

GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), Q10Settings, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 461, 20)))

GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), HHRate, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 462, 20)))

GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), HHRate, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 463, 20)))

GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), HHTime, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 464, 20)))

GateHHUndetermined._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), HHVariable, scope=GateHHUndetermined, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 465, 20)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 460, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 460, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 461, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'q10Settings')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 461, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 462, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'forwardRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 462, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 463, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reverseRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 463, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 464, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'timeCourse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 464, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 465, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHUndetermined._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'steadyState')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 465, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 460, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 461, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 462, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 463, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 464, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 465, 20))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    final_update = set()
    symbol = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 459, 16)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GateHHUndetermined._Automaton = _BuildAutomaton_12()




GateHHRates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=GateHHRates, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 477, 20)))

GateHHRates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), Q10Settings, scope=GateHHRates, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 478, 20)))

GateHHRates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), HHRate, scope=GateHHRates, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 479, 20)))

GateHHRates._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), HHRate, scope=GateHHRates, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 480, 20)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 477, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRates._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 477, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 478, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRates._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'q10Settings')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 478, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRates._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'forwardRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 479, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRates._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reverseRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 480, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 477, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 478, 20))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    final_update = set()
    symbol = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 476, 16)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GateHHRates._Automaton = _BuildAutomaton_19()




GateHHTauInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=GateHHTauInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 493, 20)))

GateHHTauInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), Q10Settings, scope=GateHHTauInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 494, 20)))

GateHHTauInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), HHTime, scope=GateHHTauInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 495, 20)))

GateHHTauInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), HHVariable, scope=GateHHTauInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 496, 20)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 493, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHTauInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 493, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 494, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHTauInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'q10Settings')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 494, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHTauInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'timeCourse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 495, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHTauInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'steadyState')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 496, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 493, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 494, 20))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    sub_automata.append(_BuildAutomaton_27())
    sub_automata.append(_BuildAutomaton_28())
    final_update = set()
    symbol = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 492, 16)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GateHHTauInf._Automaton = _BuildAutomaton_24()




GateHHRatesTau._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=GateHHRatesTau, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 508, 20)))

GateHHRatesTau._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), Q10Settings, scope=GateHHRatesTau, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 509, 20)))

GateHHRatesTau._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), HHRate, scope=GateHHRatesTau, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 510, 20)))

GateHHRatesTau._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), HHRate, scope=GateHHRatesTau, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 511, 20)))

GateHHRatesTau._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'timeCourse'), HHTime, scope=GateHHRatesTau, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 512, 20)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 508, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRatesTau._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 508, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 509, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRatesTau._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'q10Settings')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 509, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesTau._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'forwardRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 510, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesTau._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reverseRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 511, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesTau._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'timeCourse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 512, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 508, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 509, 20))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_30())
    sub_automata.append(_BuildAutomaton_31())
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    final_update = set()
    symbol = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 507, 16)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GateHHRatesTau._Automaton = _BuildAutomaton_29()




GateHHRatesInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=GateHHRatesInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 524, 20)))

GateHHRatesInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'q10Settings'), Q10Settings, scope=GateHHRatesInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 525, 20)))

GateHHRatesInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forwardRate'), HHRate, scope=GateHHRatesInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 526, 20)))

GateHHRatesInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reverseRate'), HHRate, scope=GateHHRatesInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 527, 20)))

GateHHRatesInf._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'steadyState'), HHVariable, scope=GateHHRatesInf, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 528, 20)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 524, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRatesInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 524, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 525, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GateHHRatesInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'q10Settings')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 525, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'forwardRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 526, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reverseRate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 527, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GateHHRatesInf._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'steadyState')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 528, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 524, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 525, 20))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_36())
    sub_automata.append(_BuildAutomaton_37())
    sub_automata.append(_BuildAutomaton_38())
    sub_automata.append(_BuildAutomaton_39())
    sub_automata.append(_BuildAutomaton_40())
    final_update = set()
    symbol = pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 523, 16)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GateHHRatesInf._Automaton = _BuildAutomaton_35()




SegmentGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'member'), Member, scope=SegmentGroup, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 882, 20)))

SegmentGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), Include, scope=SegmentGroup, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 883, 20)))

SegmentGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'path'), Path, scope=SegmentGroup, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 884, 20)))

SegmentGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subTree'), SubTree, scope=SegmentGroup, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 885, 20)))

SegmentGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousParam'), InhomogeneousParam, scope=SegmentGroup, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 886, 20)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 882, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 883, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 884, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 885, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 886, 20))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SegmentGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'member')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 882, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SegmentGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 883, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SegmentGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'path')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 884, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SegmentGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subTree')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 885, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SegmentGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inhomogeneousParam')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 886, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SegmentGroup._Automaton = _BuildAutomaton_41()




InhomogeneousParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'proximal'), ProximalDetails, scope=InhomogeneousParam, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 898, 20)))

InhomogeneousParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'distal'), DistalDetails, scope=InhomogeneousParam, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 899, 20)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 898, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 899, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InhomogeneousParam._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'proximal')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 898, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InhomogeneousParam._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'distal')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 899, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InhomogeneousParam._Automaton = _BuildAutomaton_42()




ChannelPopulation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'variableParameter'), VariableParameter, scope=ChannelPopulation, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1003, 20)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1003, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChannelPopulation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'variableParameter')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1003, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ChannelPopulation._Automaton = _BuildAutomaton_43()




ChannelDensity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'variableParameter'), VariableParameter, scope=ChannelDensity, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1036, 20)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1036, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ChannelDensity._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'variableParameter')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1036, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ChannelDensity._Automaton = _BuildAutomaton_44()




ExtracellularProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'species'), Species, scope=ExtracellularProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1189, 20)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1189, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExtracellularProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'species')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1189, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExtracellularProperties._Automaton = _BuildAutomaton_45()




def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1211, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1211, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReactionScheme._Automaton = _BuildAutomaton_46()




Space._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'structure'), SpaceStructure, scope=Space, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1395, 20)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1395, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Space._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'structure')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1395, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Space._Automaton = _BuildAutomaton_47()




def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1430, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1430, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Region._Automaton = _BuildAutomaton_48()




def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1528, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1528, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CellSet._Automaton = _BuildAutomaton_49()




Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connection'), Connection, scope=Projection, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1555, 20)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1555, 20))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Projection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'connection')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1555, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Projection._Automaton = _BuildAutomaton_50()




InputList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'input'), Input, scope=InputList, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1597, 20)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InputList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'input')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1597, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InputList._Automaton = _BuildAutomaton_51()




Standalone._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), Notes, scope=Standalone, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20)))

Standalone._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'annotation'), Annotation, scope=Standalone, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Standalone._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Standalone._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Standalone._Automaton = _BuildAutomaton_52()




NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'include'), IncludeType, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 255, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), ExtracellularProperties, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 257, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties'), IntracellularProperties, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 258, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'morphology'), Morphology, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 260, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ionChannel'), IonChannel, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 262, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties'), BiophysicalProperties, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 269, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'network'), Network, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 281, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ComponentType'), ComponentType, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 283, 20)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cell'), Cell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 304, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'baseCell'), BaseCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 305, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iafTauCell'), IaFTauCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 306, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iafTauRefCell'), IaFTauRefCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 308, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iafCell'), IaFCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 310, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'iafRefCell'), IaFRefCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 312, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'izhikevichCell'), IzhikevichCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 314, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'adExIaFCell'), AdExIaFCell, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 315, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_alpha'), IF_curr_alpha, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 325, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_exp'), IF_curr_exp, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 326, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_alpha'), IF_cond_alpha, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 327, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_exp'), IF_cond_exp, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 328, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_exp_isfa_ista'), EIF_cond_exp_isfa_ista, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 329, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_alpha_isfa_ista'), EIF_cond_alpha_isfa_ista, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 330, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HH_cond_exp'), HH_cond_exp, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 331, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expOneSynapse'), ExpOneSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 343, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expTwoSynapse'), ExpTwoSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 344, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blockingPlasticSynapse'), BlockingPlasticSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 345, 5)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expCondSynapse'), ExpCondSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 355, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alphaCondSynapse'), AlphaCondSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 356, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expCurrSynapse'), ExpCurrSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 357, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alphaCurrSynapse'), AlphaCurrSynapse, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 358, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pulseGenerator'), PulseGenerator, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 370, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sineGenerator'), SineGenerator, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 372, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rampGenerator'), RampGenerator, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 374, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'voltageClamp'), VoltageClamp, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 376, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spikeArray'), SpikeArray, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 378, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spikeGenerator'), SpikeGenerator, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 380, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorRandom'), SpikeGeneratorRandom, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 382, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorPoisson'), SpikeGeneratorPoisson, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 384, 1)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpikeSourcePoisson'), SpikeSourcePoisson, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 394, 12)))

NeuroMLDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'decayingPoolConcentrationModel'), DecayingPoolConcentrationModel, scope=NeuroMLDocument, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 405, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 255, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 257, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 258, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 260, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 262, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 405, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 343, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 344, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 345, 5))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 269, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 304, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 305, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 306, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 308, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 310, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 312, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 314, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 315, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 370, 1))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 372, 1))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 374, 1))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 376, 1))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 378, 1))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 380, 1))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 382, 1))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 384, 1))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 325, 12))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 326, 12))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 327, 12))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 328, 12))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 329, 12))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 330, 12))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 331, 12))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 355, 12))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 356, 12))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 357, 12))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 358, 12))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 394, 12))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 281, 20))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 283, 20))
    counters.add(cc_41)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'include')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 255, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 257, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 258, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'morphology')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 260, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ionChannel')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 262, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'decayingPoolConcentrationModel')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 405, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expOneSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 343, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expTwoSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 344, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blockingPlasticSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 345, 5))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 269, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 304, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'baseCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 305, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iafTauCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 306, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iafTauRefCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 308, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iafCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 310, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'iafRefCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 312, 12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'izhikevichCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 314, 12))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'adExIaFCell')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 315, 12))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pulseGenerator')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 370, 1))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sineGenerator')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 372, 1))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rampGenerator')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 374, 1))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'voltageClamp')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 376, 1))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spikeArray')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 378, 1))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spikeGenerator')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 380, 1))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorRandom')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 382, 1))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spikeGeneratorPoisson')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 384, 1))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_alpha')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 325, 12))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IF_curr_exp')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 326, 12))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_alpha')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 327, 12))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IF_cond_exp')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 328, 12))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_exp_isfa_ista')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 329, 12))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EIF_cond_alpha_isfa_ista')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 330, 12))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HH_cond_exp')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 331, 12))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expCondSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 355, 12))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alphaCondSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 356, 12))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expCurrSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 357, 12))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alphaCurrSynapse')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 358, 12))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SpikeSourcePoisson')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 394, 12))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'network')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 281, 20))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(NeuroMLDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ComponentType')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 283, 20))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    st_41._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NeuroMLDocument._Automaton = _BuildAutomaton_53()




IonChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gate'), GateHHUndetermined, scope=IonChannel, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 418, 20)))

IonChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gateHHrates'), GateHHRates, scope=IonChannel, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 419, 20)))

IonChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesTau'), GateHHRatesTau, scope=IonChannel, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 420, 20)))

IonChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gateHHtauInf'), GateHHTauInf, scope=IonChannel, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 421, 20)))

IonChannel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesInf'), GateHHRatesInf, scope=IonChannel, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 422, 20)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 418, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 419, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 420, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 421, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 422, 20))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gate')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 418, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gateHHrates')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 419, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesTau')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 420, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gateHHtauInf')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 421, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IonChannel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gateHHratesInf')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 422, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IonChannel._Automaton = _BuildAutomaton_54()




def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DecayingPoolConcentrationModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DecayingPoolConcentrationModel._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DecayingPoolConcentrationModel._Automaton = _BuildAutomaton_55()




def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BaseSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BaseSynapse._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BaseCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BaseCell._Automaton = _BuildAutomaton_57()




Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'segment'), Segment, scope=Morphology, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 831, 20)))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'segmentGroup'), SegmentGroup, scope=Morphology, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 832, 20)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 832, 20))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Morphology._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Morphology._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Morphology._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'segment')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 831, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Morphology._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'segmentGroup')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 832, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Morphology._Automaton = _BuildAutomaton_58()




BiophysicalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'membraneProperties'), MembraneProperties, scope=BiophysicalProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 968, 20)))

BiophysicalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties'), IntracellularProperties, scope=BiophysicalProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 969, 20)))

BiophysicalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), ExtracellularProperties, scope=BiophysicalProperties, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 970, 20)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 969, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 970, 20))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BiophysicalProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BiophysicalProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BiophysicalProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'membraneProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 968, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BiophysicalProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'intracellularProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 969, 20))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BiophysicalProperties._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 970, 20))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BiophysicalProperties._Automaton = _BuildAutomaton_59()




def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PulseGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PulseGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PulseGenerator._Automaton = _BuildAutomaton_60()




def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SineGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SineGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SineGenerator._Automaton = _BuildAutomaton_61()




def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RampGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RampGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RampGenerator._Automaton = _BuildAutomaton_62()




def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(VoltageClamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(VoltageClamp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
VoltageClamp._Automaton = _BuildAutomaton_63()




def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Spike._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Spike._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Spike._Automaton = _BuildAutomaton_64()




SpikeArray._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spike'), Spike, scope=SpikeArray, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1311, 12)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1311, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpikeArray._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpikeArray._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SpikeArray._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spike')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1311, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpikeArray._Automaton = _BuildAutomaton_65()




def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpikeGenerator._Automaton = _BuildAutomaton_66()




def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGeneratorRandom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGeneratorRandom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpikeGeneratorRandom._Automaton = _BuildAutomaton_67()




def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGeneratorPoisson._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpikeGeneratorPoisson._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpikeGeneratorPoisson._Automaton = _BuildAutomaton_68()




Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'space'), Space, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1359, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'region'), Region, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1360, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties'), ExtracellularPropertiesLocal, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1361, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'population'), Population, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1362, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cellSet'), CellSet, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1363, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synapticConnection'), SynapticConnection, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1365, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'projection'), Projection, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1366, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'explicitInput'), ExplicitInput, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1368, 20)))

Network._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inputList'), InputList, scope=Network, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1369, 20)))

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1359, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1360, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1361, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1363, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1365, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1366, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1368, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1369, 20))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'space')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1359, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'region')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1360, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extracellularProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1361, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'population')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1362, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cellSet')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1363, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synapticConnection')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1365, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'projection')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1366, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'explicitInput')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1368, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Network._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'inputList')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1369, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Network._Automaton = _BuildAutomaton_69()




Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), Layout, scope=Population, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1445, 20)))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'instance'), Instance, scope=Population, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1446, 20)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1445, 20))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Population._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Population._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Population._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1445, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Population._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'instance')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1446, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Population._Automaton = _BuildAutomaton_70()




def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpikeSourcePoisson._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SpikeSourcePoisson._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpikeSourcePoisson._Automaton = _BuildAutomaton_71()




def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BaseConductanceBasedSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BaseConductanceBasedSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BaseConductanceBasedSynapse._Automaton = _BuildAutomaton_72()




def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IaFTauCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IaFTauCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IaFTauCell._Automaton = _BuildAutomaton_73()




def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IaFCell._Automaton = _BuildAutomaton_74()




def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IzhikevichCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IzhikevichCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IzhikevichCell._Automaton = _BuildAutomaton_75()




def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdExIaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AdExIaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdExIaFCell._Automaton = _BuildAutomaton_76()




Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'morphology'), Morphology, scope=Cell, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 792, 20)))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties'), BiophysicalProperties, scope=Cell, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 793, 20)))

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 792, 20))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 793, 20))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Cell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Cell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Cell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'morphology')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 792, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Cell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biophysicalProperties')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 793, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Cell._Automaton = _BuildAutomaton_77()




def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConcentrationModel_D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ConcentrationModel_D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConcentrationModel_D._Automaton = _BuildAutomaton_78()




def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
basePyNNCell._Automaton = _BuildAutomaton_79()




def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BasePynnSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BasePynnSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BasePynnSynapse._Automaton = _BuildAutomaton_80()




def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpOneSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExpOneSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExpOneSynapse._Automaton = _BuildAutomaton_81()




def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpTwoSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExpTwoSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExpTwoSynapse._Automaton = _BuildAutomaton_82()




def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IaFTauRefCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IaFTauRefCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IaFTauRefCell._Automaton = _BuildAutomaton_83()




def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IaFRefCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IaFRefCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IaFRefCell._Automaton = _BuildAutomaton_84()




def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNIaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNIaFCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
basePyNNIaFCell._Automaton = _BuildAutomaton_85()




def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HH_cond_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(HH_cond_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
HH_cond_exp._Automaton = _BuildAutomaton_86()




def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpCondSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExpCondSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExpCondSynapse._Automaton = _BuildAutomaton_87()




def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlphaCondSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlphaCondSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlphaCondSynapse._Automaton = _BuildAutomaton_88()




def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExpCurrSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExpCurrSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ExpCurrSynapse._Automaton = _BuildAutomaton_89()




def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AlphaCurrSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AlphaCurrSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AlphaCurrSynapse._Automaton = _BuildAutomaton_90()




BlockingPlasticSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'plasticityMechanism'), PlasticityMechanism, scope=BlockingPlasticSynapse, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 651, 16)))

BlockingPlasticSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blockMechanism'), BlockMechanism, scope=BlockingPlasticSynapse, location=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 654, 2)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 651, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 654, 2))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BlockingPlasticSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BlockingPlasticSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BlockingPlasticSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'plasticityMechanism')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 651, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BlockingPlasticSynapse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blockMechanism')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 654, 2))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BlockingPlasticSynapse._Automaton = _BuildAutomaton_91()




def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNIaFCondCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(basePyNNIaFCondCell._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
basePyNNIaFCondCell._Automaton = _BuildAutomaton_92()




def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IF_curr_alpha._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IF_curr_alpha._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IF_curr_alpha._Automaton = _BuildAutomaton_93()




def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IF_curr_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IF_curr_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IF_curr_exp._Automaton = _BuildAutomaton_94()




def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IF_cond_alpha._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IF_cond_alpha._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IF_cond_alpha._Automaton = _BuildAutomaton_95()




def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IF_cond_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IF_cond_exp._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IF_cond_exp._Automaton = _BuildAutomaton_96()




def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EIF_cond_exp_isfa_ista._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EIF_cond_exp_isfa_ista._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EIF_cond_exp_isfa_ista._Automaton = _BuildAutomaton_97()




def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EIF_cond_alpha_isfa_ista._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1851, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EIF_cond_alpha_isfa_ista._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annotation')), pyxb.utils.utility.Location('https://raw.github.com/NeuroML/NeuroML2/master/Schemas/NeuroML2/NeuroML_v2beta1.xsd', 1852, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EIF_cond_alpha_isfa_ista._Automaton = _BuildAutomaton_98()

