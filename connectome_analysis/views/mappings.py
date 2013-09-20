'''
Created on Jun 19, 2013

@author: u0490822
'''

def SplitLabelTags(tags):
    '''Labels may have multiple tags within brackets seperated by a semicolon'''
    if tags is None:
        return []

    if len(tags) == 0:
        return []

    taglist = tags.split(',')
    taglist = map(str.strip, taglist)
    return taglist


def LabelParts(label):
    '''Returns a tuble with the first part containing the label with any []'s removed
       The second part contains the contents within the brackets'''

    if label is None:
        return "Unlabeled"

    if len(label) == 0:
        return "Unlabeled"

    iBracket = label.find('[')
    baselabel = label
    tagList = []
    if iBracket >= 0:
        baselabel = label[:iBracket]

        tagStr = label[iBracket + 1:]

        iendBracket = tagStr.rfind(']')
        if iendBracket >= 0:
            tagStr = tagStr[:iendBracket]

        tagList = SplitLabelTags(tagStr.strip())

    baselabel = baselabel.strip()

    return (baselabel, tagList)


# def UniqueLabels(LabelList):
#    '''Return a list of unique label names, ignoring case.  Comments and tags with [] are ignored'''
 #   pass


if __name__ == '__main__':
    pass

