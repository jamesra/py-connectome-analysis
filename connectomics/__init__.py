def enum(*sequential, **named):
    '''Generates a dictionary of names to number values used as an enumeration.
       Copied from a StackOverflow post'''
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)