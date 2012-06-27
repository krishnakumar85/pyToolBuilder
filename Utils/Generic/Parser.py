'''
Created on 27-Jun-2012

@author: krishna
'''
import ConfigParser


class Config(object):
    '''
    classdocs
    '''

    def __init__(self, filename):
        '''
        Constructor
        '''
        self.file = filename
        print filename

    def parse(self):
        self.confobj = ConfigParser.ConfigParser()
        self.confobj.read('..\\config.txt')
        print self.confobj.defaults()

    def __getattr__(self, name):
        print name
        out = self.confobj.sections()
        print out

        print out['auth']['atrpo_login']
        print 'ver --'
        #sec = self.confobj.get(name)

        #return object.__getattribute__(self, *args, **kwargs)
