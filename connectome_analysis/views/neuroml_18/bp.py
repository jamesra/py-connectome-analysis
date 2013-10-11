# .\neuroml\bp.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:af6adc7a4ac9033387baea63595b128c13f64551
# Generated 2013-10-11 13:58:41.927000 by PyXB version 1.2.3
# Namespace http://morphml.org/biophysics/schema [xmlns:bio]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/biophysics/schema', create_if_missing=True)
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

from neuroml._nsgroup import biophysics # {http://morphml.org/biophysics/schema}biophysics
from neuroml._nsgroup import SpecCapacitance # {http://morphml.org/biophysics/schema}SpecCapacitance
from neuroml._nsgroup import SpecAxialResistance # {http://morphml.org/biophysics/schema}SpecAxialResistance
from neuroml._nsgroup import InitialMembPotential # {http://morphml.org/biophysics/schema}InitialMembPotential
from neuroml._nsgroup import IonProperties # {http://morphml.org/biophysics/schema}IonProperties
from neuroml._nsgroup import NamedParameter # {http://morphml.org/biophysics/schema}NamedParameter
from neuroml._nsgroup import VariableParameter # {http://morphml.org/biophysics/schema}VariableParameter
from neuroml._nsgroup import VariableNamedParameter # {http://morphml.org/biophysics/schema}VariableNamedParameter
from neuroml._nsgroup import InhomogeneousValue # {http://morphml.org/biophysics/schema}InhomogeneousValue
from neuroml._nsgroup import UnnamedParameter # {http://morphml.org/biophysics/schema}UnnamedParameter
from neuroml._nsgroup import MechanismType # {http://morphml.org/biophysics/schema}MechanismType
from neuroml._nsgroup import SynapticDelayValue # {http://morphml.org/biophysics/schema}SynapticDelayValue
from neuroml._nsgroup import TimeConstantValue # {http://morphml.org/biophysics/schema}TimeConstantValue
from neuroml._nsgroup import InvTimeConstantValue # {http://morphml.org/biophysics/schema}InvTimeConstantValue
from neuroml._nsgroup import TimeConstantValueIncZero # {http://morphml.org/biophysics/schema}TimeConstantValueIncZero
from neuroml._nsgroup import TimeValue # {http://morphml.org/biophysics/schema}TimeValue
from neuroml._nsgroup import FrequencyValue # {http://morphml.org/biophysics/schema}FrequencyValue
from neuroml._nsgroup import ConductanceValue # {http://morphml.org/biophysics/schema}ConductanceValue
from neuroml._nsgroup import ConductanceDensityValue # {http://morphml.org/biophysics/schema}ConductanceDensityValue
from neuroml._nsgroup import LengthValue # {http://morphml.org/biophysics/schema}LengthValue
from neuroml._nsgroup import CurrentValue # {http://morphml.org/biophysics/schema}CurrentValue
from neuroml._nsgroup import ConcentrationValue # {http://morphml.org/biophysics/schema}ConcentrationValue
from neuroml._nsgroup import VoltageValue # {http://morphml.org/biophysics/schema}VoltageValue
from neuroml._nsgroup import TemperatureValue # {http://morphml.org/biophysics/schema}TemperatureValue
from neuroml._nsgroup import Biophysics # {http://morphml.org/biophysics/schema}Biophysics
from neuroml._nsgroup import Mechanism # {http://morphml.org/biophysics/schema}Mechanism
