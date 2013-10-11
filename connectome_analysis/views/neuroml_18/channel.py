# .\neuroml\channel.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7c54b1740f0b1096e9b112f6498a2d56cf04af1f
# Generated 2013-10-11 13:58:41.927000 by PyXB version 1.2.3
# Namespace http://morphml.org/channelml/schema [xmlns:cml]

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
Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/channelml/schema', create_if_missing=True)
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

from neuroml._nsgroup import channelml # {http://morphml.org/channelml/schema}channelml
from neuroml._nsgroup import Parameters # {http://morphml.org/channelml/schema}Parameters
from neuroml._nsgroup import Parameter # {http://morphml.org/channelml/schema}Parameter
from neuroml._nsgroup import SynapseType # {http://morphml.org/channelml/schema}SynapseType
from neuroml._nsgroup import ConductanceLaw # {http://morphml.org/channelml/schema}ConductanceLaw
from neuroml._nsgroup import Deprecated_Ohmic # {http://morphml.org/channelml/schema}Deprecated_Ohmic
from neuroml._nsgroup import ImplementationPrefs # {http://morphml.org/channelml/schema}ImplementationPrefs
from neuroml._nsgroup import CTD_ANON # None
from neuroml._nsgroup import RateAdjustments # {http://morphml.org/channelml/schema}RateAdjustments
from neuroml._nsgroup import Deprecated_IonRole # {http://morphml.org/channelml/schema}Deprecated_IonRole
from neuroml._nsgroup import GatingComplex # {http://morphml.org/channelml/schema}GatingComplex
from neuroml._nsgroup import ClosedState # {http://morphml.org/channelml/schema}ClosedState
from neuroml._nsgroup import Gate # {http://morphml.org/channelml/schema}Gate
from neuroml._nsgroup import Deprecated_HHGate # {http://morphml.org/channelml/schema}Deprecated_HHGate
from neuroml._nsgroup import Deprecated_KSGate # {http://morphml.org/channelml/schema}Deprecated_KSGate
from neuroml._nsgroup import Deprecated_KSState # {http://morphml.org/channelml/schema}Deprecated_KSState
from neuroml._nsgroup import Deprecated_Transition # {http://morphml.org/channelml/schema}Deprecated_Transition
from neuroml._nsgroup import Initialisation # {http://morphml.org/channelml/schema}Initialisation
from neuroml._nsgroup import Deprecated_VoltageGate # {http://morphml.org/channelml/schema}Deprecated_VoltageGate
from neuroml._nsgroup import Deprecated_VoltageConcGate # {http://morphml.org/channelml/schema}Deprecated_VoltageConcGate
from neuroml._nsgroup import Deprecated_RateConstantEqnChoice # {http://morphml.org/channelml/schema}Deprecated_RateConstantEqnChoice
from neuroml._nsgroup import Deprecated_RateConstVoltConcDep # {http://morphml.org/channelml/schema}Deprecated_RateConstVoltConcDep
from neuroml._nsgroup import Deprecated_RateConstantEqn # {http://morphml.org/channelml/schema}Deprecated_RateConstantEqn
from neuroml._nsgroup import Deprecated_GenericEquation # {http://morphml.org/channelml/schema}Deprecated_GenericEquation
from neuroml._nsgroup import IonConcentration # {http://morphml.org/channelml/schema}IonConcentration
from neuroml._nsgroup import IonSpecies # {http://morphml.org/channelml/schema}IonSpecies
from neuroml._nsgroup import FixedPoolInfo # {http://morphml.org/channelml/schema}FixedPoolInfo
from neuroml._nsgroup import Deprecated_Parameter # {http://morphml.org/channelml/schema}Deprecated_Parameter
from neuroml._nsgroup import CoreEquationType # {http://morphml.org/channelml/schema}CoreEquationType
from neuroml._nsgroup import Deprecated_CoreEquationType # {http://morphml.org/channelml/schema}Deprecated_CoreEquationType
from neuroml._nsgroup import ChannelML # {http://morphml.org/channelml/schema}ChannelML
from neuroml._nsgroup import ChannelType # {http://morphml.org/channelml/schema}ChannelType
from neuroml._nsgroup import ElectricalSynapse # {http://morphml.org/channelml/schema}ElectricalSynapse
from neuroml._nsgroup import DoubleExponentialSynapse # {http://morphml.org/channelml/schema}DoubleExponentialSynapse
from neuroml._nsgroup import Block # {http://morphml.org/channelml/schema}Block
from neuroml._nsgroup import FacDep # {http://morphml.org/channelml/schema}FacDep
from neuroml._nsgroup import StdpDep # {http://morphml.org/channelml/schema}StdpDep
from neuroml._nsgroup import CurrentVoltageRelation # {http://morphml.org/channelml/schema}CurrentVoltageRelation
from neuroml._nsgroup import IntegrateAndFire # {http://morphml.org/channelml/schema}IntegrateAndFire
from neuroml._nsgroup import CTD_ANON_16 as CTD_ANON_ # None
from neuroml._nsgroup import Offset # {http://morphml.org/channelml/schema}Offset
from neuroml._nsgroup import Q10Settings # {http://morphml.org/channelml/schema}Q10Settings
from neuroml._nsgroup import Deprecated_Ion # {http://morphml.org/channelml/schema}Deprecated_Ion
from neuroml._nsgroup import OpenState # {http://morphml.org/channelml/schema}OpenState
from neuroml._nsgroup import CTD_ANON_17 as CTD_ANON_2 # None
from neuroml._nsgroup import Transition # {http://morphml.org/channelml/schema}Transition
from neuroml._nsgroup import TimeCourse # {http://morphml.org/channelml/schema}TimeCourse
from neuroml._nsgroup import SteadyState # {http://morphml.org/channelml/schema}SteadyState
from neuroml._nsgroup import ConcFactor # {http://morphml.org/channelml/schema}ConcFactor
from neuroml._nsgroup import ConcDependence # {http://morphml.org/channelml/schema}ConcDependence
from neuroml._nsgroup import Deprecated_AkdEquation # {http://morphml.org/channelml/schema}Deprecated_AkdEquation
from neuroml._nsgroup import DecayingPoolModel # {http://morphml.org/channelml/schema}DecayingPoolModel
from neuroml._nsgroup import PoolVolumeInfo # {http://morphml.org/channelml/schema}PoolVolumeInfo
from neuroml._nsgroup import BlockingSynapse # {http://morphml.org/channelml/schema}BlockingSynapse
from neuroml._nsgroup import MultiDecaySynapse # {http://morphml.org/channelml/schema}MultiDecaySynapse
from neuroml._nsgroup import FacDepSynapse # {http://morphml.org/channelml/schema}FacDepSynapse
from neuroml._nsgroup import StdpSynapse # {http://morphml.org/channelml/schema}StdpSynapse
