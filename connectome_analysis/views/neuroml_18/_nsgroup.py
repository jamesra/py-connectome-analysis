# .\neuroml\_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:38f6b4a17cef677a41e02589f8782bfe714fd0a1
# Generated 2013-10-11 13:54:11.907000 by PyXB version 1.1.4
# Group contents:
# Namespace http://morphml.org/networkml/schema [xmlns:net]
# Namespace http://morphml.org/biophysics/schema [xmlns:bio]
# Namespace http://morphml.org/channelml/schema [xmlns:cml]
# Namespace http://morphml.org/morphml/schema [xmlns:mml]
# Namespace http://morphml.org/metadata/schema [xmlns:meta]
# Namespace http://morphml.org/neuroml/schema


import pyxb
import pyxb.binding
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e495aec0-32ae-11e3-bae7-001fbc00ed03')

# Import bindings for schemas in group
import pyxb.binding.datatypes

_Namespace_bio = pyxb.namespace.NamespaceForURI(u'http://morphml.org/biophysics/schema', create_if_missing=True)
_Namespace_bio.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_meta = pyxb.namespace.NamespaceForURI(u'http://morphml.org/metadata/schema', create_if_missing=True)
_Namespace_meta.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_cml = pyxb.namespace.NamespaceForURI(u'http://morphml.org/channelml/schema', create_if_missing=True)
_Namespace_cml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_net = pyxb.namespace.NamespaceForURI(u'http://morphml.org/networkml/schema', create_if_missing=True)
_Namespace_net.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_mml = pyxb.namespace.NamespaceForURI(u'http://morphml.org/morphml/schema', create_if_missing=True)
_Namespace_mml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.namespace.NamespaceForURI(u'http://morphml.org/neuroml/schema', create_if_missing=True)
_Namespace.configureCategories(['typeBinding', 'elementBinding'])

# Atomic SimpleTypeDefinition
class ConcentrationValue (pyxb.binding.datatypes.double):

    """Units of concentration"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'ConcentrationValue')
    _Documentation = u'Units of concentration'
ConcentrationValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ConcentrationValue, value=pyxb.binding.datatypes.double(0.0))
ConcentrationValue._InitializeFacetMap(ConcentrationValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'ConcentrationValue', ConcentrationValue)

# Atomic SimpleTypeDefinition
class InvTimeConstantValue (pyxb.binding.datatypes.double):

    """Units of the inverse of a time constant"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'InvTimeConstantValue')
    _Documentation = u'Units of the inverse of a time constant'
InvTimeConstantValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=InvTimeConstantValue, value=pyxb.binding.datatypes.double(0.0))
InvTimeConstantValue._InitializeFacetMap(InvTimeConstantValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'InvTimeConstantValue', InvTimeConstantValue)

# Atomic SimpleTypeDefinition
class TimeConstantValue (pyxb.binding.datatypes.double):

    """Units of any time constant, greater than zero"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'TimeConstantValue')
    _Documentation = u'Units of any time constant, greater than zero'
TimeConstantValue._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'0'))
TimeConstantValue._InitializeFacetMap(TimeConstantValue._CF_minExclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'TimeConstantValue', TimeConstantValue)

# Atomic SimpleTypeDefinition
class Notes (pyxb.binding.datatypes.string):

    """Textual human readable notes related to the element in question. It's useful to put these into
         the NeuroML files instead of XML comments, as the notes can be extracted and repeated in the files to which the NeuroML is mapped."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Notes')
    _Documentation = u"Textual human readable notes related to the element in question. It's useful to put these into\n         the NeuroML files instead of XML comments, as the notes can be extracted and repeated in the files to which the NeuroML is mapped."
Notes._InitializeFacetMap()
_Namespace_meta.addCategoryObject('typeBinding', u'Notes', Notes)

# Atomic SimpleTypeDefinition
class Group (pyxb.binding.datatypes.string):

    """Allows elements to be associated, such as for grouping segments or cables into the basal arbor."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Group')
    _Documentation = u'Allows elements to be associated, such as for grouping segments or cables into the basal arbor.'
Group._InitializeFacetMap()
_Namespace_meta.addCategoryObject('typeBinding', u'Group', Group)

# Atomic SimpleTypeDefinition
class Percentage (pyxb.binding.datatypes.double):

    """Double restricted to between 0 and 100"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Percentage')
    _Documentation = u'Double restricted to between 0 and 100'
Percentage._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=Percentage, value=pyxb.binding.datatypes.double(100.0))
Percentage._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=Percentage, value=pyxb.binding.datatypes.double(0.0))
Percentage._InitializeFacetMap(Percentage._CF_maxInclusive,
   Percentage._CF_minInclusive)
_Namespace_meta.addCategoryObject('typeBinding', u'Percentage', Percentage)

# Atomic SimpleTypeDefinition
class ZeroToOne (pyxb.binding.datatypes.double):

    """Double restricted to between 1 and 0"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'ZeroToOne')
    _Documentation = u'Double restricted to between 1 and 0'
ZeroToOne._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ZeroToOne, value=pyxb.binding.datatypes.double(1.0))
ZeroToOne._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ZeroToOne, value=pyxb.binding.datatypes.double(0.0))
ZeroToOne._InitializeFacetMap(ZeroToOne._CF_maxInclusive,
   ZeroToOne._CF_minInclusive)
_Namespace_meta.addCategoryObject('typeBinding', u'ZeroToOne', ZeroToOne)

# Atomic SimpleTypeDefinition
class NonNegativeDouble (pyxb.binding.datatypes.double):

    """Double restricted to 0 or greater"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'NonNegativeDouble')
    _Documentation = u'Double restricted to 0 or greater'
NonNegativeDouble._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=NonNegativeDouble, value=pyxb.binding.datatypes.double(0.0))
NonNegativeDouble._InitializeFacetMap(NonNegativeDouble._CF_minInclusive)
_Namespace_meta.addCategoryObject('typeBinding', u'NonNegativeDouble', NonNegativeDouble)

# Atomic SimpleTypeDefinition
class VoltageValue (pyxb.binding.datatypes.double):

    """Units of voltage"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'VoltageValue')
    _Documentation = u'Units of voltage'
VoltageValue._InitializeFacetMap()
_Namespace_bio.addCategoryObject('typeBinding', u'VoltageValue', VoltageValue)

# Atomic SimpleTypeDefinition
class SynapticDelayValue (pyxb.binding.datatypes.double):

    """Units of a delay associated with a synaptic connection"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'SynapticDelayValue')
    _Documentation = u'Units of a delay associated with a synaptic connection'
SynapticDelayValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=SynapticDelayValue, value=pyxb.binding.datatypes.double(0.0))
SynapticDelayValue._InitializeFacetMap(SynapticDelayValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'SynapticDelayValue', SynapticDelayValue)

# Atomic SimpleTypeDefinition
class TimeValue (pyxb.binding.datatypes.double):

    """Units of any time value, zero or greater"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'TimeValue')
    _Documentation = u'Units of any time value, zero or greater'
TimeValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TimeValue, value=pyxb.binding.datatypes.double(0.0))
TimeValue._InitializeFacetMap(TimeValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'TimeValue', TimeValue)

# Atomic SimpleTypeDefinition
class CurrentValue (pyxb.binding.datatypes.double):

    """Units of current"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'CurrentValue')
    _Documentation = u'Units of current'
CurrentValue._InitializeFacetMap()
_Namespace_bio.addCategoryObject('typeBinding', u'CurrentValue', CurrentValue)

# Atomic SimpleTypeDefinition
class TemperatureValue (pyxb.binding.datatypes.double):

    """Units of temperature"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'TemperatureValue')
    _Documentation = u'Units of temperature'
TemperatureValue._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'0'))
TemperatureValue._InitializeFacetMap(TemperatureValue._CF_minExclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'TemperatureValue', TemperatureValue)

# Atomic SimpleTypeDefinition
class FrequencyValue (pyxb.binding.datatypes.double):

    """Units of any frequency, zero or greater"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'FrequencyValue')
    _Documentation = u'Units of any frequency, zero or greater'
FrequencyValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=FrequencyValue, value=pyxb.binding.datatypes.double(0.0))
FrequencyValue._InitializeFacetMap(FrequencyValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'FrequencyValue', FrequencyValue)

# Atomic SimpleTypeDefinition
class Units (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Enumeration of unit scheme used. Only SI or Physiological units allowed"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Units')
    _Documentation = u'Enumeration of unit scheme used. Only SI or Physiological units allowed'
Units._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Units, enum_prefix=None)
Units.Physiological_Units = Units._CF_enumeration.addEnumeration(unicode_value=u'Physiological Units', tag=u'Physiological_Units')
Units.SI_Units = Units._CF_enumeration.addEnumeration(unicode_value=u'SI Units', tag=u'SI_Units')
Units._InitializeFacetMap(Units._CF_enumeration)
_Namespace_meta.addCategoryObject('typeBinding', u'Units', Units)

# Atomic SimpleTypeDefinition
class LengthUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Enumeration of length units. Used in MorphML Level 1 files, where length is the only important dimension. Note: micrometer is preferred to micron from v1.8.1"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'LengthUnits')
    _Documentation = u'Enumeration of length units. Used in MorphML Level 1 files, where length is the only important dimension. Note: micrometer is preferred to micron from v1.8.1'
LengthUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=LengthUnits, enum_prefix=None)
LengthUnits.micron = LengthUnits._CF_enumeration.addEnumeration(unicode_value=u'micron', tag=u'micron')
LengthUnits.micrometer = LengthUnits._CF_enumeration.addEnumeration(unicode_value=u'micrometer', tag=u'micrometer')
LengthUnits.millimeter = LengthUnits._CF_enumeration.addEnumeration(unicode_value=u'millimeter', tag=u'millimeter')
LengthUnits.meter = LengthUnits._CF_enumeration.addEnumeration(unicode_value=u'meter', tag=u'meter')
LengthUnits._InitializeFacetMap(LengthUnits._CF_enumeration)
_Namespace_meta.addCategoryObject('typeBinding', u'LengthUnits', LengthUnits)

# Atomic SimpleTypeDefinition
class VolumeUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Enumeration of volume units."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'VolumeUnits')
    _Documentation = u'Enumeration of volume units.'
VolumeUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=VolumeUnits, enum_prefix=None)
VolumeUnits.cubic_millimeter = VolumeUnits._CF_enumeration.addEnumeration(unicode_value=u'cubic_millimeter', tag=u'cubic_millimeter')
VolumeUnits.millilitre = VolumeUnits._CF_enumeration.addEnumeration(unicode_value=u'millilitre', tag=u'millilitre')
VolumeUnits.litre = VolumeUnits._CF_enumeration.addEnumeration(unicode_value=u'litre', tag=u'litre')
VolumeUnits._InitializeFacetMap(VolumeUnits._CF_enumeration)
_Namespace_meta.addCategoryObject('typeBinding', u'VolumeUnits', VolumeUnits)

# Atomic SimpleTypeDefinition
class TimeConstantValueIncZero (pyxb.binding.datatypes.double):

    """Units of any time constant which can have value zero"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'TimeConstantValueIncZero')
    _Documentation = u'Units of any time constant which can have value zero'
TimeConstantValueIncZero._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=TimeConstantValueIncZero, value=pyxb.binding.datatypes.double(0.0))
TimeConstantValueIncZero._InitializeFacetMap(TimeConstantValueIncZero._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'TimeConstantValueIncZero', TimeConstantValueIncZero)

# Atomic SimpleTypeDefinition
class CoreEquationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Enumeration of core equation types, used from v1.7.3: exp_linear, sigmoidal, exponential"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'CoreEquationType')
    _Documentation = u'Enumeration of core equation types, used from v1.7.3: exp_linear, sigmoidal, exponential'
CoreEquationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=CoreEquationType, enum_prefix=None)
CoreEquationType.exponential = CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'exponential', tag=u'exponential')
CoreEquationType.sigmoid = CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'sigmoid', tag=u'sigmoid')
CoreEquationType.exp_linear = CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'exp_linear', tag=u'exp_linear')
CoreEquationType.generic = CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'generic', tag=u'generic')
CoreEquationType._InitializeFacetMap(CoreEquationType._CF_enumeration)
_Namespace_cml.addCategoryObject('typeBinding', u'CoreEquationType', CoreEquationType)

# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.PreToPost = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'PreToPost', tag=u'PreToPost')
STD_ANON.PostToPre = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'PostToPre', tag=u'PostToPre')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic SimpleTypeDefinition
class PositiveDouble (pyxb.binding.datatypes.double):

    """Double restricted greater than 0"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'PositiveDouble')
    _Documentation = u'Double restricted greater than 0'
PositiveDouble._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'0'))
PositiveDouble._InitializeFacetMap(PositiveDouble._CF_minExclusive)
_Namespace_meta.addCategoryObject('typeBinding', u'PositiveDouble', PositiveDouble)

# Atomic SimpleTypeDefinition
class CellIdInNetwork (pyxb.binding.datatypes.nonNegativeInteger):

    """Id of individual cell in a network"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'CellIdInNetwork')
    _Documentation = u'Id of individual cell in a network'
CellIdInNetwork._InitializeFacetMap()
_Namespace_net.addCategoryObject('typeBinding', u'CellIdInNetwork', CellIdInNetwork)

# Atomic SimpleTypeDefinition
class SegmentIdInCell (pyxb.binding.datatypes.nonNegativeInteger):

    """Id of individual segment in a cell (integer 0 or greater). Placed in Metadata, as it's used across Levels"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'SegmentIdInCell')
    _Documentation = u"Id of individual segment in a cell (integer 0 or greater). Placed in Metadata, as it's used across Levels"
SegmentIdInCell._InitializeFacetMap()
_Namespace_meta.addCategoryObject('typeBinding', u'SegmentIdInCell', SegmentIdInCell)

# Atomic SimpleTypeDefinition
class Metric (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Metric for use in InhomogeneousParam"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Metric')
    _Documentation = u'Metric for use in InhomogeneousParam'
Metric._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Metric, enum_prefix=None)
Metric.Path_Length_from_root = Metric._CF_enumeration.addEnumeration(unicode_value=u'Path Length from root', tag=u'Path_Length_from_root')
Metric.n3D_radial_position = Metric._CF_enumeration.addEnumeration(unicode_value=u'3D radial position', tag=u'n3D_radial_position')
Metric.n3D_path_length_from_line = Metric._CF_enumeration.addEnumeration(unicode_value=u'3D path length from line', tag=u'n3D_path_length_from_line')
Metric._InitializeFacetMap(Metric._CF_enumeration)
_Namespace_mml.addCategoryObject('typeBinding', u'Metric', Metric)

# Atomic SimpleTypeDefinition
class ConductanceValue (pyxb.binding.datatypes.double):

    """Units of conductance"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'ConductanceValue')
    _Documentation = u'Units of conductance'
ConductanceValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ConductanceValue, value=pyxb.binding.datatypes.double(0.0))
ConductanceValue._InitializeFacetMap(ConductanceValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'ConductanceValue', ConductanceValue)

# Atomic SimpleTypeDefinition
class LengthValue (pyxb.binding.datatypes.double):

    """Units of length"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'LengthValue')
    _Documentation = u'Units of length'
LengthValue._InitializeFacetMap()
_Namespace_bio.addCategoryObject('typeBinding', u'LengthValue', LengthValue)

# Atomic SimpleTypeDefinition
class YesNo (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """String with only yes or no allowed"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'YesNo')
    _Documentation = u'String with only yes or no allowed'
YesNo._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=YesNo, enum_prefix=None)
YesNo.yes = YesNo._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
YesNo.no = YesNo._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
YesNo._InitializeFacetMap(YesNo._CF_enumeration)
_Namespace_meta.addCategoryObject('typeBinding', u'YesNo', YesNo)

# Atomic SimpleTypeDefinition
class ConductanceDensityValue (pyxb.binding.datatypes.double):

    """Units of conductance density"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'ConductanceDensityValue')
    _Documentation = u'Units of conductance density'
ConductanceDensityValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ConductanceDensityValue, value=pyxb.binding.datatypes.double(0.0))
ConductanceDensityValue._InitializeFacetMap(ConductanceDensityValue._CF_minInclusive)
_Namespace_bio.addCategoryObject('typeBinding', u'ConductanceDensityValue', ConductanceDensityValue)

# Atomic SimpleTypeDefinition
class Deprecated_CoreEquationType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Core equation types prior to v1.7.3, linoidal, sigmoidal, exponential"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_CoreEquationType')
    _Documentation = u'Core equation types prior to v1.7.3, linoidal, sigmoidal, exponential'
Deprecated_CoreEquationType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Deprecated_CoreEquationType, enum_prefix=None)
Deprecated_CoreEquationType.exponential = Deprecated_CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'exponential', tag=u'exponential')
Deprecated_CoreEquationType.sigmoid = Deprecated_CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'sigmoid', tag=u'sigmoid')
Deprecated_CoreEquationType.linoid = Deprecated_CoreEquationType._CF_enumeration.addEnumeration(unicode_value=u'linoid', tag=u'linoid')
Deprecated_CoreEquationType._InitializeFacetMap(Deprecated_CoreEquationType._CF_enumeration)
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_CoreEquationType', Deprecated_CoreEquationType)

# Atomic SimpleTypeDefinition
class SynapseDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Indicated whether a potential synapse location allows a presynaptic connection
                of the specified type, a postsynaptic connection or either. """

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'SynapseDirection')
    _Documentation = u'Indicated whether a potential synapse location allows a presynaptic connection\n                of the specified type, a postsynaptic connection or either. '
SynapseDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SynapseDirection, enum_prefix=None)
SynapseDirection.pre = SynapseDirection._CF_enumeration.addEnumeration(unicode_value=u'pre', tag=u'pre')
SynapseDirection.post = SynapseDirection._CF_enumeration.addEnumeration(unicode_value=u'post', tag=u'post')
SynapseDirection.preAndOrPost = SynapseDirection._CF_enumeration.addEnumeration(unicode_value=u'preAndOrPost', tag=u'preAndOrPost')
SynapseDirection._InitializeFacetMap(SynapseDirection._CF_enumeration)
_Namespace_net.addCategoryObject('typeBinding', u'SynapseDirection', SynapseDirection)

# Atomic SimpleTypeDefinition
class SpineShape (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Enumeration of allowed spine shapes."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'SpineShape')
    _Documentation = u'Enumeration of allowed spine shapes.'
SpineShape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=SpineShape, enum_prefix=None)
SpineShape.mushroom = SpineShape._CF_enumeration.addEnumeration(unicode_value=u'mushroom', tag=u'mushroom')
SpineShape.stubby = SpineShape._CF_enumeration.addEnumeration(unicode_value=u'stubby', tag=u'stubby')
SpineShape.thin = SpineShape._CF_enumeration.addEnumeration(unicode_value=u'thin', tag=u'thin')
SpineShape._InitializeFacetMap(SpineShape._CF_enumeration)
_Namespace_mml.addCategoryObject('typeBinding', u'SpineShape', SpineShape)

# Atomic SimpleTypeDefinition
class Deprecated_IonRole (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Role ion plays in cellular mechanism, e.g. ion passes through the channel (Na, K), or the 
            concentration of the ion is a factor in the rate equations of gating, or the mechanism alters 
            the concentration of this ion. This greatly simplifies the number of roles an ion can play 
            in the channel, but these options cover the majority of cases currently being modelled. Note: the term subtance is used as 
            this formalism can also be used for other chemicals which may be transmitted, modulate channels, etc."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_IonRole')
    _Documentation = u'Role ion plays in cellular mechanism, e.g. ion passes through the channel (Na, K), or the \n            concentration of the ion is a factor in the rate equations of gating, or the mechanism alters \n            the concentration of this ion. This greatly simplifies the number of roles an ion can play \n            in the channel, but these options cover the majority of cases currently being modelled. Note: the term subtance is used as \n            this formalism can also be used for other chemicals which may be transmitted, modulate channels, etc.'
Deprecated_IonRole._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=Deprecated_IonRole, enum_prefix=None)
Deprecated_IonRole.PermeatedSubstance = Deprecated_IonRole._CF_enumeration.addEnumeration(unicode_value=u'PermeatedSubstance', tag=u'PermeatedSubstance')
Deprecated_IonRole.PermeatedSubstanceFixedRevPot = Deprecated_IonRole._CF_enumeration.addEnumeration(unicode_value=u'PermeatedSubstanceFixedRevPot', tag=u'PermeatedSubstanceFixedRevPot')
Deprecated_IonRole.ModulatingSubstance = Deprecated_IonRole._CF_enumeration.addEnumeration(unicode_value=u'ModulatingSubstance', tag=u'ModulatingSubstance')
Deprecated_IonRole.SignallingSubstance = Deprecated_IonRole._CF_enumeration.addEnumeration(unicode_value=u'SignallingSubstance', tag=u'SignallingSubstance')
Deprecated_IonRole._InitializeFacetMap(Deprecated_IonRole._CF_enumeration)
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_IonRole', Deprecated_IonRole)

# Atomic SimpleTypeDefinition
class StatusValue (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Status enum for stability state of files. This is subject to change."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'StatusValue')
    _Documentation = u'Status enum for stability state of files. This is subject to change.'
StatusValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=StatusValue, enum_prefix=None)
StatusValue.stable = StatusValue._CF_enumeration.addEnumeration(unicode_value=u'stable', tag=u'stable')
StatusValue.in_progress = StatusValue._CF_enumeration.addEnumeration(unicode_value=u'in_progress', tag=u'in_progress')
StatusValue.known_issues = StatusValue._CF_enumeration.addEnumeration(unicode_value=u'known_issues', tag=u'known_issues')
StatusValue.deprecated = StatusValue._CF_enumeration.addEnumeration(unicode_value=u'deprecated', tag=u'deprecated')
StatusValue._InitializeFacetMap(StatusValue._CF_enumeration)
_Namespace_meta.addCategoryObject('typeBinding', u'StatusValue', StatusValue)

# Atomic SimpleTypeDefinition
class ConductanceLaw (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Introduced in v1.7.3 for new format ChannelML. Specifies which type of conductance law to use: ohmic, etc."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ConductanceLaw')
    _Documentation = u'Introduced in v1.7.3 for new format ChannelML. Specifies which type of conductance law to use: ohmic, etc.'
ConductanceLaw._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ConductanceLaw, enum_prefix=None)
ConductanceLaw.ohmic = ConductanceLaw._CF_enumeration.addEnumeration(unicode_value=u'ohmic', tag=u'ohmic')
ConductanceLaw.integrate_and_fire = ConductanceLaw._CF_enumeration.addEnumeration(unicode_value=u'integrate_and_fire', tag=u'integrate_and_fire')
ConductanceLaw._InitializeFacetMap(ConductanceLaw._CF_enumeration)
_Namespace_cml.addCategoryObject('typeBinding', u'ConductanceLaw', ConductanceLaw)

# Atomic SimpleTypeDefinition
class MechanismType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Specifies the type of cellular mechanism. Note could be used for any type of electrophysiological
                property of a section of a cell"""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'MechanismType')
    _Documentation = u'Specifies the type of cellular mechanism. Note could be used for any type of electrophysiological\n                property of a section of a cell'
MechanismType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=MechanismType, enum_prefix=None)
MechanismType.Channel_Mechanism = MechanismType._CF_enumeration.addEnumeration(unicode_value=u'Channel Mechanism', tag=u'Channel_Mechanism')
MechanismType.Ion_Concentration = MechanismType._CF_enumeration.addEnumeration(unicode_value=u'Ion Concentration', tag=u'Ion_Concentration')
MechanismType._InitializeFacetMap(MechanismType._CF_enumeration)
_Namespace_bio.addCategoryObject('typeBinding', u'MechanismType', MechanismType)

# Complex type ConcDependence with content type EMPTY
class ConcDependence (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ConcDependence')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute charge uses Python identifier charge
    __charge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'charge'), 'charge', '__httpmorphml_orgchannelmlschema_ConcDependence_charge', pyxb.binding.datatypes.integer, unicode_default=u'1')
    
    charge = property(__charge.value, __charge.set, None, u'Electrical charge of the ion in question. Assumes charge of 1 if not present')

    
    # Attribute variable_name uses Python identifier variable_name
    __variable_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'variable_name'), 'variable_name', '__httpmorphml_orgchannelmlschema_ConcDependence_variable_name', pyxb.binding.datatypes.string, required=True)
    
    variable_name = property(__variable_name.value, __variable_name.set, None, u'How the value of conductance will be expressed in the rate equations')

    
    # Attribute max_conc uses Python identifier max_conc
    __max_conc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_conc'), 'max_conc', '__httpmorphml_orgchannelmlschema_ConcDependence_max_conc', ConcentrationValue, required=True)
    
    max_conc = property(__max_conc.value, __max_conc.set, None, u'Maximum expected concentration. Quite likely to be needed by simulators (e.g. for generating tables)')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_ConcDependence_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name of substance, just for reference')

    
    # Attribute min_conc uses Python identifier min_conc
    __min_conc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'min_conc'), 'min_conc', '__httpmorphml_orgchannelmlschema_ConcDependence_min_conc', ConcentrationValue, required=True)
    
    min_conc = property(__min_conc.value, __min_conc.set, None, u'Minimum expected concentration. Quite likely to be needed by simulators (e.g. for generating tables)')

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpmorphml_orgchannelmlschema_ConcDependence_ion', pyxb.binding.datatypes.string, required=True)
    
    ion = property(__ion.value, __ion.set, None, u'Name of the ion')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __charge.name() : __charge,
        __variable_name.name() : __variable_name,
        __max_conc.name() : __max_conc,
        __name.name() : __name,
        __min_conc.name() : __min_conc,
        __ion.name() : __ion
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ConcDependence', ConcDependence)


# Complex type DecayingPoolModel with content type ELEMENT_ONLY
class DecayingPoolModel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'DecayingPoolModel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}fixed_pool_info uses Python identifier fixed_pool_info
    __fixed_pool_info = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'fixed_pool_info'), 'fixed_pool_info', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemafixed_pool_info', False)

    
    fixed_pool_info = property(__fixed_pool_info.value, __fixed_pool_info.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}ceiling uses Python identifier ceiling
    __ceiling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ceiling'), 'ceiling', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemaceiling', False)

    
    ceiling = property(__ceiling.value, __ceiling.set, None, u'The maximum concentration which the ion pool should be allowed get to. NOTE: In v2.0 this element will be removed. Attribute ceiling will be used instead.')

    
    # Element {http://morphml.org/channelml/schema}resting_conc uses Python identifier resting_conc
    __resting_conc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'resting_conc'), 'resting_conc', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemaresting_conc', False)

    
    resting_conc = property(__resting_conc.value, __resting_conc.set, None, u'Resting concentration of ion. NOTE: In v2.0 this element will be removed. Attribute resting_conc will be used instead.')

    
    # Element {http://morphml.org/channelml/schema}decay_constant uses Python identifier decay_constant
    __decay_constant = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'decay_constant'), 'decay_constant', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemadecay_constant', False)

    
    decay_constant = property(__decay_constant.value, __decay_constant.set, None, u'Exponential decay time of pool. NOTE: In v2.0 this element will be removed. Attribute decay_constant will be used instead.')

    
    # Element {http://morphml.org/channelml/schema}pool_volume_info uses Python identifier pool_volume_info
    __pool_volume_info = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'pool_volume_info'), 'pool_volume_info', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemapool_volume_info', False)

    
    pool_volume_info = property(__pool_volume_info.value, __pool_volume_info.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}inv_decay_constant uses Python identifier inv_decay_constant
    __inv_decay_constant = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'inv_decay_constant'), 'inv_decay_constant', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_httpmorphml_orgchannelmlschemainv_decay_constant', False)

    
    inv_decay_constant = property(__inv_decay_constant.value, __inv_decay_constant.set, None, u'Reciprocal of exponential decay time constant of pool')

    
    # Attribute inv_decay_constant uses Python identifier inv_decay_constant_
    __inv_decay_constant_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'inv_decay_constant'), 'inv_decay_constant_', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_inv_decay_constant', InvTimeConstantValue)
    
    inv_decay_constant_ = property(__inv_decay_constant_.value, __inv_decay_constant_.set, None, u'Reciprocal of exponential decay time of pool. Either decay_constant or inv_decay_constant must be included. NOTE: In v2.0 the option for \n                a decay_constant/inv_decay_constant element will be removed. Attribute decay_constant/inv_decay_constant will be used instead.')

    
    # Attribute ceiling uses Python identifier ceiling_
    __ceiling_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ceiling'), 'ceiling_', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_ceiling', ConcentrationValue)
    
    ceiling_ = property(__ceiling_.value, __ceiling_.set, None, u'The maximum concentration which the ion pool should be allowed get to. NOTE: In v2.0 the option for \n                a ceiling element will be removed. Attribute ceiling will be used instead.')

    
    # Attribute resting_conc uses Python identifier resting_conc_
    __resting_conc_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'resting_conc'), 'resting_conc_', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_resting_conc', ConcentrationValue)
    
    resting_conc_ = property(__resting_conc_.value, __resting_conc_.set, None, u'Resting concentration of ion. NOTE: In v2.0 the option for a resting_conc element will be removed. Attribute resting_conc will be required instead.')

    
    # Attribute decay_constant uses Python identifier decay_constant_
    __decay_constant_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decay_constant'), 'decay_constant_', '__httpmorphml_orgchannelmlschema_DecayingPoolModel_decay_constant', TimeConstantValue)
    
    decay_constant_ = property(__decay_constant_.value, __decay_constant_.set, None, u'Exponential decay time of pool. Either decay_constant or inv_decay_constant must be included. NOTE: In v2.0 the option for \n                a decay_constant/inv_decay_constant element will be removed. Attribute decay_constant/inv_decay_constant will be used instead.')


    _ElementMap = {
        __fixed_pool_info.name() : __fixed_pool_info,
        __ceiling.name() : __ceiling,
        __resting_conc.name() : __resting_conc,
        __decay_constant.name() : __decay_constant,
        __pool_volume_info.name() : __pool_volume_info,
        __inv_decay_constant.name() : __inv_decay_constant
    }
    _AttributeMap = {
        __inv_decay_constant_.name() : __inv_decay_constant_,
        __ceiling_.name() : __ceiling_,
        __resting_conc_.name() : __resting_conc_,
        __decay_constant_.name() : __decay_constant_
    }
_Namespace_cml.addCategoryObject('typeBinding', u'DecayingPoolModel', DecayingPoolModel)


# Complex type ConcFactor with content type EMPTY
class ConcFactor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ConcFactor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpmorphml_orgchannelmlschema_ConcFactor_ion', pyxb.binding.datatypes.string, required=True)
    
    ion = property(__ion.value, __ion.set, None, u'Name of the ion')

    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_ConcFactor_expr', pyxb.binding.datatypes.string, required=True)
    
    expr = property(__expr.value, __expr.set, None, u'Expression for the time independent multiplicative factor for the concentration dependence')

    
    # Attribute charge uses Python identifier charge
    __charge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'charge'), 'charge', '__httpmorphml_orgchannelmlschema_ConcFactor_charge', pyxb.binding.datatypes.integer, unicode_default=u'1')
    
    charge = property(__charge.value, __charge.set, None, u'Electrical charge of the ion in question. Assumes charge of 1 if not present')

    
    # Attribute min_conc uses Python identifier min_conc
    __min_conc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'min_conc'), 'min_conc', '__httpmorphml_orgchannelmlschema_ConcFactor_min_conc', ConcentrationValue, required=True)
    
    min_conc = property(__min_conc.value, __min_conc.set, None, u'Minimum expected concentration. May be needed by simulators (e.g. for generating tables)')

    
    # Attribute variable_name uses Python identifier variable_name
    __variable_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'variable_name'), 'variable_name', '__httpmorphml_orgchannelmlschema_ConcFactor_variable_name', pyxb.binding.datatypes.string, required=True)
    
    variable_name = property(__variable_name.value, __variable_name.set, None, u'How the value of conductance will be expressed in the equations')

    
    # Attribute max_conc uses Python identifier max_conc
    __max_conc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_conc'), 'max_conc', '__httpmorphml_orgchannelmlschema_ConcFactor_max_conc', ConcentrationValue, required=True)
    
    max_conc = property(__max_conc.value, __max_conc.set, None, u'Maximum expected concentration. May be needed by simulators (e.g. for generating tables)')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __ion.name() : __ion,
        __expr.name() : __expr,
        __charge.name() : __charge,
        __min_conc.name() : __min_conc,
        __variable_name.name() : __variable_name,
        __max_conc.name() : __max_conc
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ConcFactor', ConcFactor)


# Complex type Annotation with content type ELEMENT_ONLY
class Annotation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Annotation')
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Annotation', Annotation)


# Complex type Properties with content type ELEMENT_ONLY
class Properties (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Properties')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}property uses Python identifier property_
    __property = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'property'), 'property_', '__httpmorphml_orgmetadataschema_Properties_httpmorphml_orgmetadataschemaproperty', True)

    
    property_ = property(__property.value, __property.set, None, None)


    _ElementMap = {
        __property.name() : __property
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Properties', Properties)


# Complex type InputSitePattern with content type ELEMENT_ONLY
class InputSitePattern (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'InputSitePattern')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}percentage_cells uses Python identifier percentage_cells
    __percentage_cells = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'percentage_cells'), 'percentage_cells', '__httpmorphml_orgnetworkmlschema_InputSitePattern_httpmorphml_orgnetworkmlschemapercentage_cells', False)

    
    percentage_cells = property(__percentage_cells.value, __percentage_cells.set, None, u'Apply input to a certain percentage of cells in a group')

    
    # Element {http://morphml.org/networkml/schema}all_cells uses Python identifier all_cells
    __all_cells = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'all_cells'), 'all_cells', '__httpmorphml_orgnetworkmlschema_InputSitePattern_httpmorphml_orgnetworkmlschemaall_cells', False)

    
    all_cells = property(__all_cells.value, __all_cells.set, None, u'Apply input on all cells in group')


    _ElementMap = {
        __percentage_cells.name() : __percentage_cells,
        __all_cells.name() : __all_cells
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'InputSitePattern', InputSitePattern)


