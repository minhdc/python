'''
Created on Jan 30, 2018

@author: extre_000
'''
class _const:
    class ConstError(TypeError): pass
    
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't rebind const (%s)"%name
        self.__dict__[name] = value
     
    def __delattr_(self,name):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't unbind const (%s)"%name
        raise NameError,name

import sys
sys.modules[__name__] = _const()
