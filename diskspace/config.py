__author__ = 'michogarcia'

import yaml

class Config():

    __configfile__ = '../config.yaml'

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