# Complex type GatingComplex with content type ELEMENT_ONLY
class GatingComplex (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'GatingComplex')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}open_state uses Python identifier open_state
    __open_state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'open_state'), 'open_state', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschemaopen_state', True)

    
    open_state = property(__open_state.value, __open_state.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), 'transition', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschematransition', True)

    
    transition = property(__transition.value, __transition.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}time_course uses Python identifier time_course
    __time_course = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'time_course'), 'time_course', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschematime_course', True)

    
    time_course = property(__time_course.value, __time_course.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}steady_state uses Python identifier steady_state
    __steady_state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'steady_state'), 'steady_state', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschemasteady_state', True)

    
    steady_state = property(__steady_state.value, __steady_state.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}closed_state uses Python identifier closed_state
    __closed_state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'closed_state'), 'closed_state', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschemaclosed_state', True)

    
    closed_state = property(__closed_state.value, __closed_state.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}initialisation uses Python identifier initialisation
    __initialisation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), 'initialisation', '__httpmorphml_orgchannelmlschema_GatingComplex_httpmorphml_orgchannelmlschemainitialisation', False)

    
    initialisation = property(__initialisation.value, __initialisation.set, None, u'For debugging/testing only! Use with caution!!')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_GatingComplex_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Reference for the gating complex, e.g. m, h, n')

    
    # Attribute instances uses Python identifier instances
    __instances = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'instances'), 'instances', '__httpmorphml_orgchannelmlschema_GatingComplex_instances', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    instances = property(__instances.value, __instances.set, None, u'The number of instances of the gate, i.e. the power to which the gating variable is raised in the expression for the total conductance')


    _ElementMap = {
        __open_state.name() : __open_state,
        __transition.name() : __transition,
        __time_course.name() : __time_course,
        __steady_state.name() : __steady_state,
        __closed_state.name() : __closed_state,
        __initialisation.name() : __initialisation
    }
    _AttributeMap = {
        __name.name() : __name,
        __instances.name() : __instances
    }
_Namespace_cml.addCategoryObject('typeBinding', u'GatingComplex', GatingComplex)


# Complex type VariableNamedParameter with content type ELEMENT_ONLY
class VariableNamedParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'VariableNamedParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}inhomogeneous_value uses Python identifier inhomogeneous_value
    __inhomogeneous_value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value'), 'inhomogeneous_value', '__httpmorphml_orgbiophysicsschema_VariableNamedParameter_httpmorphml_orgbiophysicsschemainhomogeneous_value', True)

    
    inhomogeneous_value = property(__inhomogeneous_value.value, __inhomogeneous_value.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), 'group', '__httpmorphml_orgbiophysicsschema_VariableNamedParameter_httpmorphml_orgbiophysicsschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgbiophysicsschema_VariableNamedParameter_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __inhomogeneous_value.name() : __inhomogeneous_value,
        __group.name() : __group
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'VariableNamedParameter', VariableNamedParameter)


# Complex type CTD_ANON with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute percentage uses Python identifier percentage
    __percentage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'percentage'), 'percentage', '__httpmorphml_orgnetworkmlschema_CTD_ANON_percentage', Percentage)
    
    percentage = property(__percentage.value, __percentage.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __percentage.name() : __percentage
    }



# Complex type NeuroMorphoRef with content type ELEMENT_ONLY
class NeuroMorphoRef (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'NeuroMorphoRef')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}morphologyRef uses Python identifier morphologyRef
    __morphologyRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'morphologyRef'), 'morphologyRef', '__httpmorphml_orgmetadataschema_NeuroMorphoRef_httpmorphml_orgmetadataschemamorphologyRef', False)

    
    morphologyRef = property(__morphologyRef.value, __morphologyRef.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_NeuroMorphoRef_httpmorphml_orgmetadataschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Comment on how this morphology relates to the current model')

    
    # Element {http://morphml.org/metadata/schema}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), 'uri', '__httpmorphml_orgmetadataschema_NeuroMorphoRef_httpmorphml_orgmetadataschemauri', False)

    
    uri = property(__uri.value, __uri.set, None, None)


    _ElementMap = {
        __morphologyRef.name() : __morphologyRef,
        __comment.name() : __comment,
        __uri.name() : __uri
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'NeuroMorphoRef', NeuroMorphoRef)


# Complex type CTD_ANON_ with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute probability uses Python identifier probability
    __probability = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'probability'), 'probability', '__httpmorphml_orgnetworkmlschema_CTD_ANON__probability', ZeroToOne)
    
    probability = property(__probability.value, __probability.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __probability.name() : __probability
    }



# Complex type Person with content type ELEMENT_ONLY
class Person (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Person')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'name'), 'name', '__httpmorphml_orgmetadataschema_Person_httpmorphml_orgmetadataschemaname', False)

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_Person_httpmorphml_orgmetadataschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Optional comment on their specific contribution')

    
    # Element {http://morphml.org/metadata/schema}email uses Python identifier email
    __email = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'email'), 'email', '__httpmorphml_orgmetadataschema_Person_httpmorphml_orgmetadataschemaemail', False)

    
    email = property(__email.value, __email.set, None, u"Useful to have. Note: something like '- at -' replacing the @ might be wise, in case a HTML version of the file goes online.")

    
    # Element {http://morphml.org/metadata/schema}institution uses Python identifier institution
    __institution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'institution'), 'institution', '__httpmorphml_orgmetadataschema_Person_httpmorphml_orgmetadataschemainstitution', False)

    
    institution = property(__institution.value, __institution.set, None, None)


    _ElementMap = {
        __name.name() : __name,
        __comment.name() : __comment,
        __email.name() : __email,
        __institution.name() : __institution
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Person', Person)


# Complex type UnnamedParameter with content type ELEMENT_ONLY
class UnnamedParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'UnnamedParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), 'group', '__httpmorphml_orgbiophysicsschema_UnnamedParameter_httpmorphml_orgbiophysicsschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgbiophysicsschema_UnnamedParameter_value', pyxb.binding.datatypes.double, required=True)
    
    value_ = property(__value.value, __value.set, None, None)


    _ElementMap = {
        __group.name() : __group
    }
    _AttributeMap = {
        __value.name() : __value
    }
_Namespace_bio.addCategoryObject('typeBinding', u'UnnamedParameter', UnnamedParameter)


# Complex type VariableParameter with content type ELEMENT_ONLY
class VariableParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'VariableParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}inhomogeneous_value uses Python identifier inhomogeneous_value
    __inhomogeneous_value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value'), 'inhomogeneous_value', '__httpmorphml_orgbiophysicsschema_VariableParameter_httpmorphml_orgbiophysicsschemainhomogeneous_value', True)

    
    inhomogeneous_value = property(__inhomogeneous_value.value, __inhomogeneous_value.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), 'group', '__httpmorphml_orgbiophysicsschema_VariableParameter_httpmorphml_orgbiophysicsschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgbiophysicsschema_VariableParameter_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __inhomogeneous_value.name() : __inhomogeneous_value,
        __group.name() : __group
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'VariableParameter', VariableParameter)


# Complex type Deprecated_RateConstantEqnChoice with content type ELEMENT_ONLY
class Deprecated_RateConstantEqnChoice (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_RateConstantEqnChoice')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}generic uses Python identifier generic
    __generic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic'), 'generic', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgchannelmlschemageneric', False)

    
    generic = property(__generic.value, __generic.set, None, u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}parameterised_hh uses Python identifier parameterised_hh
    __parameterised_hh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameterised_hh'), 'parameterised_hh', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgchannelmlschemaparameterised_hh', False)

    
    parameterised_hh = property(__parameterised_hh.value, __parameterised_hh.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}generic_equation_hh uses Python identifier generic_equation_hh
    __generic_equation_hh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh'), 'generic_equation_hh', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqnChoice_httpmorphml_orgchannelmlschemageneric_equation_hh', False)

    
    generic_equation_hh = property(__generic_equation_hh.value, __generic_equation_hh.set, None, u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0')


    _ElementMap = {
        __annotation.name() : __annotation,
        __properties.name() : __properties,
        __generic.name() : __generic,
        __group.name() : __group,
        __notes.name() : __notes,
        __parameterised_hh.name() : __parameterised_hh,
        __generic_equation_hh.name() : __generic_equation_hh
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_RateConstantEqnChoice', Deprecated_RateConstantEqnChoice)


# Complex type SynapseInternalProperties with content type ELEMENT_ONLY
class SynapseInternalProperties (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'SynapseInternalProperties')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Attribute prop_delay uses Python identifier prop_delay
    __prop_delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'prop_delay'), 'prop_delay', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_prop_delay', SynapticDelayValue, unicode_default=u'0')
    
    prop_delay = property(__prop_delay.value, __prop_delay.set, None, u'Delay due to simulated AP propagation along an axon')

    
    # Attribute weight uses Python identifier weight
    __weight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'weight'), 'weight', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_weight', NonNegativeDouble, unicode_default=u'1')
    
    weight = property(__weight.value, __weight.set, None, u'Multiplicative weighting factor for the synapse')

    
    # Attribute pre_delay uses Python identifier pre_delay
    __pre_delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'pre_delay'), 'pre_delay', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_pre_delay', SynapticDelayValue, unicode_default=u'0')
    
    pre_delay = property(__pre_delay.value, __pre_delay.set, None, u'Delay due to presynaptic mechanism')

    
    # Attribute threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'threshold'), 'threshold', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_threshold', VoltageValue, unicode_default=u'0')
    
    threshold = property(__threshold.value, __threshold.set, None, u'Presynaptic membrane potential level above which the synapse fires')

    
    # Attribute post_delay uses Python identifier post_delay
    __post_delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'post_delay'), 'post_delay', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_post_delay', SynapticDelayValue, unicode_default=u'0')
    
    post_delay = property(__post_delay.value, __post_delay.set, None, u'Delay due to postsynaptic mechanism')

    
    # Attribute internal_delay uses Python identifier internal_delay
    __internal_delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'internal_delay'), 'internal_delay', '__httpmorphml_orgnetworkmlschema_SynapseInternalProperties_internal_delay', SynapticDelayValue, unicode_default=u'0')
    
    internal_delay = property(__internal_delay.value, __internal_delay.set, None, u'Delay due to diffusion across the synaptic cleft. If only one delay value is known, this can be used')


    _ElementMap = {
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties
    }
    _AttributeMap = {
        __prop_delay.name() : __prop_delay,
        __weight.name() : __weight,
        __pre_delay.name() : __pre_delay,
        __threshold.name() : __threshold,
        __post_delay.name() : __post_delay,
        __internal_delay.name() : __internal_delay
    }
_Namespace_net.addCategoryObject('typeBinding', u'SynapseInternalProperties', SynapseInternalProperties)


# Complex type LocalSynapticProperties with content type ELEMENT_ONLY
class LocalSynapticProperties (SynapseInternalProperties):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'LocalSynapticProperties')
    # Base type is SynapseInternalProperties
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute prop_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse_type'), 'synapse_type', '__httpmorphml_orgnetworkmlschema_LocalSynapticProperties_synapse_type', pyxb.binding.datatypes.string)
    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, u"Optional for a single synaptic connection. Only needed in the case where multiple synapses are \n                            present at one connection and there are non default values for each synapse's weights, etc. This field gives the \n                            name of the synapse type referred to.")

    
    # Attribute weight inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute threshold inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute post_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute pre_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute internal_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties

    _ElementMap = SynapseInternalProperties._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = SynapseInternalProperties._AttributeMap.copy()
    _AttributeMap.update({
        __synapse_type.name() : __synapse_type
    })
_Namespace_net.addCategoryObject('typeBinding', u'LocalSynapticProperties', LocalSynapticProperties)


# Complex type Deprecated_HHGate with content type ELEMENT_ONLY
class Deprecated_HHGate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_HHGate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), 'transition', '__httpmorphml_orgchannelmlschema_Deprecated_HHGate_httpmorphml_orgchannelmlschematransition', False)

    
    transition = property(__transition.value, __transition.set, None, None)

    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'state'), 'state', '__httpmorphml_orgchannelmlschema_Deprecated_HHGate_state', pyxb.binding.datatypes.string, required=True)
    
    state = property(__state.value, __state.set, None, None)


    _ElementMap = {
        __transition.name() : __transition
    }
    _AttributeMap = {
        __state.name() : __state
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_HHGate', Deprecated_HHGate)


# Complex type Point with content type EMPTY
class Point (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Point')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute diameter uses Python identifier diameter
    __diameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'diameter'), 'diameter', '__httpmorphml_orgmetadataschema_Point_diameter', pyxb.binding.datatypes.double)
    
    diameter = property(__diameter.value, __diameter.set, None, None)

    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpmorphml_orgmetadataschema_Point_z', pyxb.binding.datatypes.double, required=True)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpmorphml_orgmetadataschema_Point_y', pyxb.binding.datatypes.double, required=True)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpmorphml_orgmetadataschema_Point_x', pyxb.binding.datatypes.double, required=True)
    
    x = property(__x.value, __x.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __diameter.name() : __diameter,
        __z.name() : __z,
        __y.name() : __y,
        __x.name() : __x
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Point', Point)


# Complex type PulseInput with content type EMPTY
class PulseInput (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'PulseInput')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute amplitude uses Python identifier amplitude
    __amplitude = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'amplitude'), 'amplitude', '__httpmorphml_orgnetworkmlschema_PulseInput_amplitude', CurrentValue, required=True)
    
    amplitude = property(__amplitude.value, __amplitude.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duration'), 'duration', '__httpmorphml_orgnetworkmlschema_PulseInput_duration', TimeValue, required=True)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute delay uses Python identifier delay
    __delay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'delay'), 'delay', '__httpmorphml_orgnetworkmlschema_PulseInput_delay', TimeValue, required=True)
    
    delay = property(__delay.value, __delay.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __amplitude.name() : __amplitude,
        __duration.name() : __duration,
        __delay.name() : __delay
    }
_Namespace_net.addCategoryObject('typeBinding', u'PulseInput', PulseInput)


# Complex type Q10Settings with content type EMPTY
class Q10Settings (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Q10Settings')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fixed_q10 uses Python identifier fixed_q10
    __fixed_q10 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed_q10'), 'fixed_q10', '__httpmorphml_orgchannelmlschema_Q10Settings_fixed_q10', pyxb.binding.datatypes.double)
    
    fixed_q10 = property(__fixed_q10.value, __fixed_q10.set, None, u'Q10 factor if the cell is to be run at a different temp than that at which \n                    the alpha and beta were determined. Only one of fixed_q10 or q10_factor should be specified!')

    
    # Attribute q10_factor uses Python identifier q10_factor
    __q10_factor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'q10_factor'), 'q10_factor', '__httpmorphml_orgchannelmlschema_Q10Settings_q10_factor', pyxb.binding.datatypes.double)
    
    q10_factor = property(__q10_factor.value, __q10_factor.set, None, u'Q10 factor if the cell is to be run at a different temp than that at which \n                    the alpha and beta were determined. Only one of fixed_q10 or q10_factor should be specified!')

    
    # Attribute experimental_temp uses Python identifier experimental_temp
    __experimental_temp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'experimental_temp'), 'experimental_temp', '__httpmorphml_orgchannelmlschema_Q10Settings_experimental_temp', TemperatureValue, required=True)
    
    experimental_temp = property(__experimental_temp.value, __experimental_temp.set, None, u'The experimental temperature at which alpha and beta rate \n                    equations were determined were measured')

    
    # Attribute gate uses Python identifier gate
    __gate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gate'), 'gate', '__httpmorphml_orgchannelmlschema_Q10Settings_gate', pyxb.binding.datatypes.string)
    
    gate = property(__gate.value, __gate.set, None, u'The gate to which the Q10 adjustment should be applied. If this attribute is not present, assume the adjustment applies at all gates.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fixed_q10.name() : __fixed_q10,
        __q10_factor.name() : __q10_factor,
        __experimental_temp.name() : __experimental_temp,
        __gate.name() : __gate
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Q10Settings', Q10Settings)


# Complex type Deprecated_RateConstVoltConcDep with content type ELEMENT_ONLY
class Deprecated_RateConstVoltConcDep (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_RateConstVoltConcDep')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}generic uses Python identifier generic
    __generic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic'), 'generic', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstVoltConcDep_httpmorphml_orgchannelmlschemageneric', False)

    
    generic = property(__generic.value, __generic.set, None, u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0')

    
    # Element {http://morphml.org/channelml/schema}generic_equation_hh uses Python identifier generic_equation_hh
    __generic_equation_hh = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh'), 'generic_equation_hh', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstVoltConcDep_httpmorphml_orgchannelmlschemageneric_equation_hh', False)

    
    generic_equation_hh = property(__generic_equation_hh.value, __generic_equation_hh.set, None, u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0')


    _ElementMap = {
        __generic.name() : __generic,
        __generic_equation_hh.name() : __generic_equation_hh
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_RateConstVoltConcDep', Deprecated_RateConstVoltConcDep)


# Complex type RandomStimInstance with content type EMPTY
class RandomStimInstance (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'RandomStimInstance')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute frequency uses Python identifier frequency
    __frequency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'frequency'), 'frequency', '__httpmorphml_orgnetworkmlschema_RandomStimInstance_frequency', FrequencyValue, required=True)
    
    frequency = property(__frequency.value, __frequency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __frequency.name() : __frequency
    }
_Namespace_net.addCategoryObject('typeBinding', u'RandomStimInstance', RandomStimInstance)


# Complex type Offset with content type EMPTY
class Offset (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Offset')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgchannelmlschema_Offset_value', VoltageValue, required=True)
    
    value_ = property(__value.value, __value.set, None, u'Offset introduced to alter voltage dependence of \n                rate equations, see NEURON/GENESIS mappings for details')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Offset', Offset)


# Complex type RandomStim with content type EMPTY
class RandomStim (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'RandomStim')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute synaptic_mechanism uses Python identifier synaptic_mechanism
    __synaptic_mechanism = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synaptic_mechanism'), 'synaptic_mechanism', '__httpmorphml_orgnetworkmlschema_RandomStim_synaptic_mechanism', pyxb.binding.datatypes.string, required=True)
    
    synaptic_mechanism = property(__synaptic_mechanism.value, __synaptic_mechanism.set, None, u"The name of a synaptic mechanism which will provides the conductance change.\n                        This will be fired once every 'spike' at the given frequency")

    
    # Attribute frequency uses Python identifier frequency
    __frequency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'frequency'), 'frequency', '__httpmorphml_orgnetworkmlschema_RandomStim_frequency', FrequencyValue, required=True)
    
    frequency = property(__frequency.value, __frequency.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __synaptic_mechanism.name() : __synaptic_mechanism,
        __frequency.name() : __frequency
    }
_Namespace_net.addCategoryObject('typeBinding', u'RandomStim', RandomStim)


# Complex type ChannelML with content type ELEMENT_ONLY
class ChannelML (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ChannelML')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}ion_concentration uses Python identifier ion_concentration
    __ion_concentration = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_concentration'), 'ion_concentration', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgchannelmlschemaion_concentration', True)

    
    ion_concentration = property(__ion_concentration.value, __ion_concentration.set, None, u'Specification of how an ion concentration alters with time, e.g. calcium dynamics. This may influence other\n                   channels (e.g. Ca dependent K channels), and other mechanisms may have a contribution to the concentration of the ion specified here\n                   (e.g. a channel transmitting calcium).')

    
    # Element {http://morphml.org/channelml/schema}ion uses Python identifier ion
    __ion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion'), 'ion', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgchannelmlschemaion', True)

    
    ion = property(__ion.value, __ion.set, None, u'One or more ions which play some role in the mechanism, e.g. transmitted by the channel, alters the rate, etc. Note: deprecated since v1.7.3')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}channel_type uses Python identifier channel_type
    __channel_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'channel_type'), 'channel_type', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgchannelmlschemachannel_type', True)

    
    channel_type = property(__channel_type.value, __channel_type.set, None, u'Specification of a voltage or ligand gated membrane conductance mechanism')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'synapse_type'), 'synapse_type', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgchannelmlschemasynapse_type', True)

    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, u'Specification of a synaptic conductance, triggered by a presynaptic event')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_ChannelML_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__httpmorphml_orgchannelmlschema_ChannelML_units', Units, required=True)
    
    units = property(__units.value, __units.set, None, u'Unit system of all quantities. Only SI or Physiological units are allowed!')


    _ElementMap = {
        __ion_concentration.name() : __ion_concentration,
        __ion.name() : __ion,
        __properties.name() : __properties,
        __channel_type.name() : __channel_type,
        __annotation.name() : __annotation,
        __synapse_type.name() : __synapse_type,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        __units.name() : __units
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ChannelML', ChannelML)


# Complex type CTD_ANON_2 with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute max_v uses Python identifier max_v
    __max_v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_v'), 'max_v', '__httpmorphml_orgchannelmlschema_CTD_ANON_max_v', pyxb.binding.datatypes.double, unicode_default=u'70')
    
    max_v = property(__max_v.value, __max_v.set, None, u'The maximum potential from which to calculate the tables of rate values')

    
    # Attribute table_divisions uses Python identifier table_divisions
    __table_divisions = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'table_divisions'), 'table_divisions', '__httpmorphml_orgchannelmlschema_CTD_ANON_table_divisions', pyxb.binding.datatypes.positiveInteger, unicode_default=u'200')
    
    table_divisions = property(__table_divisions.value, __table_divisions.set, None, u'The number of divisions in the table')

    
    # Attribute min_v uses Python identifier min_v
    __min_v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'min_v'), 'min_v', '__httpmorphml_orgchannelmlschema_CTD_ANON_min_v', pyxb.binding.datatypes.double, unicode_default=u'-100')
    
    min_v = property(__min_v.value, __min_v.set, None, u'The minimum potential from which to calculate the tables of rate values')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __max_v.name() : __max_v,
        __table_divisions.name() : __table_divisions,
        __min_v.name() : __min_v
    }



# Complex type Populations with content type ELEMENT_ONLY
class Populations (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Populations')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Populations_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Populations_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Populations_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Populations_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}population uses Python identifier population
    __population = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'population'), 'population', '__httpmorphml_orgnetworkmlschema_Populations_httpmorphml_orgnetworkmlschemapopulation', True)

    
    population = property(__population.value, __population.set, None, None)


    _ElementMap = {
        __group.name() : __group,
        __notes.name() : __notes,
        __annotation.name() : __annotation,
        __properties.name() : __properties,
        __population.name() : __population
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'Populations', Populations)


# Complex type Authors with content type ELEMENT_ONLY
class Authors (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Authors')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}modelTranslator uses Python identifier modelTranslator
    __modelTranslator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelTranslator'), 'modelTranslator', '__httpmorphml_orgmetadataschema_Authors_httpmorphml_orgmetadataschemamodelTranslator', True)

    
    modelTranslator = property(__modelTranslator.value, __modelTranslator.set, None, u'Person who translated the model to NeuroML')

    
    # Element {http://morphml.org/metadata/schema}modelAuthor uses Python identifier modelAuthor
    __modelAuthor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelAuthor'), 'modelAuthor', '__httpmorphml_orgmetadataschema_Authors_httpmorphml_orgmetadataschemamodelAuthor', True)

    
    modelAuthor = property(__modelAuthor.value, __modelAuthor.set, None, u'Author of the original model')


    _ElementMap = {
        __modelTranslator.name() : __modelTranslator,
        __modelAuthor.name() : __modelAuthor
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Authors', Authors)


# Complex type Projections with content type ELEMENT_ONLY
class Projections (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Projections')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Projections_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Projections_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}projection uses Python identifier projection
    __projection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'projection'), 'projection', '__httpmorphml_orgnetworkmlschema_Projections_httpmorphml_orgnetworkmlschemaprojection', True)

    
    projection = property(__projection.value, __projection.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Projections_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Projections_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__httpmorphml_orgnetworkmlschema_Projections_units', Units, required=True)
    
    units = property(__units.value, __units.set, None, u'Unit system of all quantities in the projection descriptions, e.g. synaptic time constants')


    _ElementMap = {
        __group.name() : __group,
        __notes.name() : __notes,
        __projection.name() : __projection,
        __properties.name() : __properties,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __units.name() : __units
    }
_Namespace_net.addCategoryObject('typeBinding', u'Projections', Projections)


# Complex type Deprecated_GenericEquation with content type EMPTY
class Deprecated_GenericEquation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_GenericEquation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_Deprecated_GenericEquation_expr', pyxb.binding.datatypes.string, required=True)
    
    expr = property(__expr.value, __expr.set, None, u"Note: only variable allowed in expression is v (or for an expression for tau or inf,\n                alpha and beta can be used too). Also, liberal use of brackets, e.g. 5.0*(exp (-50*(v +46))) instead \n                of 5.0* exp (-50*(v +46)) is advised, due to GENESIS's handling of exp, abs, etc. ")


    _ElementMap = {
        
    }
    _AttributeMap = {
        __expr.name() : __expr
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_GenericEquation', Deprecated_GenericEquation)


# Complex type Inputs with content type ELEMENT_ONLY
class Inputs (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Inputs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Inputs_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Inputs_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}input uses Python identifier input
    __input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'input'), 'input', '__httpmorphml_orgnetworkmlschema_Inputs_httpmorphml_orgnetworkmlschemainput', True)

    
    input = property(__input.value, __input.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Inputs_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Inputs_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__httpmorphml_orgnetworkmlschema_Inputs_units', Units, required=True)
    
    units = property(__units.value, __units.set, None, u'Unit system of all quantities in the input description, e.g. input current amplitudes')


    _ElementMap = {
        __notes.name() : __notes,
        __annotation.name() : __annotation,
        __input.name() : __input,
        __properties.name() : __properties,
        __group.name() : __group
    }
    _AttributeMap = {
        __units.name() : __units
    }
_Namespace_net.addCategoryObject('typeBinding', u'Inputs', Inputs)


# Complex type NeuroMLLevel3 with content type ELEMENT_ONLY
class NeuroMLLevel3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, u'NeuroMLLevel3')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}neuroMorphoRef uses Python identifier neuroMorphoRef
    __neuroMorphoRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), 'neuroMorphoRef', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemaneuroMorphoRef', True)

    
    neuroMorphoRef = property(__neuroMorphoRef.value, __neuroMorphoRef.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), 'publication', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemapublication', True)

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}inputs uses Python identifier inputs
    __inputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs'), 'inputs', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgnetworkmlschemainputs', False)

    
    inputs = property(__inputs.value, __inputs.set, None, u'No inputs need be specified')

    
    # Element {http://morphml.org/networkml/schema}populations uses Python identifier populations
    __populations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'populations'), 'populations', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgnetworkmlschemapopulations', False)

    
    populations = property(__populations.value, __populations.set, None, u"The least that's needed in a network is a population of cells...")

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/neuroml/schema}cells uses Python identifier cells
    __cells = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace, u'cells'), 'cells', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgneuromlschemacells', False)

    
    cells = property(__cells.value, __cells.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}neuronDBref uses Python identifier neuronDBref
    __neuronDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), 'neuronDBref', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemaneuronDBref', True)

    
    neuronDBref = property(__neuronDBref.value, __neuronDBref.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}projections uses Python identifier projections
    __projections = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'projections'), 'projections', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgnetworkmlschemaprojections', False)

    
    projections = property(__projections.value, __projections.set, None, u'In theory there can be no projections, if the file is intended only to specify positions')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelDBref uses Python identifier modelDBref
    __modelDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), 'modelDBref', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemamodelDBref', True)

    
    modelDBref = property(__modelDBref.value, __modelDBref.set, None, None)

    
    # Element {http://morphml.org/neuroml/schema}channels uses Python identifier channels
    __channels = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace, u'channels'), 'channels', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgneuromlschemachannels', False)

    
    channels = property(__channels.value, __channels.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), 'authorList', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemaauthorList', False)

    
    authorList = property(__authorList.value, __authorList.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lengthUnits'), 'lengthUnits', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_lengthUnits', LengthUnits)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute length_units uses Python identifier length_units
    __length_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length_units'), 'length_units', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_length_units', LengthUnits)
    
    length_units = property(__length_units.value, __length_units.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')

    
    # Attribute volumeUnits uses Python identifier volumeUnits
    __volumeUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'volumeUnits'), 'volumeUnits', '__httpmorphml_orgneuromlschema_NeuroMLLevel3_volumeUnits', VolumeUnits, unicode_default=u'cubic_millimeter')
    
    volumeUnits = property(__volumeUnits.value, __volumeUnits.set, None, u'Unit of all volume measurements.')


    _ElementMap = {
        __neuroMorphoRef.name() : __neuroMorphoRef,
        __publication.name() : __publication,
        __inputs.name() : __inputs,
        __populations.name() : __populations,
        __notes.name() : __notes,
        __cells.name() : __cells,
        __neuronDBref.name() : __neuronDBref,
        __projections.name() : __projections,
        __properties.name() : __properties,
        __group.name() : __group,
        __modelDBref.name() : __modelDBref,
        __channels.name() : __channels,
        __authorList.name() : __authorList,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __lengthUnits.name() : __lengthUnits,
        __name.name() : __name,
        __length_units.name() : __length_units,
        __volumeUnits.name() : __volumeUnits
    }
_Namespace.addCategoryObject('typeBinding', u'NeuroMLLevel3', NeuroMLLevel3)


# Complex type Initialisation with content type EMPTY
class Initialisation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Initialisation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgchannelmlschema_Initialisation_value', pyxb.binding.datatypes.string, required=True)
    
    value_ = property(__value.value, __value.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Initialisation', Initialisation)


# Complex type FacDep with content type EMPTY
class FacDep (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'FacDep')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tau_fac uses Python identifier tau_fac
    __tau_fac = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_fac'), 'tau_fac', '__httpmorphml_orgchannelmlschema_FacDep_tau_fac', TimeConstantValueIncZero, required=True)
    
    tau_fac = property(__tau_fac.value, __tau_fac.set, None, None)

    
    # Attribute tau_rec uses Python identifier tau_rec
    __tau_rec = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_rec'), 'tau_rec', '__httpmorphml_orgchannelmlschema_FacDep_tau_rec', TimeConstantValueIncZero, required=True)
    
    tau_rec = property(__tau_rec.value, __tau_rec.set, None, None)

    
    # Attribute init_release_prob uses Python identifier init_release_prob
    __init_release_prob = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'init_release_prob'), 'init_release_prob', '__httpmorphml_orgchannelmlschema_FacDep_init_release_prob', pyxb.binding.datatypes.double, required=True)
    
    init_release_prob = property(__init_release_prob.value, __init_release_prob.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __tau_fac.name() : __tau_fac,
        __tau_rec.name() : __tau_rec,
        __init_release_prob.name() : __init_release_prob
    }
_Namespace_cml.addCategoryObject('typeBinding', u'FacDep', FacDep)


# Complex type StdpDep with content type EMPTY
class StdpDep (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'StdpDep')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tau_ltd uses Python identifier tau_ltd
    __tau_ltd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_ltd'), 'tau_ltd', '__httpmorphml_orgchannelmlschema_StdpDep_tau_ltd', TimeConstantValue, required=True)
    
    tau_ltd = property(__tau_ltd.value, __tau_ltd.set, None, None)

    
    # Attribute del_weight_ltd uses Python identifier del_weight_ltd
    __del_weight_ltd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'del_weight_ltd'), 'del_weight_ltd', '__httpmorphml_orgchannelmlschema_StdpDep_del_weight_ltd', pyxb.binding.datatypes.double, required=True)
    
    del_weight_ltd = property(__del_weight_ltd.value, __del_weight_ltd.set, None, None)

    
    # Attribute max_syn_weight uses Python identifier max_syn_weight
    __max_syn_weight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_syn_weight'), 'max_syn_weight', '__httpmorphml_orgchannelmlschema_StdpDep_max_syn_weight', pyxb.binding.datatypes.double, required=True)
    
    max_syn_weight = property(__max_syn_weight.value, __max_syn_weight.set, None, None)

    
    # Attribute tau_ltp uses Python identifier tau_ltp
    __tau_ltp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tau_ltp'), 'tau_ltp', '__httpmorphml_orgchannelmlschema_StdpDep_tau_ltp', TimeConstantValue, required=True)
    
    tau_ltp = property(__tau_ltp.value, __tau_ltp.set, None, None)

    
    # Attribute post_spike_thresh uses Python identifier post_spike_thresh
    __post_spike_thresh = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'post_spike_thresh'), 'post_spike_thresh', '__httpmorphml_orgchannelmlschema_StdpDep_post_spike_thresh', VoltageValue, required=True)
    
    post_spike_thresh = property(__post_spike_thresh.value, __post_spike_thresh.set, None, None)

    
    # Attribute del_weight_ltp uses Python identifier del_weight_ltp
    __del_weight_ltp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'del_weight_ltp'), 'del_weight_ltp', '__httpmorphml_orgchannelmlschema_StdpDep_del_weight_ltp', pyxb.binding.datatypes.double, required=True)
    
    del_weight_ltp = property(__del_weight_ltp.value, __del_weight_ltp.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __tau_ltd.name() : __tau_ltd,
        __del_weight_ltd.name() : __del_weight_ltd,
        __max_syn_weight.name() : __max_syn_weight,
        __tau_ltp.name() : __tau_ltp,
        __post_spike_thresh.name() : __post_spike_thresh,
        __del_weight_ltp.name() : __del_weight_ltp
    }
_Namespace_cml.addCategoryObject('typeBinding', u'StdpDep', StdpDep)


# Complex type CTD_ANON_3 with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_4 with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgmorphmlschema_CTD_ANON_id', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    id = property(__id.value, __id.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id
    }



# Complex type Level3Cells with content type ELEMENT_ONLY
class Level3Cells (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, u'Level3Cells')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/neuroml/schema}cell uses Python identifier cell
    __cell = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace, u'cell'), 'cell', '__httpmorphml_orgneuromlschema_Level3Cells_httpmorphml_orgneuromlschemacell', True)

    
    cell = property(__cell.value, __cell.set, None, u'A single cell specified in MorphML extended to include channel density info.')


    _ElementMap = {
        __cell.name() : __cell
    }
    _AttributeMap = {
        
    }
