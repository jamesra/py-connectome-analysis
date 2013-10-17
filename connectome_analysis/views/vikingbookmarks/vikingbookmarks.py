# .\vikingbookmarks.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6312b9b02a52b1433df543544669f2e4527eef82
# Generated 2013-10-17 10:25:56.242000 by PyXB version 1.2.3
# Namespace http://connectomes.utah.edu/XSD/BookmarkSchema.xsd

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2e6e8340-3751-11e3-aa18-10bf480cb10f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://connectomes.utah.edu/XSD/BookmarkSchema.xsd', create_if_missing=True)
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


# Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}position with content type EMPTY
class position (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}position with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'position')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute X uses Python identifier X
    __X = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'X'), 'X', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_position_X', pyxb.binding.datatypes.double, required=True)
    __X._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 11, 4)
    __X._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 11, 4)
    
    X = property(__X.value, __X.set, None, None)

    
    # Attribute Y uses Python identifier Y
    __Y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Y'), 'Y', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_position_Y', pyxb.binding.datatypes.double, required=True)
    __Y._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 12, 4)
    __Y._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 12, 4)
    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Attribute Z uses Python identifier Z
    __Z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Z'), 'Z', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_position_Z', pyxb.binding.datatypes.double, required=True)
    __Z._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 13, 4)
    __Z._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 13, 4)
    
    Z = property(__Z.value, __Z.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __X.name() : __X,
        __Y.name() : __Y,
        __Z.name() : __Z
    })
Namespace.addCategoryObject('typeBinding', u'position', position)


# Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}view with content type EMPTY
class view (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}view with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'view')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Downsample uses Python identifier Downsample
    __Downsample = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Downsample'), 'Downsample', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_view_Downsample', pyxb.binding.datatypes.double, required=True)
    __Downsample._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 17, 4)
    __Downsample._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 17, 4)
    
    Downsample = property(__Downsample.value, __Downsample.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Downsample.name() : __Downsample
    })
Namespace.addCategoryObject('typeBinding', u'view', view)


# Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}bookmark with content type ELEMENT_ONLY
class bookmark (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}bookmark with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'bookmark')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 20, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}Position uses Python identifier Position
    __Position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Position'), 'Position', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_bookmark_httpconnectomes_utah_eduXSDBookmarkSchema_xsdPosition', False, pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 22, 6), )

    
    Position = property(__Position.value, __Position.set, None, None)

    
    # Element {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}View uses Python identifier View
    __View = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'View'), 'View', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_bookmark_httpconnectomes_utah_eduXSDBookmarkSchema_xsdView', False, pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 23, 6), )

    
    View = property(__View.value, __View.set, None, None)

    
    # Element {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Comment'), 'Comment', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_bookmark_httpconnectomes_utah_eduXSDBookmarkSchema_xsdComment', False, pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 24, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_bookmark_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 26, 4)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 26, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Position.name() : __Position,
        __View.name() : __View,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'bookmark', bookmark)


# Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}folder with content type ELEMENT_ONLY
class folder (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}folder with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'folder')
    _XSDLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}Folder uses Python identifier Folder
    __Folder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Folder'), 'Folder', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_folder_httpconnectomes_utah_eduXSDBookmarkSchema_xsdFolder', True, pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 31, 6), )

    
    Folder = property(__Folder.value, __Folder.set, None, None)

    
    # Element {http://connectomes.utah.edu/XSD/BookmarkSchema.xsd}Bookmark uses Python identifier Bookmark
    __Bookmark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Bookmark'), 'Bookmark', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_folder_httpconnectomes_utah_eduXSDBookmarkSchema_xsdBookmark', True, pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 32, 6), )

    
    Bookmark = property(__Bookmark.value, __Bookmark.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpconnectomes_utah_eduXSDBookmarkSchema_xsd_folder_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 34, 4)
    __name._UseLocation = pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 34, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Folder.name() : __Folder,
        __Bookmark.name() : __Bookmark
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'folder', folder)


Folder = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Folder'), folder, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 37, 2))
Namespace.addCategoryObject('elementBinding', Folder.name().localName(), Folder)

Bookmark = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bookmark'), bookmark, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', Bookmark.name().localName(), Bookmark)



bookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Position'), position, scope=bookmark, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 22, 6)))

bookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'View'), view, scope=bookmark, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 23, 6)))

bookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Comment'), pyxb.binding.datatypes.string, scope=bookmark, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 24, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bookmark._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Position')), pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 22, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bookmark._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'View')), pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(bookmark._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Comment')), pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 24, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
bookmark._Automaton = _BuildAutomaton()




folder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Folder'), folder, scope=folder, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 31, 6)))

folder._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Bookmark'), bookmark, scope=folder, location=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 32, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 30, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 31, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 32, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(folder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Folder')), pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(folder._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Bookmark')), pyxb.utils.utility.Location('C:\\Src\\Git\\py-connectome-analysis\\connectome_analysis\\views\\vikingbookmarks\\BookmarkSchema.xsd', 32, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
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
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
folder._Automaton = _BuildAutomaton_()

