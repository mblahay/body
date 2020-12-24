#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:51:52 2017

@author: Michael Blahay

Created this because there is no good way use common unix utilities to crop a file
down to some portion of the middle. In particular, there isn't a good way to remove
a specified number of lines from the end of a file without first knowing the number
of lines in the file*. Though, this can be done, it would require multiple passes
through a file. For a stream, multiple passes would be impossible unless the stream
is first saved to a file, which may not be reasonable depending on the size of the 
stream.

*Turns out that head and tail do offer the desired functionality when used together
with the -n switch. It is not very well documented, but is possible. Will continue
to work with this project to pilot other skills.
"""

import sys
import argparse
import logging
from collections import deque

def body(iterobject, head=0, tail=0):
    'This is the method where the magic happens. The method is a generator that will process through an interable and output the desired elements.'
    
    lg = logging.getLogger(__name__)
    lg.debug('Entering into generator head = %s, tail = %s', head, tail)
    
    rn = 0 #variable for tracking record number

    cache = deque()  #initializing the cache. The cache is what allow us to crop at the end of the file
    lg.debug('Beginning iteration')
    
    for l in iterobject:     #Please note that the more there is to be removed from the end of the file, the larger the cache, and the larger the cache, the more memory is consumed.
        lg.debug("l = %s", l)
        rn+=1
        lg.debug('rn = %s', rn)    
        if rn > head:
            cache.append(l)
            lg.debug('cache = %s',cache)

        if rn > head + tail:
            yield cache.popleft()

def initializeLogger():
    '''
    This function simply contains an encapsolation of the logger setup.
    The code was refactored from the main execution.
    '''
    lg = logging.getLogger(__name__)
    hd = logging.StreamHandler()
    hd.setLevel(logging.DEBUG)
    hd.setFormatter(logging.Formatter('%(asctime)s  %(levelname)s: %(message)s'))
    lg.addHandler(hd)
    return lg