_Namespace.addCategoryObject('typeBinding', u'Level3Cells', Level3Cells)


# Complex type Transition with content type EMPTY
class Transition (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Transition')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpmorphml_orgchannelmlschema_Transition_scale', pyxb.binding.datatypes.string)
    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpmorphml_orgchannelmlschema_Transition_rate', pyxb.binding.datatypes.string)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpmorphml_orgchannelmlschema_Transition_midpoint', pyxb.binding.datatypes.string)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_Transition_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Short name to use to refer to the transition, e.g. alpha, beta for forward, backward rates in HH gates')

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpmorphml_orgchannelmlschema_Transition_from', pyxb.binding.datatypes.string, required=True)
    
    from_ = property(__from.value, __from.set, None, u'Source state of the transition in kinetic scheme. ')

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpmorphml_orgchannelmlschema_Transition_to', pyxb.binding.datatypes.string, required=True)
    
    to = property(__to.value, __to.set, None, u'Target state of the transition in kinetic scheme. ')

    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_Transition_expr', pyxb.binding.datatypes.string)
    
    expr = property(__expr.value, __expr.set, None, None)

    
    # Attribute expr_form uses Python identifier expr_form
    __expr_form = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr_form'), 'expr_form', '__httpmorphml_orgchannelmlschema_Transition_expr_form', CoreEquationType, required=True)
    
    expr_form = property(__expr_form.value, __expr_form.set, None, u'Form of expression')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __scale.name() : __scale,
        __rate.name() : __rate,
        __midpoint.name() : __midpoint,
        __name.name() : __name,
        __from.name() : __from,
        __to.name() : __to,
        __expr.name() : __expr,
        __expr_form.name() : __expr_form
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Transition', Transition)


# Complex type PerCellConnection with content type EMPTY
class PerCellConnection (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'PerCellConnection')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute max_per_target uses Python identifier max_per_target
    __max_per_target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_per_target'), 'max_per_target', '__httpmorphml_orgnetworkmlschema_PerCellConnection_max_per_target', pyxb.binding.datatypes.positiveInteger)
    
    max_per_target = property(__max_per_target.value, __max_per_target.set, None, None)

    
    # Attribute num_per_source uses Python identifier num_per_source
    __num_per_source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'num_per_source'), 'num_per_source', '__httpmorphml_orgnetworkmlschema_PerCellConnection_num_per_source', PositiveDouble, required=True)
    
    num_per_source = property(__num_per_source.value, __num_per_source.set, None, None)

    
    # Attribute direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'direction'), 'direction', '__httpmorphml_orgnetworkmlschema_PerCellConnection_direction', STD_ANON, unicode_default=u'PreToPost')
    
    direction = property(__direction.value, __direction.set, None, u'Whether the settings below (e.g. number per source cell) refer to PreToPost or PostToPre connections.\n                        Note more info could be known about numbers of connections on post synaptic cells, so this possibility should be allowed.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __max_per_target.name() : __max_per_target,
        __num_per_source.name() : __num_per_source,
        __direction.name() : __direction
    }
_Namespace_net.addCategoryObject('typeBinding', u'PerCellConnection', PerCellConnection)


# Complex type FixedPoolInfo with content type ELEMENT_ONLY
class FixedPoolInfo (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'FixedPoolInfo')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}phi uses Python identifier phi
    __phi = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'phi'), 'phi', '__httpmorphml_orgchannelmlschema_FixedPoolInfo_httpmorphml_orgchannelmlschemaphi', False)

    
    phi = property(__phi.value, __phi.set, None, None)


    _ElementMap = {
        __phi.name() : __phi
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'FixedPoolInfo', FixedPoolInfo)


# Complex type CTD_ANON_5 with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }



# Complex type Cell with content type ELEMENT_ONLY
class Cell (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Cell')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}freePoints uses Python identifier freePoints
    __freePoints = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints'), 'freePoints', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemafreePoints', False)

    
    freePoints = property(__freePoints.value, __freePoints.set, None, u'The collection of varicosities or synaptic connections.')

    
    # Element {http://morphml.org/morphml/schema}cellBody uses Python identifier cellBody
    __cellBody = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cellBody'), 'cellBody', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemacellBody', False)

    
    cellBody = property(__cellBody.value, __cellBody.set, None, u'Used for anatomical representation of the soma. Use a Segment with equivalent properties to retain connectivity of branches to the soma for downstream applications (e.g. neuronal simulators).')

    
    # Element {http://morphml.org/metadata/schema}neuronDBref uses Python identifier neuronDBref
    __neuronDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), 'neuronDBref', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemaneuronDBref', True)

    
    neuronDBref = property(__neuronDBref.value, __neuronDBref.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}segments uses Python identifier segments
    __segments = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'segments'), 'segments', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemasegments', False)

    
    segments = property(__segments.value, __segments.set, None, u'A segment defines the smallest unit within a possibly branching structure, such as a dendrite or axon. The first segment should represent the soma, if needed for downstream applications.')

    
    # Element {http://morphml.org/metadata/schema}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), 'authorList', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemaauthorList', False)

    
    authorList = property(__authorList.value, __authorList.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelDBref uses Python identifier modelDBref
    __modelDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), 'modelDBref', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemamodelDBref', True)

    
    modelDBref = property(__modelDBref.value, __modelDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}cables uses Python identifier cables
    __cables = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cables'), 'cables', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemacables', False)

    
    cables = property(__cables.value, __cables.set, None, u'The collection of cables. Each cable will be associated with a number of connected segments.')

    
    # Element {http://morphml.org/metadata/schema}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), 'publication', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemapublication', True)

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}status uses Python identifier status
    __status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'status'), 'status', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemastatus', False)

    
    status = property(__status.value, __status.set, None, u'Status of the cell model: stable, in progress, etc.\n                    Further test comments explaining the current status should be added.')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}neuroMorphoRef uses Python identifier neuroMorphoRef
    __neuroMorphoRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), 'neuroMorphoRef', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemaneuroMorphoRef', True)

    
    neuroMorphoRef = property(__neuroMorphoRef.value, __neuroMorphoRef.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}spines uses Python identifier spines
    __spines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'spines'), 'spines', '__httpmorphml_orgmorphmlschema_Cell_httpmorphml_orgmorphmlschemaspines', False)

    
    spines = property(__spines.value, __spines.set, None, u'The collection of spines.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_Cell_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __freePoints.name() : __freePoints,
        __cellBody.name() : __cellBody,
        __neuronDBref.name() : __neuronDBref,
        __segments.name() : __segments,
        __authorList.name() : __authorList,
        __properties.name() : __properties,
        __modelDBref.name() : __modelDBref,
        __annotation.name() : __annotation,
        __cables.name() : __cables,
        __publication.name() : __publication,
        __status.name() : __status,
        __group.name() : __group,
        __neuroMorphoRef.name() : __neuroMorphoRef,
        __notes.name() : __notes,
        __spines.name() : __spines
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Cell', Cell)


# Complex type Level3Cell with content type ELEMENT_ONLY
class Level3Cell (Cell):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, u'Level3Cell')
    # Base type is Cell
    
    # Element freePoints ({http://morphml.org/morphml/schema}freePoints) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element cellBody ({http://morphml.org/morphml/schema}cellBody) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element neuronDBref ({http://morphml.org/metadata/schema}neuronDBref) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element segments ({http://morphml.org/morphml/schema}segments) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element {http://morphml.org/neuroml/schema}biophysics uses Python identifier biophysics
    __biophysics = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace, u'biophysics'), 'biophysics', '__httpmorphml_orgneuromlschema_Level3Cell_httpmorphml_orgneuromlschemabiophysics', False)

    
    biophysics = property(__biophysics.value, __biophysics.set, None, None)

    
    # Element authorList ({http://morphml.org/metadata/schema}authorList) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element modelDBref ({http://morphml.org/metadata/schema}modelDBref) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element {http://morphml.org/neuroml/schema}connectivity uses Python identifier connectivity
    __connectivity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace, u'connectivity'), 'connectivity', '__httpmorphml_orgneuromlschema_Level3Cell_httpmorphml_orgneuromlschemaconnectivity', False)

    
    connectivity = property(__connectivity.value, __connectivity.set, None, u'Note: from v1.7.1 the preferred way to specify a potential synaptic location \n                                is with a potential_syn_loc element under connectivity under cell, as opposed to the potentialSynapticLocation \n                                under biophysics under cell. The former will be the only option from v2.0')

    
    # Element cables ({http://morphml.org/morphml/schema}cables) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element publication ({http://morphml.org/metadata/schema}publication) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element status ({http://morphml.org/morphml/schema}status) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element neuroMorphoRef ({http://morphml.org/metadata/schema}neuroMorphoRef) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Element spines ({http://morphml.org/morphml/schema}spines) inherited from {http://morphml.org/morphml/schema}Cell
    
    # Attribute name inherited from {http://morphml.org/morphml/schema}Cell

    _ElementMap = Cell._ElementMap.copy()
    _ElementMap.update({
        __biophysics.name() : __biophysics,
        __connectivity.name() : __connectivity
    })
    _AttributeMap = Cell._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace.addCategoryObject('typeBinding', u'Level3Cell', Level3Cell)


# Complex type NamedParameter with content type ELEMENT_ONLY
class NamedParameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'NamedParameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), 'group', '__httpmorphml_orgbiophysicsschema_NamedParameter_httpmorphml_orgbiophysicsschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgbiophysicsschema_NamedParameter_value', pyxb.binding.datatypes.double, required=True)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgbiophysicsschema_NamedParameter_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'2 names have special meaning: gmax for the maximum conductance density, and e for the reversal potential of a passive channel')


    _ElementMap = {
        __group.name() : __group
    }
    _AttributeMap = {
        __value.name() : __value,
        __name.name() : __name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'NamedParameter', NamedParameter)


# Complex type Biophysics with content type ELEMENT_ONLY
class Biophysics (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'Biophysics')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}mechanism uses Python identifier mechanism
    __mechanism = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'mechanism'), 'mechanism', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemamechanism', True)

    
    mechanism = property(__mechanism.value, __mechanism.set, None, u'Definition of placement of a single electrophysiological mechanism (e.g. channel mechanism)\n                        on a group of cables of a cell. Note there should be at least one of these to specify the passive membrane conductance.\n                        Note: elements spec_capacitance, spec_axial_resistance, ion_props etc. should be used in preference to specificCapacitance etc!')

    
    # Element {http://morphml.org/biophysics/schema}spec_capacitance uses Python identifier spec_capacitance
    __spec_capacitance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_capacitance'), 'spec_capacitance', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaspec_capacitance', False)

    
    spec_capacitance = property(__spec_capacitance.value, __spec_capacitance.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}initialMembPotential uses Python identifier initialMembPotential
    __initialMembPotential = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'initialMembPotential'), 'initialMembPotential', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemainitialMembPotential', False)

    
    initialMembPotential = property(__initialMembPotential.value, __initialMembPotential.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}init_memb_potential uses Python identifier init_memb_potential
    __init_memb_potential = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'init_memb_potential'), 'init_memb_potential', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemainit_memb_potential', False)

    
    init_memb_potential = property(__init_memb_potential.value, __init_memb_potential.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}spec_axial_resistance uses Python identifier spec_axial_resistance
    __spec_axial_resistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_axial_resistance'), 'spec_axial_resistance', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaspec_axial_resistance', False)

    
    spec_axial_resistance = property(__spec_axial_resistance.value, __spec_axial_resistance.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}ion_props uses Python identifier ion_props
    __ion_props = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'ion_props'), 'ion_props', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaion_props', True)

    
    ion_props = property(__ion_props.value, __ion_props.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}specificAxialResistance uses Python identifier specificAxialResistance
    __specificAxialResistance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificAxialResistance'), 'specificAxialResistance', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaspecificAxialResistance', False)

    
    specificAxialResistance = property(__specificAxialResistance.value, __specificAxialResistance.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}specificCapacitance uses Python identifier specificCapacitance
    __specificCapacitance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificCapacitance'), 'specificCapacitance', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaspecificCapacitance', False)

    
    specificCapacitance = property(__specificCapacitance.value, __specificCapacitance.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}ionProperties uses Python identifier ionProperties
    __ionProperties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'ionProperties'), 'ionProperties', '__httpmorphml_orgbiophysicsschema_Biophysics_httpmorphml_orgbiophysicsschemaionProperties', False)

    
    ionProperties = property(__ionProperties.value, __ionProperties.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__httpmorphml_orgbiophysicsschema_Biophysics_units', Units, required=True)
    
    units = property(__units.value, __units.set, None, u'Unit system of all quantities.')


    _ElementMap = {
        __mechanism.name() : __mechanism,
        __spec_capacitance.name() : __spec_capacitance,
        __initialMembPotential.name() : __initialMembPotential,
        __init_memb_potential.name() : __init_memb_potential,
        __spec_axial_resistance.name() : __spec_axial_resistance,
        __ion_props.name() : __ion_props,
        __specificAxialResistance.name() : __specificAxialResistance,
        __specificCapacitance.name() : __specificCapacitance,
        __ionProperties.name() : __ionProperties
    }
    _AttributeMap = {
        __units.name() : __units
    }
_Namespace_bio.addCategoryObject('typeBinding', u'Biophysics', Biophysics)


# Complex type Level3Biophysics with content type ELEMENT_ONLY
class Level3Biophysics (Biophysics):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace, u'Level3Biophysics')
    # Base type is Biophysics
    
    # Element mechanism ({http://morphml.org/biophysics/schema}mechanism) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element spec_capacitance ({http://morphml.org/biophysics/schema}spec_capacitance) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element {http://morphml.org/networkml/schema}potentialSynapticLocation uses Python identifier potentialSynapticLocation
    __potentialSynapticLocation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'potentialSynapticLocation'), 'potentialSynapticLocation', '__httpmorphml_orgneuromlschema_Level3Biophysics_httpmorphml_orgnetworkmlschemapotentialSynapticLocation', True)

    
    potentialSynapticLocation = property(__potentialSynapticLocation.value, __potentialSynapticLocation.set, None, None)

    
    # Element init_memb_potential ({http://morphml.org/biophysics/schema}init_memb_potential) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element spec_axial_resistance ({http://morphml.org/biophysics/schema}spec_axial_resistance) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element initialMembPotential ({http://morphml.org/biophysics/schema}initialMembPotential) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element specificAxialResistance ({http://morphml.org/biophysics/schema}specificAxialResistance) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element ion_props ({http://morphml.org/biophysics/schema}ion_props) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element specificCapacitance ({http://morphml.org/biophysics/schema}specificCapacitance) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Element ionProperties ({http://morphml.org/biophysics/schema}ionProperties) inherited from {http://morphml.org/biophysics/schema}Biophysics
    
    # Attribute units inherited from {http://morphml.org/biophysics/schema}Biophysics

    _ElementMap = Biophysics._ElementMap.copy()
    _ElementMap.update({
        __potentialSynapticLocation.name() : __potentialSynapticLocation
    })
    _AttributeMap = Biophysics._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace.addCategoryObject('typeBinding', u'Level3Biophysics', Level3Biophysics)


# Complex type Level3Connectivity with content type ELEMENT_ONLY
class Level3Connectivity (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Level3Connectivity')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}potential_syn_loc uses Python identifier potential_syn_loc
    __potential_syn_loc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'potential_syn_loc'), 'potential_syn_loc', '__httpmorphml_orgnetworkmlschema_Level3Connectivity_httpmorphml_orgnetworkmlschemapotential_syn_loc', True)

    
    potential_syn_loc = property(__potential_syn_loc.value, __potential_syn_loc.set, None, None)


    _ElementMap = {
        __potential_syn_loc.name() : __potential_syn_loc
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'Level3Connectivity', Level3Connectivity)


# Complex type CTD_ANON_6 with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute translationStart uses Python identifier translationStart
    __translationStart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'translationStart'), 'translationStart', '__httpmorphml_orgmorphmlschema_CTD_ANON__translationStart', pyxb.binding.datatypes.double, required=True)
    
    translationStart = property(__translationStart.value, __translationStart.set, None, u'The variable is translated to this value at the proximal point')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __translationStart.name() : __translationStart
    }



# Complex type Connection with content type ELEMENT_ONLY
class Connection (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Connection')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}post uses Python identifier post
    __post = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'post'), 'post', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgnetworkmlschemapost', False)

    
    post = property(__post.value, __post.set, None, u'NOTE: Attributes post_cell_id etc. for WILL BE PREFERRED FORMAT IN v2.0')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}properties uses Python identifier properties_
    __properties_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'properties'), 'properties_', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgnetworkmlschemaproperties', True)

    
    properties_ = property(__properties_.value, __properties_.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}pre uses Python identifier pre
    __pre = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'pre'), 'pre', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgnetworkmlschemapre', False)

    
    pre = property(__pre.value, __pre.set, None, u'NOTE: Attributes pre_cell_id etc. for WILL BE PREFERRED FORMAT IN v2.0')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Connection_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Attribute post_fraction_along uses Python identifier post_fraction_along
    __post_fraction_along = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'post_fraction_along'), 'post_fraction_along', '__httpmorphml_orgnetworkmlschema_Connection_post_fraction_along', ZeroToOne, unicode_default=u'0.5')
    
    post_fraction_along = property(__post_fraction_along.value, __post_fraction_along.set, None, u'The fraction along the length of the specified segment on the postsynaptic cell where the synapse is located.\n                        Attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute pre_fraction_along uses Python identifier pre_fraction_along
    __pre_fraction_along = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'pre_fraction_along'), 'pre_fraction_along', '__httpmorphml_orgnetworkmlschema_Connection_pre_fraction_along', ZeroToOne, unicode_default=u'0.5')
    
    pre_fraction_along = property(__pre_fraction_along.value, __pre_fraction_along.set, None, u'The fraction along the length of the specified segment on the presynaptic cell where the synapse is located.\n                        Attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute post_cell_id uses Python identifier post_cell_id
    __post_cell_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'post_cell_id'), 'post_cell_id', '__httpmorphml_orgnetworkmlschema_Connection_post_cell_id', pyxb.binding.datatypes.integer)
    
    post_cell_id = property(__post_cell_id.value, __post_cell_id.set, None, u'The ID of the postsynaptic cell. Must be listed in populations, so that too must list instances.\n                        Optional now, but attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute pre_cell_id uses Python identifier pre_cell_id
    __pre_cell_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'pre_cell_id'), 'pre_cell_id', '__httpmorphml_orgnetworkmlschema_Connection_pre_cell_id', pyxb.binding.datatypes.integer)
    
    pre_cell_id = property(__pre_cell_id.value, __pre_cell_id.set, None, u'The ID of the presynaptic cell. Must be listed in populations, so that too must list instances.\n                        Optional now, but attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgnetworkmlschema_Connection_id', pyxb.binding.datatypes.integer, required=True)
    
    id = property(__id.value, __id.set, None, u'The unique ID of the single synaptic connection.')

    
    # Attribute pre_segment_id uses Python identifier pre_segment_id
    __pre_segment_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'pre_segment_id'), 'pre_segment_id', '__httpmorphml_orgnetworkmlschema_Connection_pre_segment_id', pyxb.binding.datatypes.integer, unicode_default=u'0')
    
    pre_segment_id = property(__pre_segment_id.value, __pre_segment_id.set, None, u'The segment on the presynaptic cell where the synapse is located.\n                        Attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute post_segment_id uses Python identifier post_segment_id
    __post_segment_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'post_segment_id'), 'post_segment_id', '__httpmorphml_orgnetworkmlschema_Connection_post_segment_id', pyxb.binding.datatypes.integer, unicode_default=u'0')
    
    post_segment_id = property(__post_segment_id.value, __post_segment_id.set, None, u'The segment on the postsynaptic cell where the synapse is located.\n                        Attributes pre_cell_id, etc. WILL BE PREFERRED FORMAT IN v2.0')


    _ElementMap = {
        __post.name() : __post,
        __annotation.name() : __annotation,
        __properties_.name() : __properties_,
        __group.name() : __group,
        __notes.name() : __notes,
        __pre.name() : __pre,
        __properties.name() : __properties
    }
    _AttributeMap = {
        __post_fraction_along.name() : __post_fraction_along,
        __pre_fraction_along.name() : __pre_fraction_along,
        __post_cell_id.name() : __post_cell_id,
        __pre_cell_id.name() : __pre_cell_id,
        __id.name() : __id,
        __pre_segment_id.name() : __pre_segment_id,
        __post_segment_id.name() : __post_segment_id
    }
_Namespace_net.addCategoryObject('typeBinding', u'Connection', Connection)


# Complex type InputSite with content type ELEMENT_ONLY
class InputSite (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'InputSite')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}random_stim_instance uses Python identifier random_stim_instance
    __random_stim_instance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim_instance'), 'random_stim_instance', '__httpmorphml_orgnetworkmlschema_InputSite_httpmorphml_orgnetworkmlschemarandom_stim_instance', False)

    
    random_stim_instance = property(__random_stim_instance.value, __random_stim_instance.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}pulse_input_instance uses Python identifier pulse_input_instance
    __pulse_input_instance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input_instance'), 'pulse_input_instance', '__httpmorphml_orgnetworkmlschema_InputSite_httpmorphml_orgnetworkmlschemapulse_input_instance', False)

    
    pulse_input_instance = property(__pulse_input_instance.value, __pulse_input_instance.set, None, None)

    
    # Attribute cell_id uses Python identifier cell_id
    __cell_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cell_id'), 'cell_id', '__httpmorphml_orgnetworkmlschema_InputSite_cell_id', CellIdInNetwork, required=True)
    
    cell_id = property(__cell_id.value, __cell_id.set, None, None)

    
    # Attribute fraction_along uses Python identifier fraction_along
    __fraction_along = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fraction_along'), 'fraction_along', '__httpmorphml_orgnetworkmlschema_InputSite_fraction_along', ZeroToOne, unicode_default=u'0.5')
    
    fraction_along = property(__fraction_along.value, __fraction_along.set, None, None)

    
    # Attribute segment_id uses Python identifier segment_id
    __segment_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment_id'), 'segment_id', '__httpmorphml_orgnetworkmlschema_InputSite_segment_id', SegmentIdInCell, unicode_default=u'0')
    
    segment_id = property(__segment_id.value, __segment_id.set, None, None)


    _ElementMap = {
        __random_stim_instance.name() : __random_stim_instance,
        __pulse_input_instance.name() : __pulse_input_instance
    }
    _AttributeMap = {
        __cell_id.name() : __cell_id,
        __fraction_along.name() : __fraction_along,
        __segment_id.name() : __segment_id
    }
_Namespace_net.addCategoryObject('typeBinding', u'InputSite', InputSite)


# Complex type Points with content type ELEMENT_ONLY
class Points (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Points')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}point uses Python identifier point
    __point = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'point'), 'point', '__httpmorphml_orgmetadataschema_Points_httpmorphml_orgmetadataschemapoint', True)

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmetadataschema_Points_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __point.name() : __point
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Points', Points)


# Complex type FreePoints with content type ELEMENT_ONLY
class FreePoints (Points):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'FreePoints')
    # Base type is Points
    
    # Element point ({http://morphml.org/metadata/schema}point) inherited from {http://morphml.org/metadata/schema}Points
    
    # Attribute name inherited from {http://morphml.org/metadata/schema}Points

    _ElementMap = Points._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Points._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_mml.addCategoryObject('typeBinding', u'FreePoints', FreePoints)


# Complex type PotentialSynapticLocation with content type ELEMENT_ONLY
class PotentialSynapticLocation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'PotentialSynapticLocation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}synapse_direction uses Python identifier synapse_direction
    __synapse_direction = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_direction'), 'synapse_direction', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgnetworkmlschemasynapse_direction', False)

    
    synapse_direction = property(__synapse_direction.value, __synapse_direction.set, None, u'Whether this synapse location allows a presynaptic connection, a postsynaptic\n                                connection or either')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}group uses Python identifier group_
    __group_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'group'), 'group_', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgnetworkmlschemagroup', True)

    
    group_ = property(__group_.value, __group_.set, None, u'List of groups of sections allowing the synapse')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), 'synapse_type', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgnetworkmlschemasynapse_type', False)

    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, u'Which of the synaptic mechanisms can be present')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_PotentialSynapticLocation_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)


    _ElementMap = {
        __synapse_direction.name() : __synapse_direction,
        __annotation.name() : __annotation,
        __group_.name() : __group_,
        __group.name() : __group,
        __notes.name() : __notes,
        __synapse_type.name() : __synapse_type,
        __properties.name() : __properties
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'PotentialSynapticLocation', PotentialSynapticLocation)


# Complex type CTD_ANON_7 with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute normalizationEnd uses Python identifier normalizationEnd
    __normalizationEnd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'normalizationEnd'), 'normalizationEnd', '__httpmorphml_orgmorphmlschema_CTD_ANON_2_normalizationEnd', pyxb.binding.datatypes.double, required=True)
    
    normalizationEnd = property(__normalizationEnd.value, __normalizationEnd.set, None, u'The variable is normalised so that it has this value at the distal point')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __normalizationEnd.name() : __normalizationEnd
    }



# Complex type Point3D with content type EMPTY
class Point3D (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Point3D')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpmorphml_orgmetadataschema_Point3D_z', pyxb.binding.datatypes.double, required=True)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpmorphml_orgmetadataschema_Point3D_y', pyxb.binding.datatypes.double, required=True)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpmorphml_orgmetadataschema_Point3D_x', pyxb.binding.datatypes.double, required=True)
    
    x = property(__x.value, __x.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __z.name() : __z,
        __y.name() : __y,
        __x.name() : __x
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Point3D', Point3D)


# Complex type Population with content type ELEMENT_ONLY
class Population (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Population')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}cell_type uses Python identifier cell_type
    __cell_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'cell_type'), 'cell_type', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgnetworkmlschemacell_type', False)

    
    cell_type = property(__cell_type.value, __cell_type.set, None, u'The cell type for this population. NOTE: an attribute value for cell_type WILL BE PREFERRED FORMAT IN v2.0. The option for this element will be removed!')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}instances uses Python identifier instances
    __instances = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'instances'), 'instances', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgnetworkmlschemainstances', False)

    
    instances = property(__instances.value, __instances.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}pop_location uses Python identifier pop_location
    __pop_location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'pop_location'), 'pop_location', '__httpmorphml_orgnetworkmlschema_Population_httpmorphml_orgnetworkmlschemapop_location', False)

    
    pop_location = property(__pop_location.value, __pop_location.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgnetworkmlschema_Population_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'The name of the population')

    
    # Attribute cell_type uses Python identifier cell_type_
    __cell_type_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cell_type'), 'cell_type_', '__httpmorphml_orgnetworkmlschema_Population_cell_type', pyxb.binding.datatypes.string)
    
    cell_type_ = property(__cell_type_.value, __cell_type_.set, None, u'The cell type for this population. Optional now, but WILL BE PREFERRED FORMAT IN v2.0')


    _ElementMap = {
        __cell_type.name() : __cell_type,
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __instances.name() : __instances,
        __properties.name() : __properties,
        __pop_location.name() : __pop_location
    }
    _AttributeMap = {
        __name.name() : __name,
        __cell_type_.name() : __cell_type_
    }
_Namespace_net.addCategoryObject('typeBinding', u'Population', Population)


# Complex type Projection with content type ELEMENT_ONLY
class Projection (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Projection')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}connections uses Python identifier connections
    __connections = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'connections'), 'connections', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgnetworkmlschemaconnections', False)

    
    connections = property(__connections.value, __connections.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}target uses Python identifier target
    __target = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'target'), 'target', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgnetworkmlschematarget', False)

    
    target = property(__target.value, __target.set, None, u'Cell population where synaptic connection terminates. NOTE: attribute values for source and target WILL BE THE PREFERRED FORMAT IN v2.0. The option for this element will be removed!')

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}connectivity_pattern uses Python identifier connectivity_pattern
    __connectivity_pattern = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'connectivity_pattern'), 'connectivity_pattern', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgnetworkmlschemaconnectivity_pattern', False)

    
    connectivity_pattern = property(__connectivity_pattern.value, __connectivity_pattern.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}synapse_props uses Python identifier synapse_props
    __synapse_props = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_props'), 'synapse_props', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgnetworkmlschemasynapse_props', True)

    
    synapse_props = property(__synapse_props.value, __synapse_props.set, None, u'Properties of a synapse associated with this connection.')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}source uses Python identifier source
    __source = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'source'), 'source', '__httpmorphml_orgnetworkmlschema_Projection_httpmorphml_orgnetworkmlschemasource', False)

    
    source = property(__source.value, __source.set, None, u'Cell population where synaptic connection begins. NOTE: attribute values for source and target WILL BE THE PREFERRED FORMAT IN v2.0. The option for this element will be removed!')

    
    # Attribute source uses Python identifier source_
    __source_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'source'), 'source_', '__httpmorphml_orgnetworkmlschema_Projection_source', pyxb.binding.datatypes.string)
    
    source_ = property(__source_.value, __source_.set, None, u'Cell population where synaptic connection begins. Optional now, but WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute target uses Python identifier target_
    __target_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'target'), 'target_', '__httpmorphml_orgnetworkmlschema_Projection_target', pyxb.binding.datatypes.string)
    
    target_ = property(__target_.value, __target_.set, None, u'Cell population where synaptic connection terminates. Optional now, but WILL BE PREFERRED FORMAT IN v2.0')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgnetworkmlschema_Projection_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'String reference for the projection')


    _ElementMap = {
        __connections.name() : __connections,
        __annotation.name() : __annotation,
        __target.name() : __target,
        __notes.name() : __notes,
        __connectivity_pattern.name() : __connectivity_pattern,
        __group.name() : __group,
        __synapse_props.name() : __synapse_props,
        __properties.name() : __properties,
        __source.name() : __source
    }
    _AttributeMap = {
        __source_.name() : __source_,
        __target_.name() : __target_,
        __name.name() : __name
    }
_Namespace_net.addCategoryObject('typeBinding', u'Projection', Projection)


# Complex type Deprecated_VoltageGate with content type ELEMENT_ONLY
class Deprecated_VoltageGate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_VoltageGate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}inf uses Python identifier inf
    __inf = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf'), 'inf', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemainf', False)

    
    inf = property(__inf.value, __inf.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}gamma uses Python identifier gamma
    __gamma = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma'), 'gamma', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemagamma', False)

    
    gamma = property(__gamma.value, __gamma.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}initialisation uses Python identifier initialisation
    __initialisation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), 'initialisation', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemainitialisation', False)

    
    initialisation = property(__initialisation.value, __initialisation.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}zeta uses Python identifier zeta
    __zeta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta'), 'zeta', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemazeta', False)

    
    zeta = property(__zeta.value, __zeta.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}alpha uses Python identifier alpha
    __alpha = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha'), 'alpha', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemaalpha', False)

    
    alpha = property(__alpha.value, __alpha.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}beta uses Python identifier beta
    __beta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta'), 'beta', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschemabeta', False)

    
    beta = property(__beta.value, __beta.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}tau uses Python identifier tau
    __tau = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau'), 'tau', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageGate_httpmorphml_orgchannelmlschematau', False)

    
    tau = property(__tau.value, __tau.set, None, None)


    _ElementMap = {
        __inf.name() : __inf,
        __gamma.name() : __gamma,
        __initialisation.name() : __initialisation,
        __zeta.name() : __zeta,
        __alpha.name() : __alpha,
        __beta.name() : __beta,
        __tau.name() : __tau
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_VoltageGate', Deprecated_VoltageGate)


# Complex type Input with content type ELEMENT_ONLY
class Input (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Input')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}target uses Python identifier target
    __target = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'target'), 'target', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgnetworkmlschematarget', False)

    
    target = property(__target.value, __target.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}pulse_input uses Python identifier pulse_input
    __pulse_input = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input'), 'pulse_input', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgnetworkmlschemapulse_input', False)

    
    pulse_input = property(__pulse_input.value, __pulse_input.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}random_stim uses Python identifier random_stim
    __random_stim = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim'), 'random_stim', '__httpmorphml_orgnetworkmlschema_Input_httpmorphml_orgnetworkmlschemarandom_stim', False)

    
    random_stim = property(__random_stim.value, __random_stim.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgnetworkmlschema_Input_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __annotation.name() : __annotation,
        __target.name() : __target,
        __group.name() : __group,
        __notes.name() : __notes,
        __pulse_input.name() : __pulse_input,
        __properties.name() : __properties,
        __random_stim.name() : __random_stim
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_net.addCategoryObject('typeBinding', u'Input', Input)


# Complex type CTD_ANON_8 with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}cablegroup uses Python identifier cablegroup
    __cablegroup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cablegroup'), 'cablegroup', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmorphmlschemacablegroup', True)

    
    cablegroup = property(__cablegroup.value, __cablegroup.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}cable uses Python identifier cable
    __cable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable'), 'cable', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmorphmlschemacable', True)

    
    cable = property(__cable.value, __cable.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_CTD_ANON_3_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)


    _ElementMap = {
        __cablegroup.name() : __cablegroup,
        __properties.name() : __properties,
        __annotation.name() : __annotation,
        __cable.name() : __cable,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        
    }



# Complex type InputTarget with content type ELEMENT_ONLY
class InputTarget (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'InputTarget')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}sites uses Python identifier sites
    __sites = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'sites'), 'sites', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgnetworkmlschemasites', False)

    
    sites = property(__sites.value, __sites.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}site_pattern uses Python identifier site_pattern
    __site_pattern = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'site_pattern'), 'site_pattern', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgnetworkmlschemasite_pattern', False)

    
    site_pattern = property(__site_pattern.value, __site_pattern.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_InputTarget_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute population uses Python identifier population
    __population = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'population'), 'population', '__httpmorphml_orgnetworkmlschema_InputTarget_population', pyxb.binding.datatypes.string)
    
    population = property(__population.value, __population.set, None, u'The cell group to which to apply the stimulation. Note for v2.0 population is the preferred name of this attribute (not cell_group).')

    
    # Attribute cell_group uses Python identifier cell_group
    __cell_group = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cell_group'), 'cell_group', '__httpmorphml_orgnetworkmlschema_InputTarget_cell_group', pyxb.binding.datatypes.string)
    
    cell_group = property(__cell_group.value, __cell_group.set, None, u'The cell group to which to apply the stimulation. Note for v2.0 population is the preferred name of this attribute (not cell_group).')


    _ElementMap = {
        __sites.name() : __sites,
        __properties.name() : __properties,
        __site_pattern.name() : __site_pattern,
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        __population.name() : __population,
        __cell_group.name() : __cell_group
    }
