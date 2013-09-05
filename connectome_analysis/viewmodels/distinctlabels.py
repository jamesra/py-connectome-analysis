'''
Created on Jul 10, 2013

@author: u0490822
'''

from connectome_analysis.datamodels import queries


def UniqueLabel(label):
    '''
    Returns the portion of the label not within []'s
    '''

    if label is None:
        return None

    label = str(label)

    if len(label) == 0:
        return None

    iBracket = label.find('[')

    if iBracket >= 0:
        truncLabel = label[:iBracket]
        label = truncLabel.strip()

    iParen = label.find("(")
    if iParen >= 0:
        truncLabel = label[:iParen]
        label = truncLabel.strip()

    return label


def LabelsForStructures(structs=None):
    structLabels = {}

    if structs is None:
        structs = queries.GetStructuresWithLabels()

    for s in structs:
        label = UniqueLabel(s.Label)

        if not label in structLabels:
            structLabels[label] = [s]
            print label
        else:
            structLabels[label].append(s)

    return structLabels


