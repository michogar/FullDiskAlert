__author__ = 'michogarcia'

import yaml
import os
import diskspace

class Config():

    path = os.path.abspath(diskspace.__file__)
    tmppath = os.path.join(path, os.pardir, os.pardir)
    dir_path = os.path.abspath(tmppath)
    __configfile__ = dir_path + '/config.yaml'

    path = "/"
    threshold = 90
    receivers = None
    email = None
    host = None

    def __init__(self):
        '''

        '''
        f = open(self.__configfile__, 'r')
        data = yaml.load(f)

        self.path = data['path']
        self.threshold = data['threshold']
        self.receivers = data['receivers']
        self.email = data['email']
        self.host = data['host']
        f.close()