_Namespace_net.addCategoryObject('typeBinding', u'InputTarget', InputTarget)


# Complex type NeuronDBReference with content type ELEMENT_ONLY
class NeuronDBReference (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'NeuronDBReference')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_NeuronDBReference_httpmorphml_orgmetadataschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Comment on how this neuron relates to the current model')

    
    # Element {http://morphml.org/metadata/schema}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), 'uri', '__httpmorphml_orgmetadataschema_NeuronDBReference_httpmorphml_orgmetadataschemauri', False)

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelName uses Python identifier modelName
    __modelName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName'), 'modelName', '__httpmorphml_orgmetadataschema_NeuronDBReference_httpmorphml_orgmetadataschemamodelName', False)

    
    modelName = property(__modelName.value, __modelName.set, None, None)


    _ElementMap = {
        __comment.name() : __comment,
        __uri.name() : __uri,
        __modelName.name() : __modelName
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'NeuronDBReference', NeuronDBReference)


# Complex type ModelDBReference with content type ELEMENT_ONLY
class ModelDBReference (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'ModelDBReference')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), 'uri', '__httpmorphml_orgmetadataschema_ModelDBReference_httpmorphml_orgmetadataschemauri', False)

    
    uri = property(__uri.value, __uri.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelName uses Python identifier modelName
    __modelName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName'), 'modelName', '__httpmorphml_orgmetadataschema_ModelDBReference_httpmorphml_orgmetadataschemamodelName', False)

    
    modelName = property(__modelName.value, __modelName.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_ModelDBReference_httpmorphml_orgmetadataschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Comment on how this model relates to the current model in NeuroML')


    _ElementMap = {
        __uri.name() : __uri,
        __modelName.name() : __modelName,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'ModelDBReference', ModelDBReference)


# Complex type DoubleExponentialSynapse with content type ELEMENT_ONLY
class DoubleExponentialSynapse (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'DoubleExponentialSynapse')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute decay_time uses Python identifier decay_time
    __decay_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decay_time'), 'decay_time', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_decay_time', TimeConstantValue, required=True)
    
    decay_time = property(__decay_time.value, __decay_time.set, None, u'The characteristic decay time of the conductance waveform ')

    
    # Attribute max_conductance uses Python identifier max_conductance
    __max_conductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_conductance'), 'max_conductance', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_max_conductance', ConductanceValue, required=True)
    
    max_conductance = property(__max_conductance.value, __max_conductance.set, None, u'The maximum conductance of the channel')

    
    # Attribute reversal_potential uses Python identifier reversal_potential
    __reversal_potential = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reversal_potential'), 'reversal_potential', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_reversal_potential', VoltageValue, required=True)
    
    reversal_potential = property(__reversal_potential.value, __reversal_potential.set, None, u'The reversal potential of the synapse, which (along with the membrane potential) will determine the current passing through the synapse when the conductance is non zero ')

    
    # Attribute rise_time uses Python identifier rise_time
    __rise_time = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rise_time'), 'rise_time', '__httpmorphml_orgchannelmlschema_DoubleExponentialSynapse_rise_time', TimeConstantValueIncZero, required=True)
    
    rise_time = property(__rise_time.value, __rise_time.set, None, u'The characteristic rise time of the conductance waveform ')


    _ElementMap = {
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __decay_time.name() : __decay_time,
        __max_conductance.name() : __max_conductance,
        __reversal_potential.name() : __reversal_potential,
        __rise_time.name() : __rise_time
    }
_Namespace_cml.addCategoryObject('typeBinding', u'DoubleExponentialSynapse', DoubleExponentialSynapse)


# Complex type BlockingSynapse with content type ELEMENT_ONLY
class BlockingSynapse (DoubleExponentialSynapse):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'BlockingSynapse')
    # Base type is DoubleExponentialSynapse
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element {http://morphml.org/channelml/schema}block uses Python identifier block
    __block = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'block'), 'block', '__httpmorphml_orgchannelmlschema_BlockingSynapse_httpmorphml_orgchannelmlschemablock', False)

    
    block = property(__block.value, __block.set, None, None)

    
    # Attribute decay_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute reversal_potential inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute rise_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse

    _ElementMap = DoubleExponentialSynapse._ElementMap.copy()
    _ElementMap.update({
        __block.name() : __block
    })
    _AttributeMap = DoubleExponentialSynapse._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_cml.addCategoryObject('typeBinding', u'BlockingSynapse', BlockingSynapse)


# Complex type Segment with content type ELEMENT_ONLY
class Segment (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Segment')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_Segment_httpmorphml_orgmorphmlschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, u'Some optional properties associated with the segment.')

    
    # Element {http://morphml.org/morphml/schema}proximal uses Python identifier proximal
    __proximal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), 'proximal', '__httpmorphml_orgmorphmlschema_Segment_httpmorphml_orgmorphmlschemaproximal', False)

    
    proximal = property(__proximal.value, __proximal.set, None, u'The start point (and diameter) of the segment. If absent, it is assumed that the distal point of the parent is the start point of this segment.')

    
    # Element {http://morphml.org/morphml/schema}distal uses Python identifier distal
    __distal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), 'distal', '__httpmorphml_orgmorphmlschema_Segment_httpmorphml_orgmorphmlschemadistal', False)

    
    distal = property(__distal.value, __distal.set, None, u'The end point (and diameter) of the segment. Note if the 3D location of the distal point is the same as the proximal point, the segment is assumed to be spherical.')

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parent'), 'parent', '__httpmorphml_orgmorphmlschema_Segment_parent', SegmentIdInCell)
    
    parent = property(__parent.value, __parent.set, None, u'Used to indicate logical connectivity between segments. Note that there is no requirement that the end point of this parent segment is equal to the start point of this segment.')

    
    # Attribute cable uses Python identifier cable
    __cable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cable'), 'cable', '__httpmorphml_orgmorphmlschema_Segment_cable', pyxb.binding.datatypes.nonNegativeInteger)
    
    cable = property(__cable.value, __cable.set, None, u'The cable ID of which this segment is part. Numerous segments will make up one cable, and it is assumed these are connected electrically.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgmorphmlschema_Segment_id', SegmentIdInCell, required=True)
    
    id = property(__id.value, __id.set, None, u'The ID of the segment, which should be unique within the cell.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_Segment_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, u'As many simulators use a string to identify the compartments, etc. a unique name can be given to the segment.')


    _ElementMap = {
        __properties.name() : __properties,
        __proximal.name() : __proximal,
        __distal.name() : __distal
    }
    _AttributeMap = {
        __parent.name() : __parent,
        __cable.name() : __cable,
        __id.name() : __id,
        __name.name() : __name
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Segment', Segment)


# Complex type Cells with content type ELEMENT_ONLY
class Cells (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Cells')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}cell uses Python identifier cell
    __cell = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cell'), 'cell', '__httpmorphml_orgmorphmlschema_Cells_httpmorphml_orgmorphmlschemacell', True)

    
    cell = property(__cell.value, __cell.set, None, u'A single cell.')


    _ElementMap = {
        __cell.name() : __cell
    }
    _AttributeMap = {
        
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Cells', Cells)


# Complex type ElectricalSynapse with content type ELEMENT_ONLY
class ElectricalSynapse (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ElectricalSynapse')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_ElectricalSynapse_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_ElectricalSynapse_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_ElectricalSynapse_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_ElectricalSynapse_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Attribute conductance uses Python identifier conductance
    __conductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'conductance'), 'conductance', '__httpmorphml_orgchannelmlschema_ElectricalSynapse_conductance', ConductanceValue, required=True)
    
    conductance = property(__conductance.value, __conductance.set, None, u'The conductance of the electrical connection')


    _ElementMap = {
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties
    }
    _AttributeMap = {
        __conductance.name() : __conductance
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ElectricalSynapse', ElectricalSynapse)


# Complex type CellInstance with content type ELEMENT_ONLY
class CellInstance (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'CellInstance')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}location uses Python identifier location
    __location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'location'), 'location', '__httpmorphml_orgnetworkmlschema_CellInstance_httpmorphml_orgnetworkmlschemalocation', False)

    
    location = property(__location.value, __location.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_CellInstance_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_CellInstance_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_CellInstance_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_CellInstance_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgnetworkmlschema_CellInstance_id', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    id = property(__id.value, __id.set, None, u'A unique non negative integer id for the cell instance')

    
    # Attribute node_id uses Python identifier node_id
    __node_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'node_id'), 'node_id', '__httpmorphml_orgnetworkmlschema_CellInstance_node_id', pyxb.binding.datatypes.nonNegativeInteger)
    
    node_id = property(__node_id.value, __node_id.set, None, u'An optional specification of the node id on which this cell should run. This can be used\n                    to allow exchange of neuronal networks partitioned for execution in\n                    distributed computing environments. A parsing appliction can ignore this inforation and create its own partition.')


    _ElementMap = {
        __location.name() : __location,
        __properties.name() : __properties,
        __group.name() : __group,
        __notes.name() : __notes,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __id.name() : __id,
        __node_id.name() : __node_id
    }
_Namespace_net.addCategoryObject('typeBinding', u'CellInstance', CellInstance)


# Complex type MultiDecaySynapse with content type ELEMENT_ONLY
class MultiDecaySynapse (DoubleExponentialSynapse):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'MultiDecaySynapse')
    # Base type is DoubleExponentialSynapse
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance_3 uses Python identifier max_conductance_3
    __max_conductance_3 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_conductance_3'), 'max_conductance_3', '__httpmorphml_orgchannelmlschema_MultiDecaySynapse_max_conductance_3', ConductanceValue)
    
    max_conductance_3 = property(__max_conductance_3.value, __max_conductance_3.set, None, None)

    
    # Attribute decay_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute reversal_potential inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance_2 uses Python identifier max_conductance_2
    __max_conductance_2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'max_conductance_2'), 'max_conductance_2', '__httpmorphml_orgchannelmlschema_MultiDecaySynapse_max_conductance_2', ConductanceValue)
    
    max_conductance_2 = property(__max_conductance_2.value, __max_conductance_2.set, None, None)

    
    # Attribute rise_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute decay_time_2 uses Python identifier decay_time_2
    __decay_time_2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decay_time_2'), 'decay_time_2', '__httpmorphml_orgchannelmlschema_MultiDecaySynapse_decay_time_2', TimeConstantValue)
    
    decay_time_2 = property(__decay_time_2.value, __decay_time_2.set, None, None)

    
    # Attribute decay_time_3 uses Python identifier decay_time_3
    __decay_time_3 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'decay_time_3'), 'decay_time_3', '__httpmorphml_orgchannelmlschema_MultiDecaySynapse_decay_time_3', TimeConstantValue)
    
    decay_time_3 = property(__decay_time_3.value, __decay_time_3.set, None, None)

    
    # Attribute max_conductance inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse

    _ElementMap = DoubleExponentialSynapse._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = DoubleExponentialSynapse._AttributeMap.copy()
    _AttributeMap.update({
        __max_conductance_3.name() : __max_conductance_3,
        __max_conductance_2.name() : __max_conductance_2,
        __decay_time_2.name() : __decay_time_2,
        __decay_time_3.name() : __decay_time_3
    })
_Namespace_cml.addCategoryObject('typeBinding', u'MultiDecaySynapse', MultiDecaySynapse)


# Complex type CableGroup with content type ELEMENT_ONLY
class CableGroup (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'CableGroup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}inhomogeneous_param uses Python identifier inhomogeneous_param
    __inhomogeneous_param = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'inhomogeneous_param'), 'inhomogeneous_param', '__httpmorphml_orgmorphmlschema_CableGroup_httpmorphml_orgmorphmlschemainhomogeneous_param', True)

    
    inhomogeneous_param = property(__inhomogeneous_param.value, __inhomogeneous_param.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}cable uses Python identifier cable
    __cable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable'), 'cable', '__httpmorphml_orgmorphmlschema_CableGroup_httpmorphml_orgmorphmlschemacable', True)

    
    cable = property(__cable.value, __cable.set, None, u'The id of a single cable in the group')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_CableGroup_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name of the cable group')


    _ElementMap = {
        __inhomogeneous_param.name() : __inhomogeneous_param,
        __cable.name() : __cable
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_mml.addCategoryObject('typeBinding', u'CableGroup', CableGroup)


# Complex type CTD_ANON_9 with content type EMPTY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fraction uses Python identifier fraction
    __fraction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fraction'), 'fraction', '__httpmorphml_orgchannelmlschema_CTD_ANON__fraction', ZeroToOne, unicode_default=u'1')
    
    fraction = property(__fraction.value, __fraction.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_CTD_ANON__name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fraction.name() : __fraction,
        __name.name() : __name
    }



# Complex type StdpSynapse with content type ELEMENT_ONLY
class StdpSynapse (MultiDecaySynapse):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'StdpSynapse')
    # Base type is MultiDecaySynapse
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element {http://morphml.org/channelml/schema}spike_time_dep uses Python identifier spike_time_dep
    __spike_time_dep = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'spike_time_dep'), 'spike_time_dep', '__httpmorphml_orgchannelmlschema_StdpSynapse_httpmorphml_orgchannelmlschemaspike_time_dep', False)

    
    spike_time_dep = property(__spike_time_dep.value, __spike_time_dep.set, None, None)

    
    # Attribute max_conductance_3 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute reversal_potential inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute rise_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance_2 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time_2 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time_3 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute max_conductance inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse

    _ElementMap = MultiDecaySynapse._ElementMap.copy()
    _ElementMap.update({
        __spike_time_dep.name() : __spike_time_dep
    })
    _AttributeMap = MultiDecaySynapse._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_cml.addCategoryObject('typeBinding', u'StdpSynapse', StdpSynapse)


# Complex type Cable with content type ELEMENT_ONLY
class Cable (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Cable')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_Cable_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_Cable_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_Cable_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_Cable_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Attribute fract_along_parent uses Python identifier fract_along_parent
    __fract_along_parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fract_along_parent'), 'fract_along_parent', '__httpmorphml_orgmorphmlschema_Cable_fract_along_parent', ZeroToOne)
    
    fract_along_parent = property(__fract_along_parent.value, __fract_along_parent.set, None, u'Connection location of this section\'s proximal point along the parent cable. \n                Normally this could be determined by the 3D points, but this option is needed as many reconstructed neurons have dendrites "floating in space", possibly due to drift\n                of the slice. In this case the fract_along_parent determines electrical connectivity, and it is up to the loading application/its user to decide to ignore the discrepancy, \n                move the dendrite or fill in an extra section.\n                NOTE: this attribute will be required in v2.0!! Don\'t use fractAlongParent anymore.\n            Changed for consistency with ChannelML and NetworkML naming conventions.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgmorphmlschema_Cable_id', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    id = property(__id.value, __id.set, None, u'ID of the cable, unique within this cell')

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parent'), 'parent', '__httpmorphml_orgmorphmlschema_Cable_parent', pyxb.binding.datatypes.nonNegativeInteger)
    
    parent = property(__parent.value, __parent.set, None, u'A cable ID. A way to connect cables logically.')

    
    # Attribute fractAlongParent uses Python identifier fractAlongParent
    __fractAlongParent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fractAlongParent'), 'fractAlongParent', '__httpmorphml_orgmorphmlschema_Cable_fractAlongParent', ZeroToOne)
    
    fractAlongParent = property(__fractAlongParent.value, __fractAlongParent.set, None, u"Approximate location of this section's proximal point along the parent cable. NOTE: this attribute will be removed in v2.0!! Use fract_along_parent instead.\n            Changed for consistency with ChannelML and NetworkML naming conventions.")

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_Cable_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, u'As many simulators use a string to identify the sections, etc. a unique name can be given to the segment.')


    _ElementMap = {
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties
    }
    _AttributeMap = {
        __fract_along_parent.name() : __fract_along_parent,
        __id.name() : __id,
        __parent.name() : __parent,
        __fractAlongParent.name() : __fractAlongParent,
        __name.name() : __name
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Cable', Cable)


# Complex type CTD_ANON_10 with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygon'), 'polygon', '__httpmorphml_orgmetadataschema_CTD_ANON_httpmorphml_orgmetadataschemapolygon', True)

    
    polygon = property(__polygon.value, __polygon.set, None, None)


    _ElementMap = {
        __polygon.name() : __polygon
    }
    _AttributeMap = {
        
    }



# Complex type Polygon with content type ELEMENT_ONLY
class Polygon (Points):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Polygon')
    # Base type is Points
    
    # Element point ({http://morphml.org/metadata/schema}point) inherited from {http://morphml.org/metadata/schema}Points
    
    # Attribute name inherited from {http://morphml.org/metadata/schema}Points

    _ElementMap = Points._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Points._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_meta.addCategoryObject('typeBinding', u'Polygon', Polygon)


# Complex type Polyhedron with content type ELEMENT_ONLY
class Polyhedron (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Polyhedron')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}polygons uses Python identifier polygons
    __polygons = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygons'), 'polygons', '__httpmorphml_orgmetadataschema_Polyhedron_httpmorphml_orgmetadataschemapolygons', False)

    
    polygons = property(__polygons.value, __polygons.set, None, u'Collection of polygons defining the polyhedron.')


    _ElementMap = {
        __polygons.name() : __polygons
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Polyhedron', Polyhedron)


# Complex type Sphere with content type ELEMENT_ONLY
class Sphere (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Sphere')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}center uses Python identifier center
    __center = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'center'), 'center', '__httpmorphml_orgmetadataschema_Sphere_httpmorphml_orgmetadataschemacenter', False)

    
    center = property(__center.value, __center.set, None, u'Diameter of sphere is obtained from center Point.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmetadataschema_Sphere_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __center.name() : __center
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Sphere', Sphere)


# Complex type CTD_ANON_11 with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_CTD_ANON_4_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_CTD_ANON_4_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}spine uses Python identifier spine
    __spine = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'spine'), 'spine', '__httpmorphml_orgmorphmlschema_CTD_ANON_4_httpmorphml_orgmorphmlschemaspine', True)

    
    spine = property(__spine.value, __spine.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_CTD_ANON_4_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_CTD_ANON_4_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)


    _ElementMap = {
        __notes.name() : __notes,
        __properties.name() : __properties,
        __spine.name() : __spine,
        __annotation.name() : __annotation,
        __group.name() : __group
    }
    _AttributeMap = {
        
    }



# Complex type FacDepSynapse with content type ELEMENT_ONLY
class FacDepSynapse (MultiDecaySynapse):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'FacDepSynapse')
    # Base type is MultiDecaySynapse
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element {http://morphml.org/channelml/schema}plasticity uses Python identifier plasticity
    __plasticity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'plasticity'), 'plasticity', '__httpmorphml_orgchannelmlschema_FacDepSynapse_httpmorphml_orgchannelmlschemaplasticity', False)

    
    plasticity = property(__plasticity.value, __plasticity.set, None, None)

    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance_3 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute reversal_potential inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute rise_time inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse
    
    # Attribute max_conductance_2 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time_2 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute decay_time_3 inherited from {http://morphml.org/channelml/schema}MultiDecaySynapse
    
    # Attribute max_conductance inherited from {http://morphml.org/channelml/schema}DoubleExponentialSynapse

    _ElementMap = MultiDecaySynapse._ElementMap.copy()
    _ElementMap.update({
        __plasticity.name() : __plasticity
    })
    _AttributeMap = MultiDecaySynapse._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_cml.addCategoryObject('typeBinding', u'FacDepSynapse', FacDepSynapse)


# Complex type Connections with content type ELEMENT_ONLY
class Connections (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Connections')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Connections_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Connections_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Connections_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}connection uses Python identifier connection
    __connection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'connection'), 'connection', '__httpmorphml_orgnetworkmlschema_Connections_httpmorphml_orgnetworkmlschemaconnection', True)

    
    connection = property(__connection.value, __connection.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Connections_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__httpmorphml_orgnetworkmlschema_Connections_size', pyxb.binding.datatypes.nonNegativeInteger)
    
    size = property(__size.value, __size.set, None, u'The number of instances of connections. \n                    This is redundant information, but can be useful when the file is being parsed to allocate memory for an array of cells. \n                    NOTE: likely to be required from v2.0')


    _ElementMap = {
        __group.name() : __group,
        __annotation.name() : __annotation,
        __notes.name() : __notes,
        __connection.name() : __connection,
        __properties.name() : __properties
    }
    _AttributeMap = {
        __size.name() : __size
    }
_Namespace_net.addCategoryObject('typeBinding', u'Connections', Connections)


# Complex type Deprecated_KSState with content type EMPTY
class Deprecated_KSState (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_KSState')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_Deprecated_KSState_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_KSState', Deprecated_KSState)


# Complex type Deprecated_Transition with content type ELEMENT_ONLY
class Deprecated_Transition (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_Transition')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}voltage_conc_gate uses Python identifier voltage_conc_gate
    __voltage_conc_gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_conc_gate'), 'voltage_conc_gate', '__httpmorphml_orgchannelmlschema_Deprecated_Transition_httpmorphml_orgchannelmlschemavoltage_conc_gate', False)

    
    voltage_conc_gate = property(__voltage_conc_gate.value, __voltage_conc_gate.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}voltage_gate uses Python identifier voltage_gate
    __voltage_gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_gate'), 'voltage_gate', '__httpmorphml_orgchannelmlschema_Deprecated_Transition_httpmorphml_orgchannelmlschemavoltage_gate', False)

    
    voltage_gate = property(__voltage_gate.value, __voltage_gate.set, None, None)

    
    # Attribute source uses Python identifier source
    __source = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'source'), 'source', '__httpmorphml_orgchannelmlschema_Deprecated_Transition_source', pyxb.binding.datatypes.string)
    
    source = property(__source.value, __source.set, None, u'Source state of the transition if used in kinetic scheme. Must be used with attribute target. Use this in preference to src!!!')

    
    # Attribute target uses Python identifier target
    __target = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'target'), 'target', '__httpmorphml_orgchannelmlschema_Deprecated_Transition_target', pyxb.binding.datatypes.string)
    
    target = property(__target.value, __target.set, None, u'Target state of the transition if used in kinetic scheme. Must be used with attribute src')


    _ElementMap = {
        __voltage_conc_gate.name() : __voltage_conc_gate,
        __voltage_gate.name() : __voltage_gate
    }
    _AttributeMap = {
        __source.name() : __source,
        __target.name() : __target
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_Transition', Deprecated_Transition)


# Complex type SynapseProperties with content type ELEMENT_ONLY
class SynapseProperties (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'SynapseProperties')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}default_values uses Python identifier default_values
    __default_values = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values'), 'default_values', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgnetworkmlschemadefault_values', False)

    
    default_values = property(__default_values.value, __default_values.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), 'synapse_type', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgnetworkmlschemasynapse_type', False)

    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_SynapseProperties_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)


    _ElementMap = {
        __properties.name() : __properties,
        __default_values.name() : __default_values,
        __annotation.name() : __annotation,
        __synapse_type.name() : __synapse_type,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'SynapseProperties', SynapseProperties)


# Complex type IonProperties with content type ELEMENT_ONLY
class IonProperties (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'IonProperties')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), 'parameter', '__httpmorphml_orgbiophysicsschema_IonProperties_httpmorphml_orgbiophysicsschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgbiophysicsschema_IonProperties_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __parameter.name() : __parameter
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'IonProperties', IonProperties)


# Complex type SpecCapacitance with content type ELEMENT_ONLY
class SpecCapacitance (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'SpecCapacitance')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), 'variableParameter', '__httpmorphml_orgbiophysicsschema_SpecCapacitance_httpmorphml_orgbiophysicsschemavariableParameter', True)

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')

    
    # Element {http://morphml.org/biophysics/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), 'parameter', '__httpmorphml_orgbiophysicsschema_SpecCapacitance_httpmorphml_orgbiophysicsschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}variable_parameter uses Python identifier variable_parameter
    __variable_parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), 'variable_parameter', '__httpmorphml_orgbiophysicsschema_SpecCapacitance_httpmorphml_orgbiophysicsschemavariable_parameter', True)

    
    variable_parameter = property(__variable_parameter.value, __variable_parameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')


    _ElementMap = {
        __variableParameter.name() : __variableParameter,
        __parameter.name() : __parameter,
        __variable_parameter.name() : __variable_parameter
    }
    _AttributeMap = {
        
    }
_Namespace_bio.addCategoryObject('typeBinding', u'SpecCapacitance', SpecCapacitance)


# Complex type Block with content type EMPTY
class Block (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Block')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute eta uses Python identifier eta
    __eta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'eta'), 'eta', '__httpmorphml_orgchannelmlschema_Block_eta', pyxb.binding.datatypes.double, required=True)
    
    eta = property(__eta.value, __eta.set, None, u'Used in multiplicative factor for total conductance: 1/(1 + eta * [conc] * exp(-1* gamma * V))')

    
    # Attribute gamma uses Python identifier gamma
    __gamma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'gamma'), 'gamma', '__httpmorphml_orgchannelmlschema_Block_gamma', pyxb.binding.datatypes.double, required=True)
    
    gamma = property(__gamma.value, __gamma.set, None, u'Used in multiplicative factor for total conductance: 1/(1 + eta * [conc] * exp(-1* gamma * V))')

    
    # Attribute species uses Python identifier species
    __species = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'species'), 'species', '__httpmorphml_orgchannelmlschema_Block_species', pyxb.binding.datatypes.string, required=True)
    
    species = property(__species.value, __species.set, None, u'Name of species. For ions use lowercase, e.g. mg')

    
    # Attribute conc uses Python identifier conc
    __conc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'conc'), 'conc', '__httpmorphml_orgchannelmlschema_Block_conc', ConcentrationValue, required=True)
    
    conc = property(__conc.value, __conc.set, None, u'Concentration of species. Multiplicative factor for total conductance: 1/(1 + eta * [conc] * exp(-1* gamma * V))')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __eta.name() : __eta,
        __gamma.name() : __gamma,
        __species.name() : __species,
        __conc.name() : __conc
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Block', Block)


# Complex type SpecAxialResistance with content type ELEMENT_ONLY
class SpecAxialResistance (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'SpecAxialResistance')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), 'variableParameter', '__httpmorphml_orgbiophysicsschema_SpecAxialResistance_httpmorphml_orgbiophysicsschemavariableParameter', True)

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')

    
    # Element {http://morphml.org/biophysics/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), 'parameter', '__httpmorphml_orgbiophysicsschema_SpecAxialResistance_httpmorphml_orgbiophysicsschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}variable_parameter uses Python identifier variable_parameter
    __variable_parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), 'variable_parameter', '__httpmorphml_orgbiophysicsschema_SpecAxialResistance_httpmorphml_orgbiophysicsschemavariable_parameter', True)

    
    variable_parameter = property(__variable_parameter.value, __variable_parameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')


    _ElementMap = {
        __variableParameter.name() : __variableParameter,
        __parameter.name() : __parameter,
        __variable_parameter.name() : __variable_parameter
    }
    _AttributeMap = {
        
    }
_Namespace_bio.addCategoryObject('typeBinding', u'SpecAxialResistance', SpecAxialResistance)


# Complex type IntegrateAndFire with content type EMPTY
class IntegrateAndFire (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'IntegrateAndFire')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'threshold'), 'threshold', '__httpmorphml_orgchannelmlschema_IntegrateAndFire_threshold', VoltageValue, required=True)
    
    threshold = property(__threshold.value, __threshold.set, None, u'Voltage at which the mechanism causes the segment/cell to fire, i.e. membrane potential will be reset to v_reset')

    
    # Attribute v_reset uses Python identifier v_reset
    __v_reset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v_reset'), 'v_reset', '__httpmorphml_orgchannelmlschema_IntegrateAndFire_v_reset', VoltageValue, required=True)
    
    v_reset = property(__v_reset.value, __v_reset.set, None, u'Membrane potential is reset to this after spiking')

    
    # Attribute g_refrac uses Python identifier g_refrac
    __g_refrac = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'g_refrac'), 'g_refrac', '__httpmorphml_orgchannelmlschema_IntegrateAndFire_g_refrac', ConductanceValue, required=True)
    
    g_refrac = property(__g_refrac.value, __g_refrac.set, None, u'Conductance during the period t_refrac after a spike, when the current due to this mechanism is given by i = g_refrac*(v - v_reset), therefore a high value for g_refrac, e.g. 100 microsiemens, will effectively clamp the cell at v_reset')

    
    # Attribute t_refrac uses Python identifier t_refrac
    __t_refrac = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't_refrac'), 't_refrac', '__httpmorphml_orgchannelmlschema_IntegrateAndFire_t_refrac', TimeValue, required=True)
    
    t_refrac = property(__t_refrac.value, __t_refrac.set, None, u'Time after a spike during which the segment will be clamped to v_reset (clamping current given by i = g_refrac*(v - v_reset))')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __threshold.name() : __threshold,
        __v_reset.name() : __v_reset,
        __g_refrac.name() : __g_refrac,
        __t_refrac.name() : __t_refrac
    }
_Namespace_cml.addCategoryObject('typeBinding', u'IntegrateAndFire', IntegrateAndFire)


# Complex type InitialMembPotential with content type ELEMENT_ONLY
class InitialMembPotential (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'InitialMembPotential')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), 'variableParameter', '__httpmorphml_orgbiophysicsschema_InitialMembPotential_httpmorphml_orgbiophysicsschemavariableParameter', True)

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, None)

    
    # Element {http://morphml.org/biophysics/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), 'parameter', '__httpmorphml_orgbiophysicsschema_InitialMembPotential_httpmorphml_orgbiophysicsschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)


    _ElementMap = {
        __variableParameter.name() : __variableParameter,
        __parameter.name() : __parameter
    }
    _AttributeMap = {
        
    }
_Namespace_bio.addCategoryObject('typeBinding', u'InitialMembPotential', InitialMembPotential)


# Complex type Property with content type ELEMENT_ONLY
class Property (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Property')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}value uses Python identifier value_
    __value = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'value'), 'value_', '__httpmorphml_orgmetadataschema_Property_httpmorphml_orgmetadataschemavalue', False)

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}tag uses Python identifier tag
    __tag = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'tag'), 'tag', '__httpmorphml_orgmetadataschema_Property_httpmorphml_orgmetadataschematag', False)

    
    tag = property(__tag.value, __tag.set, None, None)

    
    # Attribute value uses Python identifier value_2
    __value_2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_2', '__httpmorphml_orgmetadataschema_Property_value', pyxb.binding.datatypes.string)
    
    value_2 = property(__value_2.value, __value_2.set, None, None)

    
    # Attribute tag uses Python identifier tag_
    __tag_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'tag'), 'tag_', '__httpmorphml_orgmetadataschema_Property_tag', pyxb.binding.datatypes.string)
    
    tag_ = property(__tag_.value, __tag_.set, None, None)


    _ElementMap = {
        __value.name() : __value,
        __tag.name() : __tag
    }
    _AttributeMap = {
        __value_2.name() : __value_2,
        __tag_.name() : __tag_
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Property', Property)


# Complex type Publication with content type ELEMENT_ONLY
class Publication (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Publication')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}fullTitle uses Python identifier fullTitle
    __fullTitle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'fullTitle'), 'fullTitle', '__httpmorphml_orgmetadataschema_Publication_httpmorphml_orgmetadataschemafullTitle', False)

    
    fullTitle = property(__fullTitle.value, __fullTitle.set, None, u'A reasonably complete reference to the paper, etc. including journal, authors, issue, year. \n                    Mainly for quick recognition of the paper. The PubMed ref should contain the unique ID.')

    
    # Element {http://morphml.org/metadata/schema}pubmedRef uses Python identifier pubmedRef
    __pubmedRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'pubmedRef'), 'pubmedRef', '__httpmorphml_orgmetadataschema_Publication_httpmorphml_orgmetadataschemapubmedRef', False)

    
    pubmedRef = property(__pubmedRef.value, __pubmedRef.set, None, u'URL of paper in PubMed (starting with http://www.ncbi.nlm.nih.gov)')

    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_Publication_httpmorphml_orgmetadataschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Comment on how this publication relates to the current model')


    _ElementMap = {
        __fullTitle.name() : __fullTitle,
        __pubmedRef.name() : __pubmedRef,
        __comment.name() : __comment
    }
    _AttributeMap = {
        
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Publication', Publication)


# Complex type RateAdjustments with content type ELEMENT_ONLY
class RateAdjustments (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'RateAdjustments')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset'), 'offset', '__httpmorphml_orgchannelmlschema_RateAdjustments_httpmorphml_orgchannelmlschemaoffset', False)

    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}q10_settings uses Python identifier q10_settings
    __q10_settings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings'), 'q10_settings', '__httpmorphml_orgchannelmlschema_RateAdjustments_httpmorphml_orgchannelmlschemaq10_settings', True)

    
    q10_settings = property(__q10_settings.value, __q10_settings.set, None, None)


    _ElementMap = {
        __offset.name() : __offset,
        __q10_settings.name() : __q10_settings
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'RateAdjustments', RateAdjustments)


