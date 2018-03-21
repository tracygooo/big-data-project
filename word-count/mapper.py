#!/usr/bin/env python

# Refer to http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

import sys
# Read each line from stdin
for line in sys.stdin:

# Get the words in each line
    words = line.split()

    # Generate the count for each word
    for word in words:

    # Write the key-value pair to stdout to be processed by
    # the reducer.
    # The key is anything before the first tab character and the
    # value is anything after the first tab character.

        '''
        str.format(*args, **kwargs), perform a string formatting operation. 

        The string on which this method is called can contain literal text or replacement fields 
        delimited by braces {}. 

        Each replacement field contains either the numeric index of a positional argument, 
        or the name of a keyword argument. 

        Returns a copy of the string where each replacement field is replaced with 
        the string value of the corresponding argument.
        '''

        print '{0}\t{1}'.format(word, 1)
