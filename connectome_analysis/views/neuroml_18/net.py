# .\neuroml\net.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:56beb1973796b8a006baf6da39b86ef35282f15c
# Generated 2013-10-11 13:58:41.927000 by PyXB version 1.2.3
# Namespace http://morphml.org/networkml/schema [xmlns:net]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:869d53cf-32af-11e3-8e1e-001fbc00ed03')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import neuroml._nsgroup as _ImportedBinding_neuroml__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/networkml/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
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
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)

from neuroml._nsgroup import networkml # {http://morphml.org/networkml/schema}networkml
from neuroml._nsgroup import Populations # {http://morphml.org/networkml/schema}Populations
from neuroml._nsgroup import Input # {http://morphml.org/networkml/schema}Input
from neuroml._nsgroup import InputTarget # {http://morphml.org/networkml/schema}InputTarget
from neuroml._nsgroup import InputSitePattern # {http://morphml.org/networkml/schema}InputSitePattern
from neuroml._nsgroup import CTD_ANON_13 as CTD_ANON # None
from neuroml._nsgroup import InputSites # {http://morphml.org/networkml/schema}InputSites
from neuroml._nsgroup import Population # {http://morphml.org/networkml/schema}Population
from neuroml._nsgroup import Instances # {http://morphml.org/networkml/schema}Instances
from neuroml._nsgroup import Projection # {http://morphml.org/networkml/schema}Projection
from neuroml._nsgroup import SynapseProperties # {http://morphml.org/networkml/schema}SynapseProperties
from neuroml._nsgroup import ConnectivityPattern # {http://morphml.org/networkml/schema}ConnectivityPattern
from neuroml._nsgroup import CTD_ANON_14 as CTD_ANON_ # None
from neuroml._nsgroup import STD_ANON # None
from neuroml._nsgroup import Connections # {http://morphml.org/networkml/schema}Connections
from neuroml._nsgroup import CellInstance # {http://morphml.org/networkml/schema}CellInstance
from neuroml._nsgroup import PopulationLocation # {http://morphml.org/networkml/schema}PopulationLocation
from neuroml._nsgroup import RandomArrangement # {http://morphml.org/networkml/schema}RandomArrangement
from neuroml._nsgroup import GridArrangement # {http://morphml.org/networkml/schema}GridArrangement
from neuroml._nsgroup import CTD_ANON_15 as CTD_ANON_2 # None
from neuroml._nsgroup import Level3Connectivity # {http://morphml.org/networkml/schema}Level3Connectivity
from neuroml._nsgroup import PotentialSynapticLocation # {http://morphml.org/networkml/schema}PotentialSynapticLocation
from neuroml._nsgroup import SynapseDirection # {http://morphml.org/networkml/schema}SynapseDirection
from neuroml._nsgroup import CellIdInNetwork # {http://morphml.org/networkml/schema}CellIdInNetwork
from neuroml._nsgroup import NetworkML # {http://morphml.org/networkml/schema}NetworkML
from neuroml._nsgroup import Projections # {http://morphml.org/networkml/schema}Projections
from neuroml._nsgroup import Inputs # {http://morphml.org/networkml/schema}Inputs
from neuroml._nsgroup import PulseInput # {http://morphml.org/networkml/schema}PulseInput
from neuroml._nsgroup import RandomStim # {http://morphml.org/networkml/schema}RandomStim
from neuroml._nsgroup import RandomStimInstance # {http://morphml.org/networkml/schema}RandomStimInstance
from neuroml._nsgroup import CTD_ANON_18 as CTD_ANON_3 # None
from neuroml._nsgroup import InputSite # {http://morphml.org/networkml/schema}InputSite
from neuroml._nsgroup import SynapseInternalProperties # {http://morphml.org/networkml/schema}SynapseInternalProperties
from neuroml._nsgroup import CTD_ANON_19 as CTD_ANON_4 # None
from neuroml._nsgroup import PerCellConnection # {http://morphml.org/networkml/schema}PerCellConnection
from neuroml._nsgroup import Connection # {http://morphml.org/networkml/schema}Connection
from neuroml._nsgroup import SynapticLocation # {http://morphml.org/networkml/schema}SynapticLocation
from neuroml._nsgroup import PotentialSynLoc # {http://morphml.org/networkml/schema}PotentialSynLoc
from neuroml._nsgroup import GlobalSynapticProperties # {http://morphml.org/networkml/schema}GlobalSynapticProperties
from neuroml._nsgroup import LocalSynapticProperties # {http://morphml.org/networkml/schema}LocalSynapticProperties