# Complex type PoolVolumeInfo with content type ELEMENT_ONLY
class PoolVolumeInfo (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'PoolVolumeInfo')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}shell_thickness uses Python identifier shell_thickness
    __shell_thickness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'shell_thickness'), 'shell_thickness', '__httpmorphml_orgchannelmlschema_PoolVolumeInfo_httpmorphml_orgchannelmlschemashell_thickness', False)

    
    shell_thickness = property(__shell_thickness.value, __shell_thickness.set, None, u'The volume of the pool is calculated from the thickness of the shell inside\n                    the membrane. This will have to be multiplied by the surface area of the relevant compartment. NOTE: In v2.0 the option for \n                    a shell_thickness element will be removed. Attribute shell_thickness will be used instead.')

    
    # Attribute shell_thickness uses Python identifier shell_thickness_
    __shell_thickness_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shell_thickness'), 'shell_thickness_', '__httpmorphml_orgchannelmlschema_PoolVolumeInfo_shell_thickness', LengthValue)
    
    shell_thickness_ = property(__shell_thickness_.value, __shell_thickness_.set, None, u'The volume of the pool is calculated from the thickness of the shell inside\n                    the membrane. This will have to be multiplied by the surface area of the relevant compartment. NOTE: In v2.0 the option for \n                a shell_thickness element will be removed. Attribute shell_thickness will be used instead.')


    _ElementMap = {
        __shell_thickness.name() : __shell_thickness
    }
    _AttributeMap = {
        __shell_thickness_.name() : __shell_thickness_
    }
_Namespace_cml.addCategoryObject('typeBinding', u'PoolVolumeInfo', PoolVolumeInfo)


# Complex type Gate with content type ELEMENT_ONLY
class Gate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Gate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'state'), 'state', '__httpmorphml_orgchannelmlschema_Gate_httpmorphml_orgchannelmlschemastate', True)

    
    state = property(__state.value, __state.set, None, u'Internal state of the gate, specifying a name, and possibly a fractional contribution. \n                    HHGate or KSGate elements will specify the rate equations, etc. for the gate, referencing this state name.')

    
    # Attribute power uses Python identifier power
    __power = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'power'), 'power', '__httpmorphml_orgchannelmlschema_Gate_power', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    power = property(__power.value, __power.set, None, u'The power to which the gate is raised in the expression for the total conductance')


    _ElementMap = {
        __state.name() : __state
    }
    _AttributeMap = {
        __power.name() : __power
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Gate', Gate)


# Complex type CTD_ANON_12 with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}propertyDetail uses Python identifier propertyDetail
    __propertyDetail = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetail'), 'propertyDetail', '__httpmorphml_orgmorphmlschema_CTD_ANON_5_httpmorphml_orgmorphmlschemapropertyDetail', True)

    
    propertyDetail = property(__propertyDetail.value, __propertyDetail.set, None, None)


    _ElementMap = {
        __propertyDetail.name() : __propertyDetail
    }
    _AttributeMap = {
        
    }



# Complex type GlobalSynapticProperties with content type ELEMENT_ONLY
class GlobalSynapticProperties (SynapseInternalProperties):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'GlobalSynapticProperties')
    # Base type is SynapseInternalProperties
    
    # Element group ({http://morphml.org/metadata/schema}group) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element notes ({http://morphml.org/metadata/schema}notes) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element properties ({http://morphml.org/metadata/schema}properties) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Element {http://morphml.org/networkml/schema}default_values uses Python identifier default_values
    __default_values = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values'), 'default_values', '__httpmorphml_orgnetworkmlschema_GlobalSynapticProperties_httpmorphml_orgnetworkmlschemadefault_values', False)

    
    default_values = property(__default_values.value, __default_values.set, None, u'For compatability to pre v1.7.1. Will be removed in v2.0.')

    
    # Element {http://morphml.org/networkml/schema}synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), 'synapse_type', '__httpmorphml_orgnetworkmlschema_GlobalSynapticProperties_httpmorphml_orgnetworkmlschemasynapse_type', False)

    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, u'For compatability to pre v1.7.1. Will be removed in v2.0.')

    
    # Element annotation ({http://morphml.org/metadata/schema}annotation) inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute prop_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute pre_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute weight inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute threshold inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute post_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute internal_delay inherited from {http://morphml.org/networkml/schema}SynapseInternalProperties
    
    # Attribute synapse_type uses Python identifier synapse_type_
    __synapse_type_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse_type'), 'synapse_type_', '__httpmorphml_orgnetworkmlschema_GlobalSynapticProperties_synapse_type', pyxb.binding.datatypes.string)
    
    synapse_type_ = property(__synapse_type_.value, __synapse_type_.set, None, u'Including synapse_type as attribute in synapse_props will be required in v2.0')


    _ElementMap = SynapseInternalProperties._ElementMap.copy()
    _ElementMap.update({
        __default_values.name() : __default_values,
        __synapse_type.name() : __synapse_type
    })
    _AttributeMap = SynapseInternalProperties._AttributeMap.copy()
    _AttributeMap.update({
        __synapse_type_.name() : __synapse_type_
    })
_Namespace_net.addCategoryObject('typeBinding', u'GlobalSynapticProperties', GlobalSynapticProperties)


# Complex type ChannelType with content type ELEMENT_ONLY
class ChannelType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ChannelType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}neuronDBref uses Python identifier neuronDBref
    __neuronDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), 'neuronDBref', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemaneuronDBref', True)

    
    neuronDBref = property(__neuronDBref.value, __neuronDBref.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}hh_gate uses Python identifier hh_gate
    __hh_gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'hh_gate'), 'hh_gate', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemahh_gate', True)

    
    hh_gate = property(__hh_gate.value, __hh_gate.set, None, u'Channel specification based on the Hodgkin Huxley formalism. Deprecated! Will be removed in v2.0')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelDBref uses Python identifier modelDBref
    __modelDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), 'modelDBref', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemamodelDBref', True)

    
    modelDBref = property(__modelDBref.value, __modelDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), 'authorList', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemaauthorList', False)

    
    authorList = property(__authorList.value, __authorList.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameters'), 'parameters', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemaparameters', False)

    
    parameters = property(__parameters.value, __parameters.set, None, u'Fixed value parameters which can be used in generic expressions')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}neuroMorphoRef uses Python identifier neuroMorphoRef
    __neuroMorphoRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), 'neuroMorphoRef', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemaneuroMorphoRef', True)

    
    neuroMorphoRef = property(__neuroMorphoRef.value, __neuroMorphoRef.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), 'publication', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemapublication', True)

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}impl_prefs uses Python identifier impl_prefs
    __impl_prefs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'impl_prefs'), 'impl_prefs', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemaimpl_prefs', False)

    
    impl_prefs = property(__impl_prefs.value, __impl_prefs.set, None, u'Optional recommended values, e.g. for size of tables, when creating an implementation of the \n                    channel mechanism on a specific simulator')

    
    # Element {http://morphml.org/channelml/schema}ks_gate uses Python identifier ks_gate
    __ks_gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ks_gate'), 'ks_gate', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemaks_gate', True)

    
    ks_gate = property(__ks_gate.value, __ks_gate.set, None, u'Channel specification based on a kinetic scheme formalism. Deprecated! Will be removed in v2.0')

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}current_voltage_relation uses Python identifier current_voltage_relation
    __current_voltage_relation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'current_voltage_relation'), 'current_voltage_relation', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemacurrent_voltage_relation', False)

    
    current_voltage_relation = property(__current_voltage_relation.value, __current_voltage_relation.set, None, u'The specification of how the current flow etc. into the cell relates to the membrane potential \n                    difference (e.g. Ohmic relationship)')

    
    # Element {http://morphml.org/channelml/schema}status uses Python identifier status
    __status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), 'status', '__httpmorphml_orgchannelmlschema_ChannelType_httpmorphml_orgchannelmlschemastatus', False)

    
    status = property(__status.value, __status.set, None, u'Status of the channel specification: stable, in progress, etc.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_ChannelType_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'A unique name for the channel mechanism')

    
    # Attribute density uses Python identifier density
    __density = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'density'), 'density', '__httpmorphml_orgchannelmlschema_ChannelType_density', YesNo, unicode_default=u'yes')
    
    density = property(__density.value, __density.set, None, u'Is this a specification of conductance per unit area? Note: almost all channel mechanisms to far have been density mechanisms. \n                This attribute is subject to change when use of ChannelML for single channel conductances is supported.')


    _ElementMap = {
        __neuronDBref.name() : __neuronDBref,
        __hh_gate.name() : __hh_gate,
        __properties.name() : __properties,
        __group.name() : __group,
        __modelDBref.name() : __modelDBref,
        __authorList.name() : __authorList,
        __parameters.name() : __parameters,
        __annotation.name() : __annotation,
        __neuroMorphoRef.name() : __neuroMorphoRef,
        __publication.name() : __publication,
        __impl_prefs.name() : __impl_prefs,
        __ks_gate.name() : __ks_gate,
        __notes.name() : __notes,
        __current_voltage_relation.name() : __current_voltage_relation,
        __status.name() : __status
    }
    _AttributeMap = {
        __name.name() : __name,
        __density.name() : __density
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ChannelType', ChannelType)


# Complex type CTD_ANON_13 with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}gate uses Python identifier gate
    __gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate'), 'gate', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgchannelmlschemagate', True)

    
    gate = property(__gate.value, __gate.set, None, u'Voltage/concentration dependent gate')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}rate_adjustments uses Python identifier rate_adjustments
    __rate_adjustments = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'rate_adjustments'), 'rate_adjustments', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgchannelmlschemarate_adjustments', False)

    
    rate_adjustments = property(__rate_adjustments.value, __rate_adjustments.set, None, u'Adjustments, e.g. temperature dependence, to apply to the gating mechanisms')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}conc_factor uses Python identifier conc_factor
    __conc_factor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor'), 'conc_factor', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgchannelmlschemaconc_factor', False)

    
    conc_factor = property(__conc_factor.value, __conc_factor.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute default_gmax uses Python identifier default_gmax
    __default_gmax = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default_gmax'), 'default_gmax', '__httpmorphml_orgchannelmlschema_CTD_ANON_2_default_gmax', ConductanceDensityValue, required=True)
    
    default_gmax = property(__default_gmax.value, __default_gmax.set, None, u'Maximum conductance density of channel')


    _ElementMap = {
        __gate.name() : __gate,
        __properties.name() : __properties,
        __notes.name() : __notes,
        __rate_adjustments.name() : __rate_adjustments,
        __annotation.name() : __annotation,
        __conc_factor.name() : __conc_factor,
        __group.name() : __group
    }
    _AttributeMap = {
        __default_gmax.name() : __default_gmax
    }



# Complex type Deprecated_RateConstantEqn with content type ELEMENT_ONLY
class Deprecated_RateConstantEqn (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_RateConstantEqn')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter'), 'parameter', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqn_httpmorphml_orgchannelmlschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, u'A parameter which is used in the equation')

    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqn_expr', pyxb.binding.datatypes.string)
    
    expr = property(__expr.value, __expr.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqn_type', pyxb.binding.datatypes.string, required=True)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __parameter.name() : __parameter
    }
    _AttributeMap = {
        __expr.name() : __expr,
        __type.name() : __type
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_RateConstantEqn', Deprecated_RateConstantEqn)


# Complex type Deprecated_AkdEquation with content type ELEMENT_ONLY
class Deprecated_AkdEquation (Deprecated_RateConstantEqn):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_AkdEquation')
    # Base type is Deprecated_RateConstantEqn
    
    # Element parameter ({http://morphml.org/channelml/schema}parameter) inherited from {http://morphml.org/channelml/schema}Deprecated_RateConstantEqn
    
    # Attribute type is restricted from parent
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqn_type', Deprecated_CoreEquationType, required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute expr is restricted from parent
    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_Deprecated_RateConstantEqn_expr', pyxb.binding.datatypes.string)
    
    expr = property(__expr.value, __expr.set, None, u"Note: this expression is has been useful to include when the type is, e.g. linoid, to remind users of the form of the equation.\n                        However, it's use should be discouraged, as it could be assumed that changing this attribute can change the form of the equation (as for generic_equation_hh).\n                        It's better to include the form of the equation as a comment, as in the examples. This attribute may be removed in v2.0")


    _ElementMap = Deprecated_RateConstantEqn._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Deprecated_RateConstantEqn._AttributeMap.copy()
    _AttributeMap.update({
        __type.name() : __type,
        __expr.name() : __expr
    })
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_AkdEquation', Deprecated_AkdEquation)


# Complex type CTD_ANON_14 with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon'), 'polygon', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmorphmlschemapolygon', False)

    
    polygon = property(__polygon.value, __polygon.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}polyhedron uses Python identifier polyhedron
    __polyhedron = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron'), 'polyhedron', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmorphmlschemapolyhedron', False)

    
    polyhedron = property(__polyhedron.value, __polyhedron.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere'), 'sphere', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmorphmlschemasphere', False)

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_CTD_ANON_6_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)


    _ElementMap = {
        __group.name() : __group,
        __notes.name() : __notes,
        __polygon.name() : __polygon,
        __properties.name() : __properties,
        __polyhedron.name() : __polyhedron,
        __sphere.name() : __sphere,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        
    }



# Complex type NonSpatialGrid with content type EMPTY
class NonSpatialGrid (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'NonSpatialGrid')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpmorphml_orgmetadataschema_NonSpatialGrid_z', pyxb.binding.datatypes.positiveInteger)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpmorphml_orgmetadataschema_NonSpatialGrid_y', pyxb.binding.datatypes.positiveInteger)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpmorphml_orgmetadataschema_NonSpatialGrid_x', pyxb.binding.datatypes.positiveInteger, required=True)
    
    x = property(__x.value, __x.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __z.name() : __z,
        __y.name() : __y,
        __x.name() : __x
    }
_Namespace_meta.addCategoryObject('typeBinding', u'NonSpatialGrid', NonSpatialGrid)


# Complex type RectangularBox with content type ELEMENT_ONLY
class RectangularBox (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'RectangularBox')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}size uses Python identifier size
    __size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'size'), 'size', '__httpmorphml_orgmetadataschema_RectangularBox_httpmorphml_orgmetadataschemasize', False)

    
    size = property(__size.value, __size.set, None, u'Size of box. Note if width, height or depth is zero, implies a lower dimension box, e.g. 2D plane.')

    
    # Element {http://morphml.org/metadata/schema}corner uses Python identifier corner
    __corner = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'corner'), 'corner', '__httpmorphml_orgmetadataschema_RectangularBox_httpmorphml_orgmetadataschemacorner', False)

    
    corner = property(__corner.value, __corner.set, None, u'Location of vertex with lowest x, y, z coords.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmetadataschema_RectangularBox_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __size.name() : __size,
        __corner.name() : __corner
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_meta.addCategoryObject('typeBinding', u'RectangularBox', RectangularBox)


# Complex type CTD_ANON_15 with content type EMPTY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'z'), 'z', '__httpmorphml_orgnetworkmlschema_CTD_ANON_4_z', pyxb.binding.datatypes.double)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__httpmorphml_orgnetworkmlschema_CTD_ANON_4_y', pyxb.binding.datatypes.double)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__httpmorphml_orgnetworkmlschema_CTD_ANON_4_x', pyxb.binding.datatypes.double)
    
    x = property(__x.value, __x.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __z.name() : __z,
        __y.name() : __y,
        __x.name() : __x
    }



# Complex type ConnectivityPattern with content type ELEMENT_ONLY
class ConnectivityPattern (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'ConnectivityPattern')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}all_to_all uses Python identifier all_to_all
    __all_to_all = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'all_to_all'), 'all_to_all', '__httpmorphml_orgnetworkmlschema_ConnectivityPattern_httpmorphml_orgnetworkmlschemaall_to_all', False)

    
    all_to_all = property(__all_to_all.value, __all_to_all.set, None, u'Connect every pre cell to every post cell')

    
    # Element {http://morphml.org/networkml/schema}per_cell_connection uses Python identifier per_cell_connection
    __per_cell_connection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'per_cell_connection'), 'per_cell_connection', '__httpmorphml_orgnetworkmlschema_ConnectivityPattern_httpmorphml_orgnetworkmlschemaper_cell_connection', False)

    
    per_cell_connection = property(__per_cell_connection.value, __per_cell_connection.set, None, u'Connection built iteratively from each pre (or post) cell based on a number of parameters')

    
    # Element {http://morphml.org/networkml/schema}fixed_probability uses Python identifier fixed_probability
    __fixed_probability = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'fixed_probability'), 'fixed_probability', '__httpmorphml_orgnetworkmlschema_ConnectivityPattern_httpmorphml_orgnetworkmlschemafixed_probability', False)

    
    fixed_probability = property(__fixed_probability.value, __fixed_probability.set, None, u'For each pre - post pair, there is a fixed probability of connection')


    _ElementMap = {
        __all_to_all.name() : __all_to_all,
        __per_cell_connection.name() : __per_cell_connection,
        __fixed_probability.name() : __fixed_probability
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'ConnectivityPattern', ConnectivityPattern)


# Complex type SteadyState with content type EMPTY
class SteadyState (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'SteadyState')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpmorphml_orgchannelmlschema_SteadyState_to', pyxb.binding.datatypes.string, required=True)
    
    to = property(__to.value, __to.set, None, u'Target state of the transition in kinetic scheme. ')

    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_SteadyState_expr', pyxb.binding.datatypes.string)
    
    expr = property(__expr.value, __expr.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpmorphml_orgchannelmlschema_SteadyState_midpoint', pyxb.binding.datatypes.string)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpmorphml_orgchannelmlschema_SteadyState_from', pyxb.binding.datatypes.string, required=True)
    
    from_ = property(__from.value, __from.set, None, u'Source state of the transition in kinetic scheme. ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_SteadyState_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Short name to use to refer to the steady state e.g. inf')

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpmorphml_orgchannelmlschema_SteadyState_scale', pyxb.binding.datatypes.string)
    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Attribute expr_form uses Python identifier expr_form
    __expr_form = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr_form'), 'expr_form', '__httpmorphml_orgchannelmlschema_SteadyState_expr_form', CoreEquationType, required=True)
    
    expr_form = property(__expr_form.value, __expr_form.set, None, u'Form of expression')

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpmorphml_orgchannelmlschema_SteadyState_rate', pyxb.binding.datatypes.string)
    
    rate = property(__rate.value, __rate.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __to.name() : __to,
        __expr.name() : __expr,
        __midpoint.name() : __midpoint,
        __from.name() : __from,
        __name.name() : __name,
        __scale.name() : __scale,
        __expr_form.name() : __expr_form,
        __rate.name() : __rate
    }
_Namespace_cml.addCategoryObject('typeBinding', u'SteadyState', SteadyState)


# Complex type PotentialSynLoc with content type ELEMENT_ONLY
class PotentialSynLoc (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'PotentialSynLoc')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}group uses Python identifier group_
    __group_ = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'group'), 'group_', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_httpmorphml_orgnetworkmlschemagroup', True)

    
    group_ = property(__group_.value, __group_.set, None, u'List of groups of sections allowing the synapse')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Attribute synapse_type uses Python identifier synapse_type
    __synapse_type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse_type'), 'synapse_type', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_synapse_type', pyxb.binding.datatypes.string, required=True)
    
    synapse_type = property(__synapse_type.value, __synapse_type.set, None, u'Which of the synaptic mechanisms can be present')

    
    # Attribute synapse_direction uses Python identifier synapse_direction
    __synapse_direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'synapse_direction'), 'synapse_direction', '__httpmorphml_orgnetworkmlschema_PotentialSynLoc_synapse_direction', SynapseDirection, unicode_default=u'preAndOrPost')
    
    synapse_direction = property(__synapse_direction.value, __synapse_direction.set, None, u'Whether this synapse location allows a presynaptic connection, a postsynaptic\n                        connection or either')


    _ElementMap = {
        __notes.name() : __notes,
        __properties.name() : __properties,
        __group_.name() : __group_,
        __annotation.name() : __annotation,
        __group.name() : __group
    }
    _AttributeMap = {
        __synapse_type.name() : __synapse_type,
        __synapse_direction.name() : __synapse_direction
    }
_Namespace_net.addCategoryObject('typeBinding', u'PotentialSynLoc', PotentialSynLoc)


# Complex type Spine with content type ELEMENT_ONLY
class Spine (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Spine')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}proximal uses Python identifier proximal
    __proximal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), 'proximal', '__httpmorphml_orgmorphmlschema_Spine_httpmorphml_orgmorphmlschemaproximal', False)

    
    proximal = property(__proximal.value, __proximal.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}distal uses Python identifier distal
    __distal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), 'distal', '__httpmorphml_orgmorphmlschema_Spine_httpmorphml_orgmorphmlschemadistal', False)

    
    distal = property(__distal.value, __distal.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'shape'), 'shape', '__httpmorphml_orgmorphmlschema_Spine_shape', SpineShape)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute volume uses Python identifier volume
    __volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'volume'), 'volume', '__httpmorphml_orgmorphmlschema_Spine_volume', pyxb.binding.datatypes.double)
    
    volume = property(__volume.value, __volume.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length'), 'length', '__httpmorphml_orgmorphmlschema_Spine_length', pyxb.binding.datatypes.double)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parent'), 'parent', '__httpmorphml_orgmorphmlschema_Spine_parent', SegmentIdInCell)
    
    parent = property(__parent.value, __parent.set, None, u'The segment with which this spine is associated.')


    _ElementMap = {
        __proximal.name() : __proximal,
        __distal.name() : __distal
    }
    _AttributeMap = {
        __shape.name() : __shape,
        __volume.name() : __volume,
        __length.name() : __length,
        __parent.name() : __parent
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Spine', Spine)


# Complex type Instances with content type ELEMENT_ONLY
class Instances (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'Instances')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_Instances_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_Instances_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_Instances_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_Instances_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}instance uses Python identifier instance
    __instance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'instance'), 'instance', '__httpmorphml_orgnetworkmlschema_Instances_httpmorphml_orgnetworkmlschemainstance', True)

    
    instance = property(__instance.value, __instance.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__httpmorphml_orgnetworkmlschema_Instances_size', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    size = property(__size.value, __size.set, None, u'The number of instances of cells for this population. \n                    This is redundant information, but can be useful when the file is being parsed to allocate memory for an array of cells. \n                    NOTE: required from v1.7.3')


    _ElementMap = {
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties,
        __instance.name() : __instance
    }
    _AttributeMap = {
        __size.name() : __size
    }
_Namespace_net.addCategoryObject('typeBinding', u'Instances', Instances)


# Complex type PopulationLocation with content type ELEMENT_ONLY
class PopulationLocation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'PopulationLocation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}random_arrangement uses Python identifier random_arrangement
    __random_arrangement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'random_arrangement'), 'random_arrangement', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgnetworkmlschemarandom_arrangement', False)

    
    random_arrangement = property(__random_arrangement.value, __random_arrangement.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}grid_arrangement uses Python identifier grid_arrangement
    __grid_arrangement = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'grid_arrangement'), 'grid_arrangement', '__httpmorphml_orgnetworkmlschema_PopulationLocation_httpmorphml_orgnetworkmlschemagrid_arrangement', False)

    
    grid_arrangement = property(__grid_arrangement.value, __grid_arrangement.set, None, None)

    
    # Attribute reference uses Python identifier reference
    __reference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'reference'), 'reference', '__httpmorphml_orgnetworkmlschema_PopulationLocation_reference', pyxb.binding.datatypes.string)
    
    reference = property(__reference.value, __reference.set, None, None)


    _ElementMap = {
        __group.name() : __group,
        __notes.name() : __notes,
        __properties.name() : __properties,
        __random_arrangement.name() : __random_arrangement,
        __annotation.name() : __annotation,
        __grid_arrangement.name() : __grid_arrangement
    }
    _AttributeMap = {
        __reference.name() : __reference
    }
_Namespace_net.addCategoryObject('typeBinding', u'PopulationLocation', PopulationLocation)


# Complex type CTD_ANON_16 with content type EMPTY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute depth uses Python identifier depth
    __depth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'depth'), 'depth', '__httpmorphml_orgmetadataschema_CTD_ANON__depth', pyxb.binding.datatypes.double)
    
    depth = property(__depth.value, __depth.set, None, None)

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'height'), 'height', '__httpmorphml_orgmetadataschema_CTD_ANON__height', pyxb.binding.datatypes.double)
    
    height = property(__height.value, __height.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'width'), 'width', '__httpmorphml_orgmetadataschema_CTD_ANON__width', pyxb.binding.datatypes.double)
    
    width = property(__width.value, __width.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __depth.name() : __depth,
        __height.name() : __height,
        __width.name() : __width
    }



# Complex type Deprecated_Parameter with content type ELEMENT_ONLY
class Deprecated_Parameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_Parameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_value', pyxb.binding.datatypes.double, required=True)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_Deprecated_Parameter_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __properties.name() : __properties,
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        __value.name() : __value,
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_Parameter', Deprecated_Parameter)


# Complex type Deprecated_Ohmic with content type ELEMENT_ONLY
class Deprecated_Ohmic (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_Ohmic')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}conductance uses Python identifier conductance
    __conductance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'conductance'), 'conductance', '__httpmorphml_orgchannelmlschema_Deprecated_Ohmic_httpmorphml_orgchannelmlschemaconductance', False)

    
    conductance = property(__conductance.value, __conductance.set, None, u'Description of the conductance including maximum conductance density and possible (voltage and/or concentration dependent) gating mechanisms')

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpmorphml_orgchannelmlschema_Deprecated_Ohmic_ion', pyxb.binding.datatypes.string)
    
    ion = property(__ion.value, __ion.set, None, u'The ion which will flow due to the conductance. Note this should be already declared in an Ion element at the beginning of the file.')


    _ElementMap = {
        __conductance.name() : __conductance
    }
    _AttributeMap = {
        __ion.name() : __ion
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_Ohmic', Deprecated_Ohmic)


# Complex type Deprecated_Ion with content type ELEMENT_ONLY
class Deprecated_Ion (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_Ion')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Simple name for the ion. Due to the conventions used in NEURON, it is usually best to use \n                the lower case form of the chemical symbol, e.g. na, ca, k')

    
    # Attribute default_erev uses Python identifier default_erev
    __default_erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default_erev'), 'default_erev', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_default_erev', VoltageValue)
    
    default_erev = property(__default_erev.value, __default_erev.set, None, u'Most implementations of these channel mechanisms (e.g. a mod file) will need a value for the\n                reversal potential for the ion which flows through the channel. However, this is a property of the cell, as opposed to the channel.\n                For convenience though, a typical value can be used here, so a pretty self contained script can be produced, but when used in a real cell the\n                actual value for erev must be calculated')

    
    # Attribute charge uses Python identifier charge
    __charge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'charge'), 'charge', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_charge', pyxb.binding.datatypes.positiveInteger, required=True)
    
    charge = property(__charge.value, __charge.set, None, u'Electrical charge of the ion in question')

    
    # Attribute role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__httpmorphml_orgchannelmlschema_Deprecated_Ion_role', Deprecated_IonRole, unicode_default=u'PermeatedSubstance')
    
    role = property(__role.value, __role.set, None, u'What role the ion plays in the dynamics of the channel/cell mechanism')


    _ElementMap = {
        __group.name() : __group,
        __properties.name() : __properties,
        __notes.name() : __notes,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __name.name() : __name,
        __default_erev.name() : __default_erev,
        __charge.name() : __charge,
        __role.name() : __role
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_Ion', Deprecated_Ion)


# Complex type SynapseType with content type ELEMENT_ONLY
class SynapseType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'SynapseType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}neuroMorphoRef uses Python identifier neuroMorphoRef
    __neuroMorphoRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), 'neuroMorphoRef', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemaneuroMorphoRef', True)

    
    neuroMorphoRef = property(__neuroMorphoRef.value, __neuroMorphoRef.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), 'publication', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemapublication', True)

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}electrical_syn uses Python identifier electrical_syn
    __electrical_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'electrical_syn'), 'electrical_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemaelectrical_syn', False)

    
    electrical_syn = property(__electrical_syn.value, __electrical_syn.set, None, u'Electrical synaptic coupling as at a gap junction')

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}multi_decay_syn uses Python identifier multi_decay_syn
    __multi_decay_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'multi_decay_syn'), 'multi_decay_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemamulti_decay_syn', False)

    
    multi_decay_syn = property(__multi_decay_syn.value, __multi_decay_syn.set, None, u'An extension incorporating multiple decay time courses')

    
    # Element {http://morphml.org/channelml/schema}blocking_syn uses Python identifier blocking_syn
    __blocking_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'blocking_syn'), 'blocking_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemablocking_syn', False)

    
    blocking_syn = property(__blocking_syn.value, __blocking_syn.set, None, u'For example NMDA receptor synapses')

    
    # Element {http://morphml.org/channelml/schema}stdp_syn uses Python identifier stdp_syn
    __stdp_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'stdp_syn'), 'stdp_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemastdp_syn', False)

    
    stdp_syn = property(__stdp_syn.value, __stdp_syn.set, None, u'A synaptic mechanism implementing basic Spike Timing Dependent Plasticity based on Song and Abbott, 2001')

    
    # Element {http://morphml.org/metadata/schema}neuronDBref uses Python identifier neuronDBref
    __neuronDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), 'neuronDBref', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemaneuronDBref', True)

    
    neuronDBref = property(__neuronDBref.value, __neuronDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelDBref uses Python identifier modelDBref
    __modelDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), 'modelDBref', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemamodelDBref', True)

    
    modelDBref = property(__modelDBref.value, __modelDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), 'authorList', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemaauthorList', False)

    
    authorList = property(__authorList.value, __authorList.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}status uses Python identifier status
    __status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), 'status', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemastatus', False)

    
    status = property(__status.value, __status.set, None, u'Status of the synapse specification: stable, in progress, etc.')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}fac_dep_syn uses Python identifier fac_dep_syn
    __fac_dep_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'fac_dep_syn'), 'fac_dep_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemafac_dep_syn', False)

    
    fac_dep_syn = property(__fac_dep_syn.value, __fac_dep_syn.set, None, u'A facilitating and depressing synaptic mechanism')

    
    # Element {http://morphml.org/channelml/schema}doub_exp_syn uses Python identifier doub_exp_syn
    __doub_exp_syn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'doub_exp_syn'), 'doub_exp_syn', '__httpmorphml_orgchannelmlschema_SynapseType_httpmorphml_orgchannelmlschemadoub_exp_syn', False)

    
    doub_exp_syn = property(__doub_exp_syn.value, __doub_exp_syn.set, None, u'Synaptic conductance with rise time and decay time')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_SynapseType_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __neuroMorphoRef.name() : __neuroMorphoRef,
        __publication.name() : __publication,
        __properties.name() : __properties,
        __group.name() : __group,
        __electrical_syn.name() : __electrical_syn,
        __notes.name() : __notes,
        __multi_decay_syn.name() : __multi_decay_syn,
        __blocking_syn.name() : __blocking_syn,
        __stdp_syn.name() : __stdp_syn,
        __neuronDBref.name() : __neuronDBref,
        __modelDBref.name() : __modelDBref,
        __authorList.name() : __authorList,
        __status.name() : __status,
        __annotation.name() : __annotation,
        __fac_dep_syn.name() : __fac_dep_syn,
        __doub_exp_syn.name() : __doub_exp_syn
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'SynapseType', SynapseType)


# Complex type IonConcentration with content type ELEMENT_ONLY
class IonConcentration (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'IonConcentration')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}ion_species uses Python identifier ion_species
    __ion_species = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_species'), 'ion_species', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgchannelmlschemaion_species', False)

    
    ion_species = property(__ion_species.value, __ion_species.set, None, u'Which ion is involved in mechanism.')

    
    # Element {http://morphml.org/metadata/schema}publication uses Python identifier publication
    __publication = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), 'publication', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemapublication', True)

    
    publication = property(__publication.value, __publication.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}neuroMorphoRef uses Python identifier neuroMorphoRef
    __neuroMorphoRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), 'neuroMorphoRef', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemaneuroMorphoRef', True)

    
    neuroMorphoRef = property(__neuroMorphoRef.value, __neuroMorphoRef.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}status uses Python identifier status
    __status = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), 'status', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgchannelmlschemastatus', False)

    
    status = property(__status.value, __status.set, None, u'Status of the ion conc mech specification: stable, in progress, etc.')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}decaying_pool_model uses Python identifier decaying_pool_model
    __decaying_pool_model = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'decaying_pool_model'), 'decaying_pool_model', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgchannelmlschemadecaying_pool_model', False)

    
    decaying_pool_model = property(__decaying_pool_model.value, __decaying_pool_model.set, None, u'At present there is only one choice of a model for this process,\n                        more can be added later..')

    
    # Element {http://morphml.org/metadata/schema}neuronDBref uses Python identifier neuronDBref
    __neuronDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), 'neuronDBref', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemaneuronDBref', True)

    
    neuronDBref = property(__neuronDBref.value, __neuronDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}modelDBref uses Python identifier modelDBref
    __modelDBref = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), 'modelDBref', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemamodelDBref', True)

    
    modelDBref = property(__modelDBref.value, __modelDBref.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), 'authorList', '__httpmorphml_orgchannelmlschema_IonConcentration_httpmorphml_orgmetadataschemaauthorList', False)

    
    authorList = property(__authorList.value, __authorList.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_IonConcentration_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'A unique name for this ion concentration mechanism, as opposed to name of the ion used.')


    _ElementMap = {
        __annotation.name() : __annotation,
        __ion_species.name() : __ion_species,
        __publication.name() : __publication,
        __neuroMorphoRef.name() : __neuroMorphoRef,
        __status.name() : __status,
        __group.name() : __group,
        __notes.name() : __notes,
        __decaying_pool_model.name() : __decaying_pool_model,
        __neuronDBref.name() : __neuronDBref,
        __properties.name() : __properties,
        __modelDBref.name() : __modelDBref,
        __authorList.name() : __authorList
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'IonConcentration', IonConcentration)


# Complex type Parameter with content type EMPTY
class Parameter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Parameter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgchannelmlschema_Parameter_value', pyxb.binding.datatypes.double, required=True)
    
    value_ = property(__value.value, __value.set, None, u'The default value for the parameter')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_Parameter_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'A unique name for the parameter')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value,
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Parameter', Parameter)


