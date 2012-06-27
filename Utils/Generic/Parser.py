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
        self.conf = None

        print filename

    def parse(self):
        self.confobj = ConfigParser.RawConfigParser()
        open(self.file, 'r').close()
        self.confobj.read(self.file)

    def __getattr__(self, name):
        print name
        sections = self.confobj.sections()
        #print sections
        if name in sections:
            self.conf = self.confobj.items(name)

        dictconf = {}
        for tupconf in self.conf:
            dictconf[tupconf[0]] = tupconf[1]

        return dictconf
        #sec = self.confobj.get(name)

        #return object.__getattribute__(self, *args, **kwargs)
