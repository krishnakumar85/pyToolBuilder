'''
Created on 30-Jun-2012

@author: krishna
'''


class SimpleLogger(object):
    '''
    classdocs
    '''

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.logfile = filename

    # TODO: make this multi-arg to accept params
    def log(self, msg):
        print >>self.logfile, msg