# Complex type Status with content type ELEMENT_ONLY
class Status (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Status')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'contributor'), 'contributor', '__httpmorphml_orgmetadataschema_Status_httpmorphml_orgmetadataschemacontributor', True)

    
    contributor = property(__contributor.value, __contributor.set, None, u'Who added the comments?')

    
    # Element {http://morphml.org/metadata/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), 'comment', '__httpmorphml_orgmetadataschema_Status_httpmorphml_orgmetadataschemacomment', True)

    
    comment = property(__comment.value, __comment.set, None, u'A comment on the current status. Not necessarily signalling a problem.')

    
    # Element {http://morphml.org/metadata/schema}issue uses Python identifier issue
    __issue = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'issue'), 'issue', '__httpmorphml_orgmetadataschema_Status_httpmorphml_orgmetadataschemaissue', True)

    
    issue = property(__issue.value, __issue.set, None, u'An issue which need addressing')

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgmetadataschema_Status_value', StatusValue)
    
    value_ = property(__value.value, __value.set, None, u'Currently an enum value of status/in progress/etc.')


    _ElementMap = {
        __contributor.name() : __contributor,
        __comment.name() : __comment,
        __issue.name() : __issue
    }
    _AttributeMap = {
        __value.name() : __value
    }
_Namespace_meta.addCategoryObject('typeBinding', u'Status', Status)


# Complex type Deprecated_VoltageConcGate with content type ELEMENT_ONLY
class Deprecated_VoltageConcGate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_VoltageConcGate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}conc_dependence uses Python identifier conc_dependence
    __conc_dependence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence'), 'conc_dependence', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemaconc_dependence', False)

    
    conc_dependence = property(__conc_dependence.value, __conc_dependence.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}alpha uses Python identifier alpha
    __alpha = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha'), 'alpha', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemaalpha', False)

    
    alpha = property(__alpha.value, __alpha.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}zeta uses Python identifier zeta
    __zeta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta'), 'zeta', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemazeta', False)

    
    zeta = property(__zeta.value, __zeta.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}tau uses Python identifier tau
    __tau = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau'), 'tau', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschematau', False)

    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}gamma uses Python identifier gamma
    __gamma = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma'), 'gamma', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemagamma', False)

    
    gamma = property(__gamma.value, __gamma.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}beta uses Python identifier beta
    __beta = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta'), 'beta', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemabeta', False)

    
    beta = property(__beta.value, __beta.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}inf uses Python identifier inf
    __inf = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf'), 'inf', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemainf', False)

    
    inf = property(__inf.value, __inf.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}initialisation uses Python identifier initialisation
    __initialisation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), 'initialisation', '__httpmorphml_orgchannelmlschema_Deprecated_VoltageConcGate_httpmorphml_orgchannelmlschemainitialisation', False)

    
    initialisation = property(__initialisation.value, __initialisation.set, None, None)


    _ElementMap = {
        __conc_dependence.name() : __conc_dependence,
        __alpha.name() : __alpha,
        __zeta.name() : __zeta,
        __tau.name() : __tau,
        __gamma.name() : __gamma,
        __beta.name() : __beta,
        __inf.name() : __inf,
        __initialisation.name() : __initialisation
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_VoltageConcGate', Deprecated_VoltageConcGate)


# Complex type IonSpecies with content type SIMPLE
class IonSpecies (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'IonSpecies')
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_IonSpecies_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_cml.addCategoryObject('typeBinding', u'IonSpecies', IonSpecies)


# Complex type Parameters with content type ELEMENT_ONLY
class Parameters (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Parameters')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter'), 'parameter', '__httpmorphml_orgchannelmlschema_Parameters_httpmorphml_orgchannelmlschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)


    _ElementMap = {
        __parameter.name() : __parameter
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Parameters', Parameters)


# Complex type CurrentVoltageRelation with content type ELEMENT_ONLY
class CurrentVoltageRelation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'CurrentVoltageRelation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}offset uses Python identifier offset
    __offset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset'), 'offset', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaoffset', False)

    
    offset = property(__offset.value, __offset.set, None, u'Preferred location of offset information since v1.7.3. ')

    
    # Element {http://morphml.org/channelml/schema}conc_dependence uses Python identifier conc_dependence
    __conc_dependence = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence'), 'conc_dependence', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaconc_dependence', False)

    
    conc_dependence = property(__conc_dependence.value, __conc_dependence.set, None, u'Preferred location of conc_dependence since v1.7.3. ')

    
    # Element {http://morphml.org/channelml/schema}conc_factor uses Python identifier conc_factor
    __conc_factor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor'), 'conc_factor', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaconc_factor', False)

    
    conc_factor = property(__conc_factor.value, __conc_factor.set, None, u'Preferred location of conc_factor since v1.7.3. ')

    
    # Element {http://morphml.org/channelml/schema}ohmic uses Python identifier ohmic
    __ohmic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'ohmic'), 'ohmic', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaohmic', False)

    
    ohmic = property(__ohmic.value, __ohmic.set, None, u'Deprecated since v1.7.3. Use attribute cond_law and gate elements below this element instead. ')

    
    # Element {http://morphml.org/channelml/schema}gate uses Python identifier gate
    __gate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate'), 'gate', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemagate', True)

    
    gate = property(__gate.value, __gate.set, None, u'Preferred way of expressing gating complexes since v1.7.3. ')

    
    # Element {http://morphml.org/channelml/schema}integrate_and_fire uses Python identifier integrate_and_fire
    __integrate_and_fire = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'integrate_and_fire'), 'integrate_and_fire', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaintegrate_and_fire', False)

    
    integrate_and_fire = property(__integrate_and_fire.value, __integrate_and_fire.set, None, u'Note: use attribute cond_law="integrate_and_fire" and no other attributes here when using this. \n                    Signifies a current which will cause the cell to behave like an integrate and fire neuron')

    
    # Element {http://morphml.org/channelml/schema}q10_settings uses Python identifier q10_settings
    __q10_settings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings'), 'q10_settings', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_httpmorphml_orgchannelmlschemaq10_settings', True)

    
    q10_settings = property(__q10_settings.value, __q10_settings.set, None, u'Preferred location of Q10 information since v1.7.3. ')

    
    # Attribute default_erev uses Python identifier default_erev
    __default_erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default_erev'), 'default_erev', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_default_erev', VoltageValue)
    
    default_erev = property(__default_erev.value, __default_erev.set, None, u'Most implementations of these channel mechanisms (e.g. a mod file) will need a value for the\n                reversal potential for the ion which flows through the channel. However, this is a property of the cell, as opposed to the channel.\n                For convenience though, a typical value can be used here, so a pretty self contained script can be produced, but when used in a real cell the\n                actual value for erev must be calculated')

    
    # Attribute cond_law uses Python identifier cond_law
    __cond_law = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cond_law'), 'cond_law', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_cond_law', ConductanceLaw)
    
    cond_law = property(__cond_law.value, __cond_law.set, None, u'Introduced in v1.7.3 for new format ChannelML. Specifies which type of conductance law to use: ohmic, etc.')

    
    # Attribute charge uses Python identifier charge
    __charge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'charge'), 'charge', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_charge', pyxb.binding.datatypes.positiveInteger)
    
    charge = property(__charge.value, __charge.set, None, u'Electrical charge of the ion in question')

    
    # Attribute ion uses Python identifier ion
    __ion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ion'), 'ion', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_ion', pyxb.binding.datatypes.string)
    
    ion = property(__ion.value, __ion.set, None, u'Introduced in v1.7.3 for new format ChannelML. The ion which will flow due to the conductance. Note this should be already declared in an Ion element at the beginning of the file.')

    
    # Attribute fixed_erev uses Python identifier fixed_erev
    __fixed_erev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixed_erev'), 'fixed_erev', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_fixed_erev', YesNo, unicode_default=u'no')
    
    fixed_erev = property(__fixed_erev.value, __fixed_erev.set, None, u'Flags whether the reversal potential can be influenced from outside the channel (value = no; default)\n                as is normally the case (e.g. a Ca channel whose reversal potential is influenced by a decaying calcium pool), or \n                whether the rev pot remains fixed (just for this channel) at default_erev (value = yes)')

    
    # Attribute default_gmax uses Python identifier default_gmax
    __default_gmax = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default_gmax'), 'default_gmax', '__httpmorphml_orgchannelmlschema_CurrentVoltageRelation_default_gmax', ConductanceDensityValue)
    
    default_gmax = property(__default_gmax.value, __default_gmax.set, None, u'Introduced in v1.7.3 for new format ChannelML. Maximum conductance density of channel. Note this will normally be reset when the channel mechanism is placed on a cell, but it it \n                useful to have a default value here.')


    _ElementMap = {
        __offset.name() : __offset,
        __conc_dependence.name() : __conc_dependence,
        __conc_factor.name() : __conc_factor,
        __ohmic.name() : __ohmic,
        __gate.name() : __gate,
        __integrate_and_fire.name() : __integrate_and_fire,
        __q10_settings.name() : __q10_settings
    }
    _AttributeMap = {
        __default_erev.name() : __default_erev,
        __cond_law.name() : __cond_law,
        __charge.name() : __charge,
        __ion.name() : __ion,
        __fixed_erev.name() : __fixed_erev,
        __default_gmax.name() : __default_gmax
    }
_Namespace_cml.addCategoryObject('typeBinding', u'CurrentVoltageRelation', CurrentVoltageRelation)


# Complex type InputSites with content type ELEMENT_ONLY
class InputSites (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'InputSites')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_InputSites_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}site uses Python identifier site
    __site = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'site'), 'site', '__httpmorphml_orgnetworkmlschema_InputSites_httpmorphml_orgnetworkmlschemasite', True)

    
    site = property(__site.value, __site.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_InputSites_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_InputSites_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_InputSites_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute size uses Python identifier size
    __size = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__httpmorphml_orgnetworkmlschema_InputSites_size', pyxb.binding.datatypes.nonNegativeInteger)
    
    size = property(__size.value, __size.set, None, u'The number of instances of inputs. \n                    This is redundant information, but can be useful when the file is being parsed to allocate memory for an array of cells. \n                    NOTE: likely to be required from v2.0')


    _ElementMap = {
        __properties.name() : __properties,
        __site.name() : __site,
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes
    }
    _AttributeMap = {
        __size.name() : __size
    }
_Namespace_net.addCategoryObject('typeBinding', u'InputSites', InputSites)


# Complex type ClosedState with content type EMPTY
class ClosedState (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ClosedState')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgchannelmlschema_ClosedState_id', pyxb.binding.datatypes.string, required=True)
    
    id = property(__id.value, __id.set, None, u'Id to use in transition elements when specifying this as the from or to state of the transition.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ClosedState', ClosedState)


# Complex type OpenState with content type EMPTY
class OpenState (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'OpenState')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgchannelmlschema_OpenState_id', pyxb.binding.datatypes.string, required=True)
    
    id = property(__id.value, __id.set, None, u'Id to use in transition elements when specifying this as the from or to state of the transition.')

    
    # Attribute fraction uses Python identifier fraction
    __fraction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fraction'), 'fraction', '__httpmorphml_orgchannelmlschema_OpenState_fraction', ZeroToOne, unicode_default=u'1')
    
    fraction = property(__fraction.value, __fraction.set, None, u'The fractional conductance of the gate in this state. Has value 1 if not present')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id,
        __fraction.name() : __fraction
    }
_Namespace_cml.addCategoryObject('typeBinding', u'OpenState', OpenState)


# Complex type ImplementationPrefs with content type ELEMENT_ONLY
class ImplementationPrefs (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'ImplementationPrefs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'comment'), 'comment', '__httpmorphml_orgchannelmlschema_ImplementationPrefs_httpmorphml_orgchannelmlschemacomment', False)

    
    comment = property(__comment.value, __comment.set, None, u'Comment element to give explination for the implementation preferences. Having a dedicated element as opposed to a <-- comment --> allows the comment to be repeated in the script file impl. ')

    
    # Element {http://morphml.org/channelml/schema}table_settings uses Python identifier table_settings
    __table_settings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'table_settings'), 'table_settings', '__httpmorphml_orgchannelmlschema_ImplementationPrefs_httpmorphml_orgchannelmlschematable_settings', False)

    
    table_settings = property(__table_settings.value, __table_settings.set, None, u'Preferences for the table of values for the rate equations, e.g. used in the TABLE statement in NMODL, or in tabchannel GENESIS objects')


    _ElementMap = {
        __comment.name() : __comment,
        __table_settings.name() : __table_settings
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'ImplementationPrefs', ImplementationPrefs)


# Complex type TimeCourse with content type EMPTY
class TimeCourse (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'TimeCourse')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'from'), 'from_', '__httpmorphml_orgchannelmlschema_TimeCourse_from', pyxb.binding.datatypes.string, required=True)
    
    from_ = property(__from.value, __from.set, None, u'Source state of the transition in kinetic scheme. ')

    
    # Attribute scale uses Python identifier scale
    __scale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'scale'), 'scale', '__httpmorphml_orgchannelmlschema_TimeCourse_scale', pyxb.binding.datatypes.string)
    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgchannelmlschema_TimeCourse_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Short name to use to refer to the time course e.g. tau')

    
    # Attribute expr uses Python identifier expr
    __expr = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr'), 'expr', '__httpmorphml_orgchannelmlschema_TimeCourse_expr', pyxb.binding.datatypes.string)
    
    expr = property(__expr.value, __expr.set, None, None)

    
    # Attribute midpoint uses Python identifier midpoint
    __midpoint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'midpoint'), 'midpoint', '__httpmorphml_orgchannelmlschema_TimeCourse_midpoint', pyxb.binding.datatypes.string)
    
    midpoint = property(__midpoint.value, __midpoint.set, None, None)

    
    # Attribute rate uses Python identifier rate
    __rate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rate'), 'rate', '__httpmorphml_orgchannelmlschema_TimeCourse_rate', pyxb.binding.datatypes.string)
    
    rate = property(__rate.value, __rate.set, None, None)

    
    # Attribute expr_form uses Python identifier expr_form
    __expr_form = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'expr_form'), 'expr_form', '__httpmorphml_orgchannelmlschema_TimeCourse_expr_form', CoreEquationType, required=True)
    
    expr_form = property(__expr_form.value, __expr_form.set, None, u'Form of expression')

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'to'), 'to', '__httpmorphml_orgchannelmlschema_TimeCourse_to', pyxb.binding.datatypes.string, required=True)
    
    to = property(__to.value, __to.set, None, u'Target state of the transition in kinetic scheme. ')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __from.name() : __from,
        __scale.name() : __scale,
        __name.name() : __name,
        __expr.name() : __expr,
        __midpoint.name() : __midpoint,
        __rate.name() : __rate,
        __expr_form.name() : __expr_form,
        __to.name() : __to
    }
_Namespace_cml.addCategoryObject('typeBinding', u'TimeCourse', TimeCourse)


# Complex type InhomogeneousValue with content type EMPTY
class InhomogeneousValue (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'InhomogeneousValue')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpmorphml_orgbiophysicsschema_InhomogeneousValue_value', pyxb.binding.datatypes.string, required=True)
    
    value_ = property(__value.value, __value.set, None, u'Equation showing how parameter changes as function of variable attribute in inhomogeneous_param element')

    
    # Attribute param_name uses Python identifier param_name
    __param_name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'param_name'), 'param_name', '__httpmorphml_orgbiophysicsschema_InhomogeneousValue_param_name', pyxb.binding.datatypes.string, required=True)
    
    param_name = property(__param_name.value, __param_name.set, None, u'Name used in the inhomogeneous_param element in the cable group')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __value.name() : __value,
        __param_name.name() : __param_name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'InhomogeneousValue', InhomogeneousValue)


# Complex type InhomogeneousParam with content type ELEMENT_ONLY
class InhomogeneousParam (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'InhomogeneousParam')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}proximal uses Python identifier proximal
    __proximal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), 'proximal', '__httpmorphml_orgmorphmlschema_InhomogeneousParam_httpmorphml_orgmorphmlschemaproximal', False)

    
    proximal = property(__proximal.value, __proximal.set, None, u'Information on the value of the variable at the proximal point. If this element is absent,\n                    the value of the variable is determined simply from the metric, e.g. absolute path length')

    
    # Element {http://morphml.org/morphml/schema}metric uses Python identifier metric
    __metric = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'metric'), 'metric', '__httpmorphml_orgmorphmlschema_InhomogeneousParam_httpmorphml_orgmorphmlschemametric', False)

    
    metric = property(__metric.value, __metric.set, None, u'The metric used to determine the variable')

    
    # Element {http://morphml.org/morphml/schema}distal uses Python identifier distal
    __distal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), 'distal', '__httpmorphml_orgmorphmlschema_InhomogeneousParam_httpmorphml_orgmorphmlschemadistal', False)

    
    distal = property(__distal.value, __distal.set, None, u'Information on the value of the variable at the distal point. If this element is absent, the\n                    value of the variable is determined simply from the metric, e.g. path length')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_InhomogeneousParam_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name of the inhomogeneous parameter specification')

    
    # Attribute variable uses Python identifier variable
    __variable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'variable'), 'variable', '__httpmorphml_orgmorphmlschema_InhomogeneousParam_variable', pyxb.binding.datatypes.string, required=True)
    
    variable = property(__variable.value, __variable.set, None, u'Name of the variable which will change over the length')


    _ElementMap = {
        __proximal.name() : __proximal,
        __metric.name() : __metric,
        __distal.name() : __distal
    }
    _AttributeMap = {
        __name.name() : __name,
        __variable.name() : __variable
    }
_Namespace_mml.addCategoryObject('typeBinding', u'InhomogeneousParam', InhomogeneousParam)


# Complex type CTD_ANON_17 with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_CTD_ANON_7_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_CTD_ANON_7_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'feature'), 'feature', '__httpmorphml_orgmorphmlschema_CTD_ANON_7_httpmorphml_orgmorphmlschemafeature', True)

    
    feature = property(__feature.value, __feature.set, None, u'A single feature of note.')

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_CTD_ANON_7_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_CTD_ANON_7_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)


    _ElementMap = {
        __group.name() : __group,
        __properties.name() : __properties,
        __feature.name() : __feature,
        __notes.name() : __notes,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        
    }



# Complex type Feature with content type ELEMENT_ONLY
class Feature (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Feature')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}polyhedron uses Python identifier polyhedron
    __polyhedron = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron'), 'polyhedron', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemapolyhedron', True)

    
    polyhedron = property(__polyhedron.value, __polyhedron.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}path uses Python identifier path
    __path = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'path'), 'path', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemapath', True)

    
    path = property(__path.value, __path.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere'), 'sphere', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemasphere', True)

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}freePoints uses Python identifier freePoints
    __freePoints = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints'), 'freePoints', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemafreePoints', True)

    
    freePoints = property(__freePoints.value, __freePoints.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}manifold uses Python identifier manifold
    __manifold = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'manifold'), 'manifold', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemamanifold', True)

    
    manifold = property(__manifold.value, __manifold.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}polygon uses Python identifier polygon
    __polygon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon'), 'polygon', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmorphmlschemapolygon', True)

    
    polygon = property(__polygon.value, __polygon.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_Feature_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_Feature_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __polyhedron.name() : __polyhedron,
        __path.name() : __path,
        __group.name() : __group,
        __sphere.name() : __sphere,
        __freePoints.name() : __freePoints,
        __notes.name() : __notes,
        __properties.name() : __properties,
        __manifold.name() : __manifold,
        __polygon.name() : __polygon,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        __name.name() : __name
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Feature', Feature)


# Complex type SynapticLocation with content type EMPTY
class SynapticLocation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'SynapticLocation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fraction_along uses Python identifier fraction_along
    __fraction_along = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fraction_along'), 'fraction_along', '__httpmorphml_orgnetworkmlschema_SynapticLocation_fraction_along', ZeroToOne, unicode_default=u'0.5')
    
    fraction_along = property(__fraction_along.value, __fraction_along.set, None, u'The fraction along the length of the specified segment where the synapse is located.')

    
    # Attribute cell_id uses Python identifier cell_id
    __cell_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cell_id'), 'cell_id', '__httpmorphml_orgnetworkmlschema_SynapticLocation_cell_id', pyxb.binding.datatypes.integer, required=True)
    
    cell_id = property(__cell_id.value, __cell_id.set, None, u'The ID of the cell. Must be listed in populations, so that too must list instances')

    
    # Attribute segment_id uses Python identifier segment_id
    __segment_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'segment_id'), 'segment_id', '__httpmorphml_orgnetworkmlschema_SynapticLocation_segment_id', pyxb.binding.datatypes.integer, unicode_default=u'0')
    
    segment_id = property(__segment_id.value, __segment_id.set, None, u'The segment where the synapse is located.')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fraction_along.name() : __fraction_along,
        __cell_id.name() : __cell_id,
        __segment_id.name() : __segment_id
    }
_Namespace_net.addCategoryObject('typeBinding', u'SynapticLocation', SynapticLocation)


# Complex type Path with content type ELEMENT_ONLY
class Path (Points):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Path')
    # Base type is Points
    
    # Element point ({http://morphml.org/metadata/schema}point) inherited from {http://morphml.org/metadata/schema}Points
    
    # Attribute parent uses Python identifier parent
    __parent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'parent'), 'parent', '__httpmorphml_orgmorphmlschema_Path_parent', pyxb.binding.datatypes.nonNegativeInteger)
    
    parent = property(__parent.value, __parent.set, None, u'A path id. A way to connect this path to another.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpmorphml_orgmorphmlschema_Path_id', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute name inherited from {http://morphml.org/metadata/schema}Points

    _ElementMap = Points._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Points._AttributeMap.copy()
    _AttributeMap.update({
        __parent.name() : __parent,
        __id.name() : __id
    })
_Namespace_mml.addCategoryObject('typeBinding', u'Path', Path)


# Complex type Manifold with content type ELEMENT_ONLY
class Manifold (Points):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'Manifold')
    # Base type is Points
    
    # Element point ({http://morphml.org/metadata/schema}point) inherited from {http://morphml.org/metadata/schema}Points
    
    # Attribute name inherited from {http://morphml.org/metadata/schema}Points

    _ElementMap = Points._ElementMap.copy()
    _ElementMap.update({
        
    })
    _AttributeMap = Points._AttributeMap.copy()
    _AttributeMap.update({
        
    })
_Namespace_meta.addCategoryObject('typeBinding', u'Manifold', Manifold)


# Complex type PropertyDetail with content type ELEMENT_ONLY
class PropertyDetail (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'PropertyDetail')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}type uses Python identifier type
    __type = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'type'), 'type', '__httpmorphml_orgmetadataschema_PropertyDetail_httpmorphml_orgmetadataschematype', False)

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'description'), 'description', '__httpmorphml_orgmetadataschema_PropertyDetail_httpmorphml_orgmetadataschemadescription', False)

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute property uses Python identifier property_
    __property = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__httpmorphml_orgmetadataschema_PropertyDetail_property', pyxb.binding.datatypes.string)
    
    property_ = property(__property.value, __property.set, None, None)


    _ElementMap = {
        __type.name() : __type,
        __description.name() : __description
    }
    _AttributeMap = {
        __property.name() : __property
    }
_Namespace_meta.addCategoryObject('typeBinding', u'PropertyDetail', PropertyDetail)


# Complex type NetworkML with content type ELEMENT_ONLY
class NetworkML (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'NetworkML')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}populations uses Python identifier populations
    __populations = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'populations'), 'populations', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgnetworkmlschemapopulations', False)

    
    populations = property(__populations.value, __populations.set, None, u"The least that's needed in a network is a population of cells...")

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}projections uses Python identifier projections
    __projections = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'projections'), 'projections', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgnetworkmlschemaprojections', False)

    
    projections = property(__projections.value, __projections.set, None, u'In theory there can be no projections, if the file is intended only to specify positions')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}inputs uses Python identifier inputs
    __inputs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs'), 'inputs', '__httpmorphml_orgnetworkmlschema_NetworkML_httpmorphml_orgnetworkmlschemainputs', False)

    
    inputs = property(__inputs.value, __inputs.set, None, u'No inputs need be specified')

    
    # Attribute volumeUnits uses Python identifier volumeUnits
    __volumeUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'volumeUnits'), 'volumeUnits', '__httpmorphml_orgnetworkmlschema_NetworkML_volumeUnits', VolumeUnits, unicode_default=u'cubic_millimeter')
    
    volumeUnits = property(__volumeUnits.value, __volumeUnits.set, None, u'Unit of all volume measurements.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lengthUnits'), 'lengthUnits', '__httpmorphml_orgnetworkmlschema_NetworkML_lengthUnits', LengthUnits)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgnetworkmlschema_NetworkML_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute length_units uses Python identifier length_units
    __length_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length_units'), 'length_units', '__httpmorphml_orgnetworkmlschema_NetworkML_length_units', LengthUnits)
    
    length_units = property(__length_units.value, __length_units.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')


    _ElementMap = {
        __properties.name() : __properties,
        __populations.name() : __populations,
        __annotation.name() : __annotation,
        __projections.name() : __projections,
        __group.name() : __group,
        __notes.name() : __notes,
        __inputs.name() : __inputs
    }
    _AttributeMap = {
        __volumeUnits.name() : __volumeUnits,
        __lengthUnits.name() : __lengthUnits,
        __name.name() : __name,
        __length_units.name() : __length_units
    }
_Namespace_net.addCategoryObject('typeBinding', u'NetworkML', NetworkML)


# Complex type CTD_ANON_18 with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/morphml/schema}groupDetail uses Python identifier groupDetail
    __groupDetail = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetail'), 'groupDetail', '__httpmorphml_orgmorphmlschema_CTD_ANON_8_httpmorphml_orgmorphmlschemagroupDetail', True)

    
    groupDetail = property(__groupDetail.value, __groupDetail.set, None, None)


    _ElementMap = {
        __groupDetail.name() : __groupDetail
    }
    _AttributeMap = {
        
    }



# Complex type Morphology with content type ELEMENT_ONLY
class Morphology (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_mml, u'Morphology')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}groupDetails uses Python identifier groupDetails
    __groupDetails = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetails'), 'groupDetails', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmorphmlschemagroupDetails', False)

    
    groupDetails = property(__groupDetails.value, __groupDetails.set, None, u'Collection of all GroupDetails for this instance.')

    
    # Element {http://morphml.org/morphml/schema}cells uses Python identifier cells
    __cells = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'cells'), 'cells', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmorphmlschemacells', False)

    
    cells = property(__cells.value, __cells.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}propertyDetails uses Python identifier propertyDetails
    __propertyDetails = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetails'), 'propertyDetails', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmorphmlschemapropertyDetails', False)

    
    propertyDetails = property(__propertyDetails.value, __propertyDetails.set, None, u'Collection of all PropertyDetails for this instance.')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}features uses Python identifier features
    __features = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'features'), 'features', '__httpmorphml_orgmorphmlschema_Morphology_httpmorphml_orgmorphmlschemafeatures', False)

    
    features = property(__features.value, __features.set, None, u'Collection of all extracellular histological features.')

    
    # Attribute volumeUnits uses Python identifier volumeUnits
    __volumeUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'volumeUnits'), 'volumeUnits', '__httpmorphml_orgmorphmlschema_Morphology_volumeUnits', VolumeUnits, unicode_default=u'cubic_millimeter')
    
    volumeUnits = property(__volumeUnits.value, __volumeUnits.set, None, u'Unit of all volume measurements.')

    
    # Attribute lengthUnits uses Python identifier lengthUnits
    __lengthUnits = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lengthUnits'), 'lengthUnits', '__httpmorphml_orgmorphmlschema_Morphology_lengthUnits', LengthUnits)
    
    lengthUnits = property(__lengthUnits.value, __lengthUnits.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgmorphmlschema_Morphology_name', pyxb.binding.datatypes.string)
    
    name = property(__name.value, __name.set, None, u'An optional name which can be given to the morphology')

    
    # Attribute length_units uses Python identifier length_units
    __length_units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length_units'), 'length_units', '__httpmorphml_orgmorphmlschema_Morphology_length_units', LengthUnits)
    
    length_units = property(__length_units.value, __length_units.set, None, u'Unit of all length measurements. Usually has the value <b>micrometer</b>. Note: length_units will be the preferred form in v2.0')


    _ElementMap = {
        __properties.name() : __properties,
        __groupDetails.name() : __groupDetails,
        __cells.name() : __cells,
        __propertyDetails.name() : __propertyDetails,
        __annotation.name() : __annotation,
        __group.name() : __group,
        __notes.name() : __notes,
        __features.name() : __features
    }
    _AttributeMap = {
        __volumeUnits.name() : __volumeUnits,
        __lengthUnits.name() : __lengthUnits,
        __name.name() : __name,
        __length_units.name() : __length_units
    }
_Namespace_mml.addCategoryObject('typeBinding', u'Morphology', Morphology)


# Complex type Mechanism with content type ELEMENT_ONLY
class Mechanism (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_bio, u'Mechanism')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/biophysics/schema}variable_parameter uses Python identifier variable_parameter
    __variable_parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), 'variable_parameter', '__httpmorphml_orgbiophysicsschema_Mechanism_httpmorphml_orgbiophysicsschemavariable_parameter', True)

    
    variable_parameter = property(__variable_parameter.value, __variable_parameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')

    
    # Element {http://morphml.org/biophysics/schema}variableParameter uses Python identifier variableParameter
    __variableParameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), 'variableParameter', '__httpmorphml_orgbiophysicsschema_Mechanism_httpmorphml_orgbiophysicsschemavariableParameter', True)

    
    variableParameter = property(__variableParameter.value, __variableParameter.set, None, u'Note variable_parameter will be the preferred form in v2.0')

    
    # Element {http://morphml.org/biophysics/schema}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), 'parameter', '__httpmorphml_orgbiophysicsschema_Mechanism_httpmorphml_orgbiophysicsschemaparameter', True)

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpmorphml_orgbiophysicsschema_Mechanism_type', MechanismType, required=True)
    
    type = property(__type.value, __type.set, None, u'Specifies the type of cellular mechanism (Channel Mechanism/Ion Concentration). Note could be used for any type of electrophysiological property of a section of a cell')

    
    # Attribute passive_conductance uses Python identifier passive_conductance
    __passive_conductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'passive_conductance'), 'passive_conductance', '__httpmorphml_orgbiophysicsschema_Mechanism_passive_conductance', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    passive_conductance = property(__passive_conductance.value, __passive_conductance.set, None, u"Whether this is a passive/leak conductance. In this case, 2 params, gmax and e should be sufficient to fully specify the\n            mechanism, independent of any implementation. Useful e.g. for mapping to and from inbuilt mechanisms in simulators (e.g. pas in NEURON, Em/Rm in GENESIS).\n        NOTE: this attribute will be required in v2.0!! Don't use passiveConductance anymore.\n            Changed for consistency with ChannelML and NetworkML naming conventions.")

    
    # Attribute passiveConductance uses Python identifier passiveConductance
    __passiveConductance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'passiveConductance'), 'passiveConductance', '__httpmorphml_orgbiophysicsschema_Mechanism_passiveConductance', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    passiveConductance = property(__passiveConductance.value, __passiveConductance.set, None, u'Whether this is a passive/leak conductance. NOTE: this attribute will be removed in v2.0!! Use passive_conductance instead.\n            Changed for consistency with ChannelML and NetworkML naming conventions.')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpmorphml_orgbiophysicsschema_Mechanism_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, u'Name of the mechanism. Should refer to a named mechanism in a ChannelML file')


    _ElementMap = {
        __variable_parameter.name() : __variable_parameter,
        __variableParameter.name() : __variableParameter,
        __parameter.name() : __parameter
    }
    _AttributeMap = {
        __type.name() : __type,
        __passive_conductance.name() : __passive_conductance,
        __passiveConductance.name() : __passiveConductance,
        __name.name() : __name
    }
_Namespace_bio.addCategoryObject('typeBinding', u'Mechanism', Mechanism)


# Complex type GroupDetail with content type ELEMENT_ONLY
class GroupDetail (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_meta, u'GroupDetail')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmetadataschema_GroupDetail_httpmorphml_orgmetadataschemaproperties', True)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'description'), 'description', '__httpmorphml_orgmetadataschema_GroupDetail_httpmorphml_orgmetadataschemadescription', False)

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute group uses Python identifier group
    __group = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__httpmorphml_orgmetadataschema_GroupDetail_group', pyxb.binding.datatypes.string)
    
    group = property(__group.value, __group.set, None, None)


    _ElementMap = {
        __properties.name() : __properties,
        __description.name() : __description
    }
    _AttributeMap = {
        __group.name() : __group
    }
_Namespace_meta.addCategoryObject('typeBinding', u'GroupDetail', GroupDetail)


# Complex type RandomArrangement with content type ELEMENT_ONLY
class RandomArrangement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'RandomArrangement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}spherical_location uses Python identifier spherical_location
    __spherical_location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'spherical_location'), 'spherical_location', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgnetworkmlschemaspherical_location', False)

    
    spherical_location = property(__spherical_location.value, __spherical_location.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}rectangular_location uses Python identifier rectangular_location
    __rectangular_location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location'), 'rectangular_location', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgnetworkmlschemarectangular_location', False)

    
    rectangular_location = property(__rectangular_location.value, __rectangular_location.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}population_size uses Python identifier population_size
    __population_size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'population_size'), 'population_size', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgnetworkmlschemapopulation_size', False)

    
    population_size = property(__population_size.value, __population_size.set, None, u'Number of cells to place randomly in the specified 3D location')

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_RandomArrangement_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)


    _ElementMap = {
        __properties.name() : __properties,
        __spherical_location.name() : __spherical_location,
        __notes.name() : __notes,
        __annotation.name() : __annotation,
        __rectangular_location.name() : __rectangular_location,
        __population_size.name() : __population_size,
        __group.name() : __group
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'RandomArrangement', RandomArrangement)


# Complex type GridArrangement with content type ELEMENT_ONLY
class GridArrangement (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_net, u'GridArrangement')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/networkml/schema}rectangular_location uses Python identifier rectangular_location
    __rectangular_location = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location'), 'rectangular_location', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgnetworkmlschemarectangular_location', False)

    
    rectangular_location = property(__rectangular_location.value, __rectangular_location.set, None, u'3D box in which the cells are regularly packed. Note if one or two of dimensions of the box is zero it can be a 2D or 1D grid (respectively).')

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}spacing uses Python identifier spacing
    __spacing = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'spacing'), 'spacing', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgnetworkmlschemaspacing', False)

    
    spacing = property(__spacing.value, __spacing.set, None, u'Separation of the cells in each dimension')

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)

    
    # Element {http://morphml.org/networkml/schema}non_spatial_grid uses Python identifier non_spatial_grid
    __non_spatial_grid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_net, u'non_spatial_grid'), 'non_spatial_grid', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgnetworkmlschemanon_spatial_grid', False)

    
    non_spatial_grid = property(__non_spatial_grid.value, __non_spatial_grid.set, None, u'Specifying this means the precise spatial location of the cells is irrelvant')

    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgnetworkmlschema_GridArrangement_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)


    _ElementMap = {
        __rectangular_location.name() : __rectangular_location,
        __notes.name() : __notes,
        __group.name() : __group,
        __spacing.name() : __spacing,
        __properties.name() : __properties,
        __non_spatial_grid.name() : __non_spatial_grid,
        __annotation.name() : __annotation
    }
    _AttributeMap = {
        
    }
_Namespace_net.addCategoryObject('typeBinding', u'GridArrangement', GridArrangement)


# Complex type CTD_ANON_19 with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/metadata/schema}annotation uses Python identifier annotation
    __annotation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), 'annotation', '__httpmorphml_orgmorphmlschema_CTD_ANON_9_httpmorphml_orgmetadataschemaannotation', False)

    
    annotation = property(__annotation.value, __annotation.set, None, None)

    
    # Element {http://morphml.org/morphml/schema}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_mml, u'segment'), 'segment', '__httpmorphml_orgmorphmlschema_CTD_ANON_9_httpmorphml_orgmorphmlschemasegment', True)

    
    segment = property(__segment.value, __segment.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), 'notes', '__httpmorphml_orgmorphmlschema_CTD_ANON_9_httpmorphml_orgmetadataschemanotes', False)

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}group uses Python identifier group
    __group = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), 'group', '__httpmorphml_orgmorphmlschema_CTD_ANON_9_httpmorphml_orgmetadataschemagroup', True)

    
    group = property(__group.value, __group.set, None, None)

    
    # Element {http://morphml.org/metadata/schema}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), 'properties', '__httpmorphml_orgmorphmlschema_CTD_ANON_9_httpmorphml_orgmetadataschemaproperties', False)

    
    properties = property(__properties.value, __properties.set, None, None)


    _ElementMap = {
        __annotation.name() : __annotation,
        __segment.name() : __segment,
        __notes.name() : __notes,
        __group.name() : __group,
        __properties.name() : __properties
    }
    _AttributeMap = {
        
    }



# Complex type Deprecated_KSGate with content type ELEMENT_ONLY
class Deprecated_KSGate (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_cml, u'Deprecated_KSGate')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://morphml.org/channelml/schema}transition uses Python identifier transition
    __transition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), 'transition', '__httpmorphml_orgchannelmlschema_Deprecated_KSGate_httpmorphml_orgchannelmlschematransition', True)

    
    transition = property(__transition.value, __transition.set, None, None)

    
    # Element {http://morphml.org/channelml/schema}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(_Namespace_cml, u'state'), 'state', '__httpmorphml_orgchannelmlschema_Deprecated_KSGate_httpmorphml_orgchannelmlschemastate', True)

    
    state = property(__state.value, __state.set, None, None)


    _ElementMap = {
        __transition.name() : __transition,
        __state.name() : __state
    }
    _AttributeMap = {
        
    }
_Namespace_cml.addCategoryObject('typeBinding', u'Deprecated_KSGate', Deprecated_KSGate)


neuroml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'neuroml'), NeuroMLLevel3, documentation=u'The root NeuroML Level 3 element.')
_Namespace.addCategoryObject('elementBinding', neuroml.name().localName(), neuroml)

biophysics = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'biophysics'), Biophysics, documentation=u'The root element. All other complex/simple elements will be children of this.')
_Namespace_bio.addCategoryObject('elementBinding', biophysics.name().localName(), biophysics)

networkml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'networkml'), NetworkML, documentation=u'The root element. \n                    Note: this element will only be present in a standalone NetworkML file (i.e. no cells or channels defined in the file).\n                    For files covering many levels, neuroml will be the root element')
_Namespace_net.addCategoryObject('elementBinding', networkml.name().localName(), networkml)

morphml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'morphml'), Morphology, documentation=u'The root element, and so will start any MorphML (NeuroML Level 1) compliant document.')
_Namespace_mml.addCategoryObject('elementBinding', morphml.name().localName(), morphml)

channelml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'channelml'), ChannelML, documentation=u'The root element of any ChannelML file. Note this element will only be present in a standalone ChannelML file.\n            For files covering many levels, neuroml will be the root element')
_Namespace_cml.addCategoryObject('elementBinding', channelml.name().localName(), channelml)



DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'fixed_pool_info'), FixedPoolInfo, scope=DecayingPoolModel))

DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ceiling'), ConcentrationValue, scope=DecayingPoolModel, documentation=u'The maximum concentration which the ion pool should be allowed get to. NOTE: In v2.0 this element will be removed. Attribute ceiling will be used instead.'))

DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'resting_conc'), ConcentrationValue, scope=DecayingPoolModel, documentation=u'Resting concentration of ion. NOTE: In v2.0 this element will be removed. Attribute resting_conc will be used instead.'))

DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'decay_constant'), TimeConstantValue, scope=DecayingPoolModel, documentation=u'Exponential decay time of pool. NOTE: In v2.0 this element will be removed. Attribute decay_constant will be used instead.'))

DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'pool_volume_info'), PoolVolumeInfo, scope=DecayingPoolModel))

DecayingPoolModel._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'inv_decay_constant'), InvTimeConstantValue, scope=DecayingPoolModel, documentation=u'Reciprocal of exponential decay time constant of pool'))
DecayingPoolModel._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'decay_constant')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'inv_decay_constant')), min_occurs=1, max_occurs=1)
    )
DecayingPoolModel._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'pool_volume_info')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'fixed_pool_info')), min_occurs=1, max_occurs=1)
    )
DecayingPoolModel._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'resting_conc')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DecayingPoolModel._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(DecayingPoolModel._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ceiling')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DecayingPoolModel._GroupModel_2, min_occurs=1, max_occurs=1)
    )
DecayingPoolModel._ContentModel = pyxb.binding.content.ParticleModel(DecayingPoolModel._GroupModel, min_occurs=1, max_occurs=1)


Annotation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_skip, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0L, max_occurs=None)
    )
Annotation._ContentModel = pyxb.binding.content.ParticleModel(Annotation._GroupModel, min_occurs=1, max_occurs=1)



Properties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'property'), Property, scope=Properties))
Properties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Properties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'property')), min_occurs=0L, max_occurs=None)
    )
Properties._ContentModel = pyxb.binding.content.ParticleModel(Properties._GroupModel, min_occurs=1, max_occurs=1)



InputSitePattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'percentage_cells'), CTD_ANON, scope=InputSitePattern, documentation=u'Apply input to a certain percentage of cells in a group'))

InputSitePattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'all_cells'), CTD_ANON_5, scope=InputSitePattern, documentation=u'Apply input on all cells in group'))
InputSitePattern._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputSitePattern._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'all_cells')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSitePattern._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'percentage_cells')), min_occurs=1, max_occurs=1)
    )
InputSitePattern._ContentModel = pyxb.binding.content.ParticleModel(InputSitePattern._GroupModel, min_occurs=1, max_occurs=1)



GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'open_state'), OpenState, scope=GatingComplex))

GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), Transition, scope=GatingComplex))

GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'time_course'), TimeCourse, scope=GatingComplex))

GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'steady_state'), SteadyState, scope=GatingComplex))

GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'closed_state'), ClosedState, scope=GatingComplex))

GatingComplex._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), Initialisation, scope=GatingComplex, documentation=u'For debugging/testing only! Use with caution!!'))
GatingComplex._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'closed_state')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'open_state')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'time_course')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(GatingComplex._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'steady_state')), min_occurs=0L, max_occurs=None)
    )
GatingComplex._ContentModel = pyxb.binding.content.ParticleModel(GatingComplex._GroupModel, min_occurs=1, max_occurs=1)



VariableNamedParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value'), InhomogeneousValue, scope=VariableNamedParameter))

VariableNamedParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), pyxb.binding.datatypes.string, scope=VariableNamedParameter))
VariableNamedParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(VariableNamedParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'group')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(VariableNamedParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value')), min_occurs=1, max_occurs=None)
    )
VariableNamedParameter._ContentModel = pyxb.binding.content.ParticleModel(VariableNamedParameter._GroupModel, min_occurs=1, max_occurs=1)



NeuroMorphoRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'morphologyRef'), pyxb.binding.datatypes.string, scope=NeuroMorphoRef))

NeuroMorphoRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=NeuroMorphoRef, documentation=u'Comment on how this morphology relates to the current model'))

NeuroMorphoRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), pyxb.binding.datatypes.string, scope=NeuroMorphoRef))
NeuroMorphoRef._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(NeuroMorphoRef._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'morphologyRef')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMorphoRef._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMorphoRef._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=1)
    )
NeuroMorphoRef._ContentModel = pyxb.binding.content.ParticleModel(NeuroMorphoRef._GroupModel, min_occurs=1, max_occurs=1)



Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'name'), pyxb.binding.datatypes.string, scope=Person))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=Person, documentation=u'Optional comment on their specific contribution'))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'email'), pyxb.binding.datatypes.string, scope=Person, documentation=u"Useful to have. Note: something like '- at -' replacing the @ might be wise, in case a HTML version of the file goes online."))

Person._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'institution'), pyxb.binding.datatypes.string, scope=Person))
Person._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Person._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Person._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'institution')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Person._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'email')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Person._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=1)
    )
Person._ContentModel = pyxb.binding.content.ParticleModel(Person._GroupModel, min_occurs=1, max_occurs=1)



UnnamedParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), pyxb.binding.datatypes.string, scope=UnnamedParameter))
UnnamedParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(UnnamedParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'group')), min_occurs=1, max_occurs=None)
    )
UnnamedParameter._ContentModel = pyxb.binding.content.ParticleModel(UnnamedParameter._GroupModel, min_occurs=1, max_occurs=1)



VariableParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value'), InhomogeneousValue, scope=VariableParameter))

VariableParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), pyxb.binding.datatypes.string, scope=VariableParameter))
VariableParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(VariableParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'group')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(VariableParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'inhomogeneous_value')), min_occurs=1, max_occurs=None)
    )
VariableParameter._ContentModel = pyxb.binding.content.ParticleModel(VariableParameter._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Deprecated_RateConstantEqnChoice))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Deprecated_RateConstantEqnChoice))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic'), Deprecated_GenericEquation, scope=Deprecated_RateConstantEqnChoice, documentation=u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0'))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Deprecated_RateConstantEqnChoice))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Deprecated_RateConstantEqnChoice))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameterised_hh'), Deprecated_AkdEquation, scope=Deprecated_RateConstantEqnChoice))

Deprecated_RateConstantEqnChoice._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh'), Deprecated_GenericEquation, scope=Deprecated_RateConstantEqnChoice, documentation=u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0'))
Deprecated_RateConstantEqnChoice._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Deprecated_RateConstantEqnChoice._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameterised_hh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic')), min_occurs=1, max_occurs=1)
    )
Deprecated_RateConstantEqnChoice._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Deprecated_RateConstantEqnChoice._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqnChoice._GroupModel, min_occurs=1, max_occurs=1)



SynapseInternalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=SynapseInternalProperties))

SynapseInternalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=SynapseInternalProperties))

SynapseInternalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=SynapseInternalProperties))

SynapseInternalProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=SynapseInternalProperties))
SynapseInternalProperties._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseInternalProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseInternalProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseInternalProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseInternalProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
SynapseInternalProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseInternalProperties._GroupModel_, min_occurs=1, max_occurs=1)
    )
SynapseInternalProperties._ContentModel = pyxb.binding.content.ParticleModel(SynapseInternalProperties._GroupModel, min_occurs=1, max_occurs=1)


LocalSynapticProperties._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LocalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(LocalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
LocalSynapticProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(LocalSynapticProperties._GroupModel_, min_occurs=1, max_occurs=1)
    )
LocalSynapticProperties._ContentModel = pyxb.binding.content.ParticleModel(LocalSynapticProperties._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_HHGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), Deprecated_Transition, scope=Deprecated_HHGate))
Deprecated_HHGate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_HHGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition')), min_occurs=1, max_occurs=1)
    )
Deprecated_HHGate._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_HHGate._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_RateConstVoltConcDep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic'), Deprecated_GenericEquation, scope=Deprecated_RateConstVoltConcDep, documentation=u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0'))

Deprecated_RateConstVoltConcDep._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh'), Deprecated_GenericEquation, scope=Deprecated_RateConstVoltConcDep, documentation=u'Note: use generic as opposed to generic_equation_hh. The latter will be removed in v2.0'))
Deprecated_RateConstVoltConcDep._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Deprecated_RateConstVoltConcDep._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic_equation_hh')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_RateConstVoltConcDep._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'generic')), min_occurs=1, max_occurs=1)
    )
Deprecated_RateConstVoltConcDep._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_RateConstVoltConcDep._GroupModel, min_occurs=1, max_occurs=1)



ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_concentration'), IonConcentration, scope=ChannelML, documentation=u'Specification of how an ion concentration alters with time, e.g. calcium dynamics. This may influence other\n                   channels (e.g. Ca dependent K channels), and other mechanisms may have a contribution to the concentration of the ion specified here\n                   (e.g. a channel transmitting calcium).'))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion'), Deprecated_Ion, scope=ChannelML, documentation=u'One or more ions which play some role in the mechanism, e.g. transmitted by the channel, alters the rate, etc. Note: deprecated since v1.7.3'))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=ChannelML))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'channel_type'), ChannelType, scope=ChannelML, documentation=u'Specification of a voltage or ligand gated membrane conductance mechanism'))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=ChannelML))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'synapse_type'), SynapseType, scope=ChannelML, documentation=u'Specification of a synaptic conductance, triggered by a presynaptic event'))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=ChannelML))

ChannelML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=ChannelML))
ChannelML._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
ChannelML._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ChannelML._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'channel_type')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'synapse_type')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_concentration')), min_occurs=0L, max_occurs=None)
    )
ChannelML._ContentModel = pyxb.binding.content.ParticleModel(ChannelML._GroupModel, min_occurs=1, max_occurs=1)



Populations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Populations))

Populations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Populations))

Populations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Populations))

Populations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Populations))

Populations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'population'), Population, scope=Populations))
Populations._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Populations._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Populations._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Populations._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Populations._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Populations._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Populations._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Populations._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'population')), min_occurs=1, max_occurs=None)
    )
Populations._ContentModel = pyxb.binding.content.ParticleModel(Populations._GroupModel, min_occurs=1, max_occurs=1)



Authors._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelTranslator'), Person, scope=Authors, documentation=u'Person who translated the model to NeuroML'))

Authors._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelAuthor'), Person, scope=Authors, documentation=u'Author of the original model'))
Authors._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Authors._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelAuthor')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Authors._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelTranslator')), min_occurs=0L, max_occurs=None)
    )
Authors._ContentModel = pyxb.binding.content.ParticleModel(Authors._GroupModel, min_occurs=1, max_occurs=1)



Projections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Projections))

Projections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Projections))

Projections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'projection'), Projection, scope=Projections))

Projections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Projections))

Projections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Projections))
Projections._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Projections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Projections._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Projections._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'projection')), min_occurs=1L, max_occurs=None)
    )
Projections._ContentModel = pyxb.binding.content.ParticleModel(Projections._GroupModel, min_occurs=1, max_occurs=1)



Inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Inputs))

Inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Inputs))

Inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'input'), Input, scope=Inputs))

Inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Inputs))

Inputs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Inputs))
Inputs._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Inputs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Inputs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Inputs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Inputs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Inputs._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Inputs._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Inputs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'input')), min_occurs=1L, max_occurs=None)
    )
Inputs._ContentModel = pyxb.binding.content.ParticleModel(Inputs._GroupModel, min_occurs=1, max_occurs=1)



NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), NeuroMorphoRef, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), Publication, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs'), Inputs, scope=NeuroMLLevel3, documentation=u'No inputs need be specified'))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'populations'), Populations, scope=NeuroMLLevel3, documentation=u"The least that's needed in a network is a population of cells..."))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'cells'), Level3Cells, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), NeuronDBReference, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'projections'), Projections, scope=NeuroMLLevel3, documentation=u'In theory there can be no projections, if the file is intended only to specify positions'))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), ModelDBReference, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'channels'), ChannelML, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), Authors, scope=NeuroMLLevel3))

NeuroMLLevel3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=NeuroMLLevel3))
NeuroMLLevel3._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
NeuroMLLevel3._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
NeuroMLLevel3._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'populations')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'projections')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs')), min_occurs=0L, max_occurs=1)
    )
NeuroMLLevel3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace, u'cells')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._UseForTag(pyxb.namespace.ExpandedName(_Namespace, u'channels')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuroMLLevel3._GroupModel_3, min_occurs=0L, max_occurs=1)
    )
NeuroMLLevel3._ContentModel = pyxb.binding.content.ParticleModel(NeuroMLLevel3._GroupModel, min_occurs=1, max_occurs=1)



Level3Cells._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'cell'), Level3Cell, scope=Level3Cells, documentation=u'A single cell specified in MorphML extended to include channel density info.'))
Level3Cells._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cells._UseForTag(pyxb.namespace.ExpandedName(_Namespace, u'cell')), min_occurs=1, max_occurs=None)
    )
Level3Cells._ContentModel = pyxb.binding.content.ParticleModel(Level3Cells._GroupModel, min_occurs=1, max_occurs=1)



FixedPoolInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'phi'), pyxb.binding.datatypes.double, scope=FixedPoolInfo))
FixedPoolInfo._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FixedPoolInfo._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'phi')), min_occurs=1, max_occurs=1)
    )
FixedPoolInfo._ContentModel = pyxb.binding.content.ParticleModel(FixedPoolInfo._GroupModel, min_occurs=1, max_occurs=1)



Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints'), FreePoints, scope=Cell, documentation=u'The collection of varicosities or synaptic connections.'))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cellBody'), CTD_ANON_14, scope=Cell, documentation=u'Used for anatomical representation of the soma. Use a Segment with equivalent properties to retain connectivity of branches to the soma for downstream applications (e.g. neuronal simulators).'))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), NeuronDBReference, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'segments'), CTD_ANON_19, scope=Cell, documentation=u'A segment defines the smallest unit within a possibly branching structure, such as a dendrite or axon. The first segment should represent the soma, if needed for downstream applications.'))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), Authors, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), ModelDBReference, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cables'), CTD_ANON_8, scope=Cell, documentation=u'The collection of cables. Each cable will be associated with a number of connected segments.'))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), Publication, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'status'), Status, scope=Cell, documentation=u'Status of the cell model: stable, in progress, etc.\n                    Further test comments explaining the current status should be added.'))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), NeuroMorphoRef, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Cell))

Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'spines'), CTD_ANON_11, scope=Cell, documentation=u'The collection of spines.'))
Cell._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Cell._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
Cell._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'segments')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cables')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cellBody')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'spines')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints')), min_occurs=0L, max_occurs=1)
    )
Cell._ContentModel = pyxb.binding.content.ParticleModel(Cell._GroupModel, min_occurs=1, max_occurs=1)



Level3Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'biophysics'), Level3Biophysics, scope=Level3Cell))

Level3Cell._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace, u'connectivity'), Level3Connectivity, scope=Level3Cell, documentation=u'Note: from v1.7.1 the preferred way to specify a potential synaptic location \n                                is with a potential_syn_loc element under connectivity under cell, as opposed to the potentialSynapticLocation \n                                under biophysics under cell. The former will be the only option from v2.0'))
Level3Cell._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Level3Cell._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
Level3Cell._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'segments')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cables')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cellBody')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'spines')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints')), min_occurs=0L, max_occurs=1)
    )
Level3Cell._GroupModel_4 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace, u'biophysics')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._UseForTag(pyxb.namespace.ExpandedName(_Namespace, u'connectivity')), min_occurs=0L, max_occurs=1)
    )
Level3Cell._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Cell._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Cell._GroupModel_4, min_occurs=1, max_occurs=1)
    )
Level3Cell._ContentModel = pyxb.binding.content.ParticleModel(Level3Cell._GroupModel, min_occurs=1, max_occurs=1)



NamedParameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'group'), pyxb.binding.datatypes.string, scope=NamedParameter))
NamedParameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NamedParameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'group')), min_occurs=1L, max_occurs=None)
    )
NamedParameter._ContentModel = pyxb.binding.content.ParticleModel(NamedParameter._GroupModel, min_occurs=1, max_occurs=1)



Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'mechanism'), Mechanism, scope=Biophysics, documentation=u'Definition of placement of a single electrophysiological mechanism (e.g. channel mechanism)\n                        on a group of cables of a cell. Note there should be at least one of these to specify the passive membrane conductance.\n                        Note: elements spec_capacitance, spec_axial_resistance, ion_props etc. should be used in preference to specificCapacitance etc!'))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_capacitance'), SpecCapacitance, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'initialMembPotential'), InitialMembPotential, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'init_memb_potential'), InitialMembPotential, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_axial_resistance'), SpecAxialResistance, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'ion_props'), IonProperties, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificAxialResistance'), SpecAxialResistance, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificCapacitance'), SpecCapacitance, scope=Biophysics))

Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'ionProperties'), IonProperties, scope=Biophysics))
Biophysics._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificCapacitance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_capacitance')), min_occurs=1, max_occurs=1)
    )
Biophysics._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificAxialResistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_axial_resistance')), min_occurs=1, max_occurs=1)
    )
Biophysics._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'initialMembPotential')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'init_memb_potential')), min_occurs=0L, max_occurs=1)
    )
Biophysics._GroupModel_4 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'ionProperties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'ion_props')), min_occurs=0L, max_occurs=None)
    )
Biophysics._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'mechanism')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Biophysics._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Biophysics._GroupModel_4, min_occurs=1, max_occurs=1)
    )
Biophysics._ContentModel = pyxb.binding.content.ParticleModel(Biophysics._GroupModel, min_occurs=1, max_occurs=1)



Level3Biophysics._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'potentialSynapticLocation'), PotentialSynapticLocation, scope=Level3Biophysics))
Level3Biophysics._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificCapacitance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_capacitance')), min_occurs=1, max_occurs=1)
    )
Level3Biophysics._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'specificAxialResistance')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'spec_axial_resistance')), min_occurs=1, max_occurs=1)
    )
Level3Biophysics._GroupModel_4 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'initialMembPotential')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'init_memb_potential')), min_occurs=0L, max_occurs=1)
    )
Level3Biophysics._GroupModel_5 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'ionProperties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'ion_props')), min_occurs=0L, max_occurs=None)
    )
Level3Biophysics._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'mechanism')), min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_4, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_5, min_occurs=1, max_occurs=1)
    )
Level3Biophysics._GroupModel_7 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Biophysics._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'potentialSynapticLocation')), min_occurs=0L, max_occurs=None)
    )
Level3Biophysics._GroupModel_6 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_7, min_occurs=0L, max_occurs=1)
    )
Level3Biophysics._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel_6, min_occurs=1, max_occurs=1)
    )
Level3Biophysics._ContentModel = pyxb.binding.content.ParticleModel(Level3Biophysics._GroupModel, min_occurs=1, max_occurs=1)



Level3Connectivity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'potential_syn_loc'), PotentialSynLoc, scope=Level3Connectivity))
Level3Connectivity._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Level3Connectivity._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'potential_syn_loc')), min_occurs=0L, max_occurs=None)
    )
Level3Connectivity._ContentModel = pyxb.binding.content.ParticleModel(Level3Connectivity._GroupModel, min_occurs=1, max_occurs=1)



Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'post'), SynapticLocation, scope=Connection, documentation=u'NOTE: Attributes post_cell_id etc. for WILL BE PREFERRED FORMAT IN v2.0'))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Connection))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'properties'), LocalSynapticProperties, scope=Connection))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Connection))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Connection))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'pre'), SynapticLocation, scope=Connection, documentation=u'NOTE: Attributes pre_cell_id etc. for WILL BE PREFERRED FORMAT IN v2.0'))

Connection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Connection))
Connection._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Connection._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Connection._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'pre')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'post')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'properties')), min_occurs=0L, max_occurs=None)
    )
Connection._ContentModel = pyxb.binding.content.ParticleModel(Connection._GroupModel, min_occurs=1, max_occurs=1)



InputSite._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim_instance'), RandomStimInstance, scope=InputSite))

InputSite._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input_instance'), PulseInput, scope=InputSite))
InputSite._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputSite._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input_instance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSite._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim_instance')), min_occurs=0L, max_occurs=1)
    )
InputSite._ContentModel = pyxb.binding.content.ParticleModel(InputSite._GroupModel, min_occurs=1, max_occurs=1)



Points._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'point'), Point, scope=Points))
Points._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Points._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'point')), min_occurs=1, max_occurs=None)
    )
Points._ContentModel = pyxb.binding.content.ParticleModel(Points._GroupModel, min_occurs=1, max_occurs=1)


FreePoints._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FreePoints._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'point')), min_occurs=1, max_occurs=None)
    )
FreePoints._ContentModel = pyxb.binding.content.ParticleModel(FreePoints._GroupModel, min_occurs=1, max_occurs=1)



PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_direction'), SynapseDirection, scope=PotentialSynapticLocation, documentation=u'Whether this synapse location allows a presynaptic connection, a postsynaptic\n                                connection or either'))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=PotentialSynapticLocation))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'group'), pyxb.binding.datatypes.string, scope=PotentialSynapticLocation, documentation=u'List of groups of sections allowing the synapse'))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=PotentialSynapticLocation))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=PotentialSynapticLocation))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), pyxb.binding.datatypes.string, scope=PotentialSynapticLocation, documentation=u'Which of the synaptic mechanisms can be present'))

PotentialSynapticLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=PotentialSynapticLocation))
PotentialSynapticLocation._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
PotentialSynapticLocation._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_direction')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'group')), min_occurs=1, max_occurs=None)
    )
PotentialSynapticLocation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynapticLocation._GroupModel_2, min_occurs=1, max_occurs=1)
    )
PotentialSynapticLocation._ContentModel = pyxb.binding.content.ParticleModel(PotentialSynapticLocation._GroupModel, min_occurs=1, max_occurs=1)



Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'cell_type'), pyxb.binding.datatypes.string, scope=Population, documentation=u'The cell type for this population. NOTE: an attribute value for cell_type WILL BE PREFERRED FORMAT IN v2.0. The option for this element will be removed!'))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Population))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Population))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Population))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'instances'), Instances, scope=Population))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Population))

Population._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'pop_location'), PopulationLocation, scope=Population))
Population._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Population._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'instances')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'pop_location')), min_occurs=1, max_occurs=1)
    )
Population._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Population._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'cell_type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Population._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Population._ContentModel = pyxb.binding.content.ParticleModel(Population._GroupModel, min_occurs=1, max_occurs=1)



Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'connections'), Connections, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'target'), pyxb.binding.datatypes.string, scope=Projection, documentation=u'Cell population where synaptic connection terminates. NOTE: attribute values for source and target WILL BE THE PREFERRED FORMAT IN v2.0. The option for this element will be removed!'))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'connectivity_pattern'), ConnectivityPattern, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_props'), GlobalSynapticProperties, scope=Projection, documentation=u'Properties of a synapse associated with this connection.'))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Projection))

Projection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'source'), pyxb.binding.datatypes.string, scope=Projection, documentation=u'Cell population where synaptic connection begins. NOTE: attribute values for source and target WILL BE THE PREFERRED FORMAT IN v2.0. The option for this element will be removed!'))
Projection._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Projection._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'connections')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'connectivity_pattern')), min_occurs=1, max_occurs=1)
    )
Projection._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Projection._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'source')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'target')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Projection._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_props')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(Projection._GroupModel_2, min_occurs=1, max_occurs=1)
    )
Projection._ContentModel = pyxb.binding.content.ParticleModel(Projection._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), Initialisation, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))

Deprecated_VoltageGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageGate))
Deprecated_VoltageGate._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta')), min_occurs=1, max_occurs=1)
    )
Deprecated_VoltageGate._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta')), min_occurs=0L, max_occurs=1)
    )
Deprecated_VoltageGate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._GroupModel_2, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf')), min_occurs=0L, max_occurs=1)
    )
Deprecated_VoltageGate._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_VoltageGate._GroupModel, min_occurs=1, max_occurs=1)



Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'target'), InputTarget, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input'), PulseInput, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Input))

Input._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim'), RandomStim, scope=Input))
Input._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Input._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'pulse_input')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'random_stim')), min_occurs=1, max_occurs=1)
    )
Input._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Input._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Input._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'target')), min_occurs=1, max_occurs=1)
    )
Input._ContentModel = pyxb.binding.content.ParticleModel(Input._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cablegroup'), CableGroup, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable'), Cable, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_8))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_8))
CTD_ANON_8._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_8._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cablegroup')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_8._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel, min_occurs=1, max_occurs=1)



InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'sites'), InputSites, scope=InputTarget))

InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=InputTarget))

InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'site_pattern'), InputSitePattern, scope=InputTarget))

InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=InputTarget))

InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=InputTarget))

InputTarget._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=InputTarget))
InputTarget._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
InputTarget._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'sites')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputTarget._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'site_pattern')), min_occurs=1, max_occurs=1)
    )
InputTarget._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputTarget._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputTarget._GroupModel_2, min_occurs=1, max_occurs=1)
    )
InputTarget._ContentModel = pyxb.binding.content.ParticleModel(InputTarget._GroupModel, min_occurs=1, max_occurs=1)



NeuronDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=NeuronDBReference, documentation=u'Comment on how this neuron relates to the current model'))

NeuronDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), pyxb.binding.datatypes.string, scope=NeuronDBReference))

NeuronDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName'), pyxb.binding.datatypes.string, scope=NeuronDBReference))
NeuronDBReference._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(NeuronDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuronDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NeuronDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=1)
    )
NeuronDBReference._ContentModel = pyxb.binding.content.ParticleModel(NeuronDBReference._GroupModel, min_occurs=1, max_occurs=1)



ModelDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri'), pyxb.binding.datatypes.string, scope=ModelDBReference))

ModelDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName'), pyxb.binding.datatypes.string, scope=ModelDBReference))

ModelDBReference._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=ModelDBReference, documentation=u'Comment on how this model relates to the current model in NeuroML'))
ModelDBReference._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(ModelDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModelDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'uri')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ModelDBReference._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=1)
    )
ModelDBReference._ContentModel = pyxb.binding.content.ParticleModel(ModelDBReference._GroupModel, min_occurs=1, max_occurs=1)



DoubleExponentialSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=DoubleExponentialSynapse))

DoubleExponentialSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=DoubleExponentialSynapse))

DoubleExponentialSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=DoubleExponentialSynapse))

DoubleExponentialSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=DoubleExponentialSynapse))
DoubleExponentialSynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
DoubleExponentialSynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._GroupModel_, min_occurs=1, max_occurs=1)
    )
DoubleExponentialSynapse._ContentModel = pyxb.binding.content.ParticleModel(DoubleExponentialSynapse._GroupModel, min_occurs=1, max_occurs=1)



BlockingSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'block'), Block, scope=BlockingSynapse))
BlockingSynapse._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BlockingSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(BlockingSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(BlockingSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(BlockingSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
BlockingSynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BlockingSynapse._GroupModel_2, min_occurs=1, max_occurs=1)
    )
BlockingSynapse._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BlockingSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'block')), min_occurs=1, max_occurs=1)
    )
BlockingSynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(BlockingSynapse._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(BlockingSynapse._GroupModel_3, min_occurs=1, max_occurs=1)
    )
BlockingSynapse._ContentModel = pyxb.binding.content.ParticleModel(BlockingSynapse._GroupModel, min_occurs=1, max_occurs=1)



Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'properties'), Properties, scope=Segment, documentation=u'Some optional properties associated with the segment.'))

Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), Point, scope=Segment, documentation=u'The start point (and diameter) of the segment. If absent, it is assumed that the distal point of the parent is the start point of this segment.'))

Segment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), Point, scope=Segment, documentation=u'The end point (and diameter) of the segment. Note if the 3D location of the distal point is the same as the proximal point, the segment is assumed to be spherical.'))
Segment._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Segment._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Segment._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Segment._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'properties')), min_occurs=0L, max_occurs=1)
    )
Segment._ContentModel = pyxb.binding.content.ParticleModel(Segment._GroupModel, min_occurs=1, max_occurs=1)



Cells._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cell'), Cell, scope=Cells, documentation=u'A single cell.'))
Cells._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cells._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cell')), min_occurs=1, max_occurs=None)
    )
Cells._ContentModel = pyxb.binding.content.ParticleModel(Cells._GroupModel, min_occurs=1, max_occurs=1)



ElectricalSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=ElectricalSynapse))

ElectricalSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=ElectricalSynapse))

ElectricalSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=ElectricalSynapse))

ElectricalSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=ElectricalSynapse))
ElectricalSynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ElectricalSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ElectricalSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ElectricalSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ElectricalSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
ElectricalSynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ElectricalSynapse._GroupModel_, min_occurs=1, max_occurs=1)
    )
ElectricalSynapse._ContentModel = pyxb.binding.content.ParticleModel(ElectricalSynapse._GroupModel, min_occurs=1, max_occurs=1)



CellInstance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'location'), Point3D, scope=CellInstance))

CellInstance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CellInstance))

CellInstance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CellInstance))

CellInstance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CellInstance))

CellInstance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CellInstance))
CellInstance._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CellInstance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CellInstance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CellInstance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CellInstance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CellInstance._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CellInstance._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CellInstance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'location')), min_occurs=1, max_occurs=1)
    )
CellInstance._ContentModel = pyxb.binding.content.ParticleModel(CellInstance._GroupModel, min_occurs=1, max_occurs=1)


MultiDecaySynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MultiDecaySynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MultiDecaySynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MultiDecaySynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(MultiDecaySynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
MultiDecaySynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(MultiDecaySynapse._GroupModel_, min_occurs=1, max_occurs=1)
    )
MultiDecaySynapse._ContentModel = pyxb.binding.content.ParticleModel(MultiDecaySynapse._GroupModel, min_occurs=1, max_occurs=1)



CableGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'inhomogeneous_param'), InhomogeneousParam, scope=CableGroup))

CableGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable'), CTD_ANON_4, scope=CableGroup, documentation=u'The id of a single cable in the group'))
CableGroup._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CableGroup._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cable')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(CableGroup._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'inhomogeneous_param')), min_occurs=0L, max_occurs=None)
    )
CableGroup._ContentModel = pyxb.binding.content.ParticleModel(CableGroup._GroupModel, min_occurs=1, max_occurs=1)



StdpSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'spike_time_dep'), StdpDep, scope=StdpSynapse))
StdpSynapse._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(StdpSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(StdpSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(StdpSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(StdpSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
StdpSynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(StdpSynapse._GroupModel_2, min_occurs=1, max_occurs=1)
    )
StdpSynapse._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(StdpSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'spike_time_dep')), min_occurs=1, max_occurs=1)
    )
StdpSynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(StdpSynapse._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(StdpSynapse._GroupModel_3, min_occurs=1, max_occurs=1)
    )
StdpSynapse._ContentModel = pyxb.binding.content.ParticleModel(StdpSynapse._GroupModel, min_occurs=1, max_occurs=1)



Cable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Cable))

Cable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Cable))

Cable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Cable))

Cable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Cable))
Cable._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cable._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cable._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cable._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Cable._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Cable._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Cable._GroupModel_, min_occurs=1, max_occurs=1)
    )
Cable._ContentModel = pyxb.binding.content.ParticleModel(Cable._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygon'), Polygon, scope=CTD_ANON_10))
CTD_ANON_10._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygon')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_10._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_10._GroupModel, min_occurs=1, max_occurs=1)


Polygon._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Polygon._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'point')), min_occurs=1, max_occurs=None)
    )
Polygon._ContentModel = pyxb.binding.content.ParticleModel(Polygon._GroupModel, min_occurs=1, max_occurs=1)



Polyhedron._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygons'), CTD_ANON_10, scope=Polyhedron, documentation=u'Collection of polygons defining the polyhedron.'))
Polyhedron._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Polyhedron._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'polygons')), min_occurs=1, max_occurs=1)
    )
Polyhedron._ContentModel = pyxb.binding.content.ParticleModel(Polyhedron._GroupModel, min_occurs=1, max_occurs=1)



Sphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'center'), Point, scope=Sphere, documentation=u'Diameter of sphere is obtained from center Point.'))
Sphere._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Sphere._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'center')), min_occurs=1, max_occurs=1)
    )
Sphere._ContentModel = pyxb.binding.content.ParticleModel(Sphere._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'spine'), Spine, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_11))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_11))
CTD_ANON_11._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_11._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'spine')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_11._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel, min_occurs=1, max_occurs=1)



FacDepSynapse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'plasticity'), FacDep, scope=FacDepSynapse))
FacDepSynapse._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FacDepSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(FacDepSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(FacDepSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(FacDepSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
FacDepSynapse._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FacDepSynapse._GroupModel_2, min_occurs=1, max_occurs=1)
    )
FacDepSynapse._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FacDepSynapse._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'plasticity')), min_occurs=1, max_occurs=1)
    )
FacDepSynapse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(FacDepSynapse._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(FacDepSynapse._GroupModel_3, min_occurs=1, max_occurs=1)
    )
FacDepSynapse._ContentModel = pyxb.binding.content.ParticleModel(FacDepSynapse._GroupModel, min_occurs=1, max_occurs=1)



Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Connections))

Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Connections))

Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Connections))

Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'connection'), Connection, scope=Connections))

Connections._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Connections))
Connections._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Connections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Connections._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Connections._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Connections._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'connection')), min_occurs=1, max_occurs=None)
    )
Connections._ContentModel = pyxb.binding.content.ParticleModel(Connections._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_Transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_conc_gate'), Deprecated_VoltageConcGate, scope=Deprecated_Transition))

Deprecated_Transition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_gate'), Deprecated_VoltageGate, scope=Deprecated_Transition))
Deprecated_Transition._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(Deprecated_Transition._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_gate')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Transition._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'voltage_conc_gate')), min_occurs=1, max_occurs=1)
    )
Deprecated_Transition._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_Transition._GroupModel, min_occurs=1, max_occurs=1)



SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=SynapseProperties))

SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values'), SynapseInternalProperties, scope=SynapseProperties))

SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=SynapseProperties))

SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), pyxb.binding.datatypes.string, scope=SynapseProperties))

SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=SynapseProperties))

SynapseProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=SynapseProperties))
SynapseProperties._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
SynapseProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseProperties._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values')), min_occurs=1, max_occurs=1)
    )
SynapseProperties._ContentModel = pyxb.binding.content.ParticleModel(SynapseProperties._GroupModel, min_occurs=1, max_occurs=1)



IonProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), NamedParameter, scope=IonProperties))
IonProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IonProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter')), min_occurs=0L, max_occurs=None)
    )
IonProperties._ContentModel = pyxb.binding.content.ParticleModel(IonProperties._GroupModel, min_occurs=1, max_occurs=1)



SpecCapacitance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), VariableParameter, scope=SpecCapacitance, documentation=u'Note variable_parameter will be the preferred form in v2.0'))

SpecCapacitance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), UnnamedParameter, scope=SpecCapacitance))

SpecCapacitance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), VariableParameter, scope=SpecCapacitance, documentation=u'Note variable_parameter will be the preferred form in v2.0'))
SpecCapacitance._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpecCapacitance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SpecCapacitance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SpecCapacitance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter')), min_occurs=0L, max_occurs=None)
    )
SpecCapacitance._ContentModel = pyxb.binding.content.ParticleModel(SpecCapacitance._GroupModel, min_occurs=1, max_occurs=1)



SpecAxialResistance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), VariableParameter, scope=SpecAxialResistance, documentation=u'Note variable_parameter will be the preferred form in v2.0'))

SpecAxialResistance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), UnnamedParameter, scope=SpecAxialResistance))

SpecAxialResistance._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), VariableParameter, scope=SpecAxialResistance, documentation=u'Note variable_parameter will be the preferred form in v2.0'))
SpecAxialResistance._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SpecAxialResistance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SpecAxialResistance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SpecAxialResistance._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter')), min_occurs=0L, max_occurs=None)
    )
SpecAxialResistance._ContentModel = pyxb.binding.content.ParticleModel(SpecAxialResistance._GroupModel, min_occurs=1, max_occurs=1)



InitialMembPotential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), VariableParameter, scope=InitialMembPotential))

InitialMembPotential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), UnnamedParameter, scope=InitialMembPotential))
InitialMembPotential._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InitialMembPotential._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(InitialMembPotential._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter')), min_occurs=0L, max_occurs=None)
    )
InitialMembPotential._ContentModel = pyxb.binding.content.ParticleModel(InitialMembPotential._GroupModel, min_occurs=1, max_occurs=1)



Property._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'value'), pyxb.binding.datatypes.string, scope=Property))

Property._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'tag'), pyxb.binding.datatypes.string, scope=Property))
Property._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(Property._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'tag')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Property._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'value')), min_occurs=1, max_occurs=1)
    )
Property._ContentModel = pyxb.binding.content.ParticleModel(Property._GroupModel, min_occurs=0L, max_occurs=1)



Publication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'fullTitle'), pyxb.binding.datatypes.string, scope=Publication, documentation=u'A reasonably complete reference to the paper, etc. including journal, authors, issue, year. \n                    Mainly for quick recognition of the paper. The PubMed ref should contain the unique ID.'))

Publication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'pubmedRef'), pyxb.binding.datatypes.string, scope=Publication, documentation=u'URL of paper in PubMed (starting with http://www.ncbi.nlm.nih.gov)'))

Publication._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=Publication, documentation=u'Comment on how this publication relates to the current model'))
Publication._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(Publication._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'fullTitle')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Publication._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'pubmedRef')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Publication._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=1)
    )
Publication._ContentModel = pyxb.binding.content.ParticleModel(Publication._GroupModel, min_occurs=1, max_occurs=1)



RateAdjustments._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset'), Offset, scope=RateAdjustments))

RateAdjustments._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings'), Q10Settings, scope=RateAdjustments))
RateAdjustments._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RateAdjustments._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(RateAdjustments._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset')), min_occurs=0L, max_occurs=1)
    )
RateAdjustments._ContentModel = pyxb.binding.content.ParticleModel(RateAdjustments._GroupModel, min_occurs=1, max_occurs=1)



PoolVolumeInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'shell_thickness'), LengthValue, scope=PoolVolumeInfo, documentation=u'The volume of the pool is calculated from the thickness of the shell inside\n                    the membrane. This will have to be multiplied by the surface area of the relevant compartment. NOTE: In v2.0 the option for \n                    a shell_thickness element will be removed. Attribute shell_thickness will be used instead.'))
PoolVolumeInfo._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PoolVolumeInfo._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'shell_thickness')), min_occurs=0L, max_occurs=1)
    )
PoolVolumeInfo._ContentModel = pyxb.binding.content.ParticleModel(PoolVolumeInfo._GroupModel, min_occurs=1, max_occurs=1)



Gate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'state'), CTD_ANON_9, scope=Gate, documentation=u'Internal state of the gate, specifying a name, and possibly a fractional contribution. \n                    HHGate or KSGate elements will specify the rate equations, etc. for the gate, referencing this state name.'))
Gate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Gate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'state')), min_occurs=1, max_occurs=2L)
    )
Gate._ContentModel = pyxb.binding.content.ParticleModel(Gate._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetail'), PropertyDetail, scope=CTD_ANON_12))
CTD_ANON_12._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetail')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_12._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_12._GroupModel, min_occurs=1, max_occurs=1)



GlobalSynapticProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values'), SynapseInternalProperties, scope=GlobalSynapticProperties, documentation=u'For compatability to pre v1.7.1. Will be removed in v2.0.'))

GlobalSynapticProperties._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type'), pyxb.binding.datatypes.string, scope=GlobalSynapticProperties, documentation=u'For compatability to pre v1.7.1. Will be removed in v2.0.'))
GlobalSynapticProperties._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
GlobalSynapticProperties._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._GroupModel_2, min_occurs=1, max_occurs=1)
    )
GlobalSynapticProperties._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'synapse_type')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'default_values')), min_occurs=0L, max_occurs=1)
    )
GlobalSynapticProperties._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GlobalSynapticProperties._GroupModel_3, min_occurs=1, max_occurs=1)
    )
GlobalSynapticProperties._ContentModel = pyxb.binding.content.ParticleModel(GlobalSynapticProperties._GroupModel, min_occurs=1, max_occurs=1)



ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), NeuronDBReference, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'hh_gate'), Deprecated_HHGate, scope=ChannelType, documentation=u'Channel specification based on the Hodgkin Huxley formalism. Deprecated! Will be removed in v2.0'))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), ModelDBReference, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), Authors, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameters'), Parameters, scope=ChannelType, documentation=u'Fixed value parameters which can be used in generic expressions'))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), NeuroMorphoRef, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), Publication, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'impl_prefs'), ImplementationPrefs, scope=ChannelType, documentation=u'Optional recommended values, e.g. for size of tables, when creating an implementation of the \n                    channel mechanism on a specific simulator'))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ks_gate'), Deprecated_KSGate, scope=ChannelType, documentation=u'Channel specification based on a kinetic scheme formalism. Deprecated! Will be removed in v2.0'))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=ChannelType))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'current_voltage_relation'), CurrentVoltageRelation, scope=ChannelType, documentation=u'The specification of how the current flow etc. into the cell relates to the membrane potential \n                    difference (e.g. Ohmic relationship)'))

ChannelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), Status, scope=ChannelType, documentation=u'Status of the channel specification: stable, in progress, etc.'))
ChannelType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
ChannelType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
ChannelType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameters')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'current_voltage_relation')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'hh_gate')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ks_gate')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(ChannelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'impl_prefs')), min_occurs=0L, max_occurs=1)
    )
ChannelType._ContentModel = pyxb.binding.content.ParticleModel(ChannelType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate'), Gate, scope=CTD_ANON_13, documentation=u'Voltage/concentration dependent gate'))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'rate_adjustments'), RateAdjustments, scope=CTD_ANON_13, documentation=u'Adjustments, e.g. temperature dependence, to apply to the gating mechanisms'))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor'), ConcFactor, scope=CTD_ANON_13))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_13))
CTD_ANON_13._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_13._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_13._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'rate_adjustments')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_13._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_13._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_RateConstantEqn._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter'), Deprecated_Parameter, scope=Deprecated_RateConstantEqn, documentation=u'A parameter which is used in the equation'))
Deprecated_RateConstantEqn._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqn._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter')), min_occurs=0L, max_occurs=None)
    )
Deprecated_RateConstantEqn._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_RateConstantEqn._GroupModel, min_occurs=1, max_occurs=1)


Deprecated_AkdEquation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_AkdEquation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter')), min_occurs=3L, max_occurs=3L)
    )
Deprecated_AkdEquation._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_AkdEquation._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon'), Polygon, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron'), Polyhedron, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere'), Sphere, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_14))
CTD_ANON_14._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_14._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_14._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel_2, min_occurs=1, max_occurs=1)
    )
CTD_ANON_14._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel, min_occurs=1, max_occurs=1)



RectangularBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'size'), CTD_ANON_16, scope=RectangularBox, documentation=u'Size of box. Note if width, height or depth is zero, implies a lower dimension box, e.g. 2D plane.'))

RectangularBox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'corner'), Point, scope=RectangularBox, documentation=u'Location of vertex with lowest x, y, z coords.'))
RectangularBox._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RectangularBox._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'corner')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RectangularBox._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'size')), min_occurs=1, max_occurs=1)
    )
RectangularBox._ContentModel = pyxb.binding.content.ParticleModel(RectangularBox._GroupModel, min_occurs=1, max_occurs=1)



ConnectivityPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'all_to_all'), CTD_ANON_3, scope=ConnectivityPattern, documentation=u'Connect every pre cell to every post cell'))

ConnectivityPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'per_cell_connection'), PerCellConnection, scope=ConnectivityPattern, documentation=u'Connection built iteratively from each pre (or post) cell based on a number of parameters'))

ConnectivityPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'fixed_probability'), CTD_ANON_, scope=ConnectivityPattern, documentation=u'For each pre - post pair, there is a fixed probability of connection'))
ConnectivityPattern._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(ConnectivityPattern._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'all_to_all')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ConnectivityPattern._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'fixed_probability')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(ConnectivityPattern._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'per_cell_connection')), min_occurs=1, max_occurs=1)
    )
ConnectivityPattern._ContentModel = pyxb.binding.content.ParticleModel(ConnectivityPattern._GroupModel, min_occurs=1, max_occurs=1)



PotentialSynLoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=PotentialSynLoc))

PotentialSynLoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=PotentialSynLoc))

PotentialSynLoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'group'), pyxb.binding.datatypes.string, scope=PotentialSynLoc, documentation=u'List of groups of sections allowing the synapse'))

PotentialSynLoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=PotentialSynLoc))

PotentialSynLoc._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=PotentialSynLoc))
PotentialSynLoc._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynLoc._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynLoc._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynLoc._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynLoc._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
PotentialSynLoc._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynLoc._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'group')), min_occurs=1L, max_occurs=None)
    )
PotentialSynLoc._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PotentialSynLoc._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PotentialSynLoc._GroupModel_2, min_occurs=1, max_occurs=1)
    )
PotentialSynLoc._ContentModel = pyxb.binding.content.ParticleModel(PotentialSynLoc._GroupModel, min_occurs=1, max_occurs=1)



Spine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), Point, scope=Spine))

Spine._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), Point, scope=Spine))
Spine._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Spine._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Spine._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal')), min_occurs=0L, max_occurs=1)
    )
Spine._ContentModel = pyxb.binding.content.ParticleModel(Spine._GroupModel, min_occurs=1, max_occurs=1)



Instances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Instances))

Instances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Instances))

Instances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Instances))

Instances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Instances))

Instances._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'instance'), CellInstance, scope=Instances))
Instances._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Instances._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Instances._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Instances._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Instances._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Instances._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Instances._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Instances._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'instance')), min_occurs=1, max_occurs=None)
    )
Instances._ContentModel = pyxb.binding.content.ParticleModel(Instances._GroupModel, min_occurs=1, max_occurs=1)



PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=PopulationLocation))

PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=PopulationLocation))

PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=PopulationLocation))

PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'random_arrangement'), RandomArrangement, scope=PopulationLocation))

PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=PopulationLocation))

PopulationLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'grid_arrangement'), GridArrangement, scope=PopulationLocation))
PopulationLocation._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
PopulationLocation._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'random_arrangement')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PopulationLocation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'grid_arrangement')), min_occurs=1, max_occurs=1)
    )
PopulationLocation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(PopulationLocation._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PopulationLocation._GroupModel_2, min_occurs=1, max_occurs=1)
    )
PopulationLocation._ContentModel = pyxb.binding.content.ParticleModel(PopulationLocation._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_Parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Deprecated_Parameter))

Deprecated_Parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Deprecated_Parameter))

Deprecated_Parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Deprecated_Parameter))

Deprecated_Parameter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Deprecated_Parameter))
Deprecated_Parameter._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_Parameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Parameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Parameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Parameter._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Deprecated_Parameter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_Parameter._GroupModel_, min_occurs=1, max_occurs=1)
    )
Deprecated_Parameter._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_Parameter._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_Ohmic._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'conductance'), CTD_ANON_13, scope=Deprecated_Ohmic, documentation=u'Description of the conductance including maximum conductance density and possible (voltage and/or concentration dependent) gating mechanisms'))
Deprecated_Ohmic._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_Ohmic._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'conductance')), min_occurs=1, max_occurs=1)
    )
Deprecated_Ohmic._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_Ohmic._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_Ion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Deprecated_Ion))

Deprecated_Ion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Deprecated_Ion))

Deprecated_Ion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Deprecated_Ion))

Deprecated_Ion._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Deprecated_Ion))
Deprecated_Ion._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_Ion._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Ion._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Ion._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_Ion._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Deprecated_Ion._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_Ion._GroupModel, min_occurs=1, max_occurs=1)



SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), NeuroMorphoRef, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), Publication, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'electrical_syn'), ElectricalSynapse, scope=SynapseType, documentation=u'Electrical synaptic coupling as at a gap junction'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'multi_decay_syn'), MultiDecaySynapse, scope=SynapseType, documentation=u'An extension incorporating multiple decay time courses'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'blocking_syn'), BlockingSynapse, scope=SynapseType, documentation=u'For example NMDA receptor synapses'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'stdp_syn'), StdpSynapse, scope=SynapseType, documentation=u'A synaptic mechanism implementing basic Spike Timing Dependent Plasticity based on Song and Abbott, 2001'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), NeuronDBReference, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), ModelDBReference, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), Authors, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), Status, scope=SynapseType, documentation=u'Status of the synapse specification: stable, in progress, etc.'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=SynapseType))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'fac_dep_syn'), FacDepSynapse, scope=SynapseType, documentation=u'A facilitating and depressing synaptic mechanism'))

SynapseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'doub_exp_syn'), DoubleExponentialSynapse, scope=SynapseType, documentation=u'Synaptic conductance with rise time and decay time'))
SynapseType._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
SynapseType._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
SynapseType._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'electrical_syn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'doub_exp_syn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'blocking_syn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'multi_decay_syn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'fac_dep_syn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'stdp_syn')), min_occurs=1, max_occurs=1)
    )
SynapseType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(SynapseType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(SynapseType._GroupModel_3, min_occurs=1, max_occurs=1)
    )
SynapseType._ContentModel = pyxb.binding.content.ParticleModel(SynapseType._GroupModel, min_occurs=1, max_occurs=1)



IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_species'), IonSpecies, scope=IonConcentration, documentation=u'Which ion is involved in mechanism.'))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication'), Publication, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef'), NeuroMorphoRef, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'status'), Status, scope=IonConcentration, documentation=u'Status of the ion conc mech specification: stable, in progress, etc.'))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'decaying_pool_model'), DecayingPoolModel, scope=IonConcentration, documentation=u'At present there is only one choice of a model for this process,\n                        more can be added later..'))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref'), NeuronDBReference, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref'), ModelDBReference, scope=IonConcentration))

IonConcentration._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList'), Authors, scope=IonConcentration))
IonConcentration._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
IonConcentration._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'authorList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'publication')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuronDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'modelDBref')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'neuroMorphoRef')), min_occurs=0L, max_occurs=None)
    )
IonConcentration._GroupModel_3 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'decaying_pool_model')), min_occurs=1, max_occurs=1)
    )
IonConcentration._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'status')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._GroupModel_2, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ion_species')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(IonConcentration._GroupModel_3, min_occurs=1, max_occurs=1)
    )
IonConcentration._ContentModel = pyxb.binding.content.ParticleModel(IonConcentration._GroupModel, min_occurs=1, max_occurs=1)



Status._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'contributor'), Person, scope=Status, documentation=u'Who added the comments?'))

Status._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment'), pyxb.binding.datatypes.string, scope=Status, documentation=u'A comment on the current status. Not necessarily signalling a problem.'))

Status._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'issue'), pyxb.binding.datatypes.string, scope=Status, documentation=u'An issue which need addressing'))
Status._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Status._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'comment')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Status._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'issue')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Status._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'contributor')), min_occurs=0L, max_occurs=None)
    )
Status._ContentModel = pyxb.binding.content.ParticleModel(Status._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence'), ConcDependence, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha'), Deprecated_RateConstVoltConcDep, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau'), Deprecated_RateConstVoltConcDep, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma'), Deprecated_RateConstantEqnChoice, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta'), Deprecated_RateConstVoltConcDep, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf'), Deprecated_RateConstVoltConcDep, scope=Deprecated_VoltageConcGate))

Deprecated_VoltageConcGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation'), Initialisation, scope=Deprecated_VoltageConcGate))
Deprecated_VoltageConcGate._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'alpha')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'beta')), min_occurs=1, max_occurs=1)
    )
Deprecated_VoltageConcGate._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'gamma')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'zeta')), min_occurs=0L, max_occurs=1)
    )
Deprecated_VoltageConcGate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'initialisation')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._GroupModel_, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._GroupModel_2, min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'tau')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'inf')), min_occurs=0L, max_occurs=1)
    )
Deprecated_VoltageConcGate._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_VoltageConcGate._GroupModel, min_occurs=1, max_occurs=1)



Parameters._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter'), Parameter, scope=Parameters))
Parameters._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Parameters._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'parameter')), min_occurs=1L, max_occurs=None)
    )
Parameters._ContentModel = pyxb.binding.content.ParticleModel(Parameters._GroupModel, min_occurs=1, max_occurs=1)



CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset'), Offset, scope=CurrentVoltageRelation, documentation=u'Preferred location of offset information since v1.7.3. '))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence'), ConcDependence, scope=CurrentVoltageRelation, documentation=u'Preferred location of conc_dependence since v1.7.3. '))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor'), ConcFactor, scope=CurrentVoltageRelation, documentation=u'Preferred location of conc_factor since v1.7.3. '))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'ohmic'), Deprecated_Ohmic, scope=CurrentVoltageRelation, documentation=u'Deprecated since v1.7.3. Use attribute cond_law and gate elements below this element instead. '))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate'), GatingComplex, scope=CurrentVoltageRelation, documentation=u'Preferred way of expressing gating complexes since v1.7.3. '))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'integrate_and_fire'), IntegrateAndFire, scope=CurrentVoltageRelation, documentation=u'Note: use attribute cond_law="integrate_and_fire" and no other attributes here when using this. \n                    Signifies a current which will cause the cell to behave like an integrate and fire neuron'))

CurrentVoltageRelation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings'), Q10Settings, scope=CurrentVoltageRelation, documentation=u'Preferred location of Q10 information since v1.7.3. '))
CurrentVoltageRelation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'ohmic')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'integrate_and_fire')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_dependence')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'conc_factor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'q10_settings')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'offset')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CurrentVoltageRelation._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'gate')), min_occurs=0L, max_occurs=None)
    )
CurrentVoltageRelation._ContentModel = pyxb.binding.content.ParticleModel(CurrentVoltageRelation._GroupModel, min_occurs=1, max_occurs=1)



InputSites._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=InputSites))

InputSites._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'site'), InputSite, scope=InputSites))

InputSites._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=InputSites))

InputSites._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=InputSites))

InputSites._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=InputSites))
InputSites._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputSites._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSites._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSites._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSites._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
InputSites._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InputSites._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InputSites._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'site')), min_occurs=1, max_occurs=None)
    )
InputSites._ContentModel = pyxb.binding.content.ParticleModel(InputSites._GroupModel, min_occurs=1, max_occurs=1)



ImplementationPrefs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'comment'), pyxb.binding.datatypes.string, scope=ImplementationPrefs, documentation=u'Comment element to give explination for the implementation preferences. Having a dedicated element as opposed to a <-- comment --> allows the comment to be repeated in the script file impl. '))

ImplementationPrefs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'table_settings'), CTD_ANON_2, scope=ImplementationPrefs, documentation=u'Preferences for the table of values for the rate equations, e.g. used in the TABLE statement in NMODL, or in tabchannel GENESIS objects'))
ImplementationPrefs._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(ImplementationPrefs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'comment')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(ImplementationPrefs._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'table_settings')), min_occurs=0L, max_occurs=1)
    )
ImplementationPrefs._ContentModel = pyxb.binding.content.ParticleModel(ImplementationPrefs._GroupModel, min_occurs=1, max_occurs=1)



InhomogeneousParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal'), CTD_ANON_6, scope=InhomogeneousParam, documentation=u'Information on the value of the variable at the proximal point. If this element is absent,\n                    the value of the variable is determined simply from the metric, e.g. absolute path length'))

InhomogeneousParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'metric'), Metric, scope=InhomogeneousParam, documentation=u'The metric used to determine the variable'))

InhomogeneousParam._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal'), CTD_ANON_7, scope=InhomogeneousParam, documentation=u'Information on the value of the variable at the distal point. If this element is absent, the\n                    value of the variable is determined simply from the metric, e.g. path length'))
InhomogeneousParam._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(InhomogeneousParam._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'metric')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(InhomogeneousParam._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'proximal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(InhomogeneousParam._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'distal')), min_occurs=0L, max_occurs=1)
    )
InhomogeneousParam._ContentModel = pyxb.binding.content.ParticleModel(InhomogeneousParam._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'feature'), Feature, scope=CTD_ANON_17, documentation=u'A single feature of note.'))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_17))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_17))
CTD_ANON_17._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_17._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'feature')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_17._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel, min_occurs=1, max_occurs=1)



Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron'), Polyhedron, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'path'), Path, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere'), Sphere, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints'), FreePoints, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'manifold'), Manifold, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon'), Polygon, scope=Feature))

Feature._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Feature))
Feature._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Feature._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Feature._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'path')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'freePoints')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'manifold')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'polygon')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'polyhedron')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Feature._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'sphere')), min_occurs=0L, max_occurs=None)
    )
Feature._ContentModel = pyxb.binding.content.ParticleModel(Feature._GroupModel, min_occurs=1, max_occurs=1)


Path._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Path._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'point')), min_occurs=1, max_occurs=None)
    )
Path._ContentModel = pyxb.binding.content.ParticleModel(Path._GroupModel, min_occurs=1, max_occurs=1)


Manifold._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Manifold._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'point')), min_occurs=1, max_occurs=None)
    )
Manifold._ContentModel = pyxb.binding.content.ParticleModel(Manifold._GroupModel, min_occurs=1, max_occurs=1)



PropertyDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'type'), pyxb.binding.datatypes.anyType, scope=PropertyDetail))

PropertyDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'description'), pyxb.binding.datatypes.string, scope=PropertyDetail))
PropertyDetail._GroupModel = pyxb.binding.content.GroupAll(
    pyxb.binding.content.ParticleModel(PropertyDetail._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(PropertyDetail._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'type')), min_occurs=1, max_occurs=1)
    )
PropertyDetail._ContentModel = pyxb.binding.content.ParticleModel(PropertyDetail._GroupModel, min_occurs=1, max_occurs=1)



NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=NetworkML))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'populations'), Populations, scope=NetworkML, documentation=u"The least that's needed in a network is a population of cells..."))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=NetworkML))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'projections'), Projections, scope=NetworkML, documentation=u'In theory there can be no projections, if the file is intended only to specify positions'))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=NetworkML))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=NetworkML))

NetworkML._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs'), Inputs, scope=NetworkML, documentation=u'No inputs need be specified'))
NetworkML._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
NetworkML._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'populations')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'projections')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'inputs')), min_occurs=0L, max_occurs=1)
    )
NetworkML._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(NetworkML._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(NetworkML._GroupModel_2, min_occurs=1, max_occurs=1)
    )
NetworkML._ContentModel = pyxb.binding.content.ParticleModel(NetworkML._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetail'), GroupDetail, scope=CTD_ANON_18))
CTD_ANON_18._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetail')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_18._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_18._GroupModel, min_occurs=1, max_occurs=1)



Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=Morphology))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetails'), CTD_ANON_18, scope=Morphology, documentation=u'Collection of all GroupDetails for this instance.'))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'cells'), Cells, scope=Morphology))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetails'), CTD_ANON_12, scope=Morphology, documentation=u'Collection of all PropertyDetails for this instance.'))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=Morphology))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=Morphology))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=Morphology))

Morphology._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'features'), CTD_ANON_17, scope=Morphology, documentation=u'Collection of all extracellular histological features.'))
Morphology._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
Morphology._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Morphology._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'cells')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'features')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'propertyDetails')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(Morphology._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'groupDetails')), min_occurs=0L, max_occurs=1)
    )
Morphology._ContentModel = pyxb.binding.content.ParticleModel(Morphology._GroupModel, min_occurs=1, max_occurs=1)



Mechanism._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter'), VariableNamedParameter, scope=Mechanism, documentation=u'Note variable_parameter will be the preferred form in v2.0'))

Mechanism._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter'), VariableNamedParameter, scope=Mechanism, documentation=u'Note variable_parameter will be the preferred form in v2.0'))

Mechanism._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter'), NamedParameter, scope=Mechanism))
Mechanism._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Mechanism._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'parameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Mechanism._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variableParameter')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(Mechanism._UseForTag(pyxb.namespace.ExpandedName(_Namespace_bio, u'variable_parameter')), min_occurs=0L, max_occurs=None)
    )
Mechanism._ContentModel = pyxb.binding.content.ParticleModel(Mechanism._GroupModel, min_occurs=1, max_occurs=1)



GroupDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=GroupDetail))

GroupDetail._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'description'), pyxb.binding.datatypes.string, scope=GroupDetail))
GroupDetail._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GroupDetail._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'description')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GroupDetail._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=None)
    )
GroupDetail._ContentModel = pyxb.binding.content.ParticleModel(GroupDetail._GroupModel, min_occurs=1, max_occurs=1)



RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=RandomArrangement))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'spherical_location'), Sphere, scope=RandomArrangement))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=RandomArrangement))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=RandomArrangement))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location'), RectangularBox, scope=RandomArrangement))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'population_size'), pyxb.binding.datatypes.nonNegativeInteger, scope=RandomArrangement, documentation=u'Number of cells to place randomly in the specified 3D location'))

RandomArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=RandomArrangement))
RandomArrangement._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
RandomArrangement._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'spherical_location')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location')), min_occurs=1, max_occurs=1)
    )
RandomArrangement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(RandomArrangement._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'population_size')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(RandomArrangement._GroupModel_2, min_occurs=1, max_occurs=1)
    )
RandomArrangement._ContentModel = pyxb.binding.content.ParticleModel(RandomArrangement._GroupModel, min_occurs=1, max_occurs=1)



GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location'), RectangularBox, scope=GridArrangement, documentation=u'3D box in which the cells are regularly packed. Note if one or two of dimensions of the box is zero it can be a 2D or 1D grid (respectively).'))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=GridArrangement))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=GridArrangement))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'spacing'), CTD_ANON_15, scope=GridArrangement, documentation=u'Separation of the cells in each dimension'))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=GridArrangement))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_net, u'non_spatial_grid'), NonSpatialGrid, scope=GridArrangement, documentation=u'Specifying this means the precise spatial location of the cells is irrelvant'))

GridArrangement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=GridArrangement))
GridArrangement._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
GridArrangement._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'rectangular_location')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'spacing')), min_occurs=1, max_occurs=1)
    )
GridArrangement._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(GridArrangement._GroupModel_3, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._UseForTag(pyxb.namespace.ExpandedName(_Namespace_net, u'non_spatial_grid')), min_occurs=1, max_occurs=1)
    )
GridArrangement._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(GridArrangement._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(GridArrangement._GroupModel_2, min_occurs=1, max_occurs=1)
    )
GridArrangement._ContentModel = pyxb.binding.content.ParticleModel(GridArrangement._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation'), Annotation, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_mml, u'segment'), Segment, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes'), Notes, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'group'), Group, scope=CTD_ANON_19))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties'), Properties, scope=CTD_ANON_19))
CTD_ANON_19._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'notes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'properties')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'annotation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_meta, u'group')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_19._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_19._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(_Namespace_mml, u'segment')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_19._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_19._GroupModel, min_occurs=1, max_occurs=1)



Deprecated_KSGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition'), Deprecated_Transition, scope=Deprecated_KSGate))

Deprecated_KSGate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_cml, u'state'), Deprecated_KSState, scope=Deprecated_KSGate))
Deprecated_KSGate._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(Deprecated_KSGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'state')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(Deprecated_KSGate._UseForTag(pyxb.namespace.ExpandedName(_Namespace_cml, u'transition')), min_occurs=1, max_occurs=None)
    )
Deprecated_KSGate._ContentModel = pyxb.binding.content.ParticleModel(Deprecated_KSGate._GroupModel, min_occurs=1, max_occurs=1)
