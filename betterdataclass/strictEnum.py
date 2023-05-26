
from typing import Type, get_origin
from betterdataclass import StrictDictionary

class EnumMember:
    def __init__(self) -> None:
        pass

class StrictEnum:
    def __init__(self,type) -> None:
        pass
    def __init_subclass__(cls,Ttype) -> None:
        
        # for key, value in cls.__dict__:
        #     pass
        pass
            
"""

"""
class x(StrictEnum):
    d="sdsd"
    d2="fff"
class y(StrictDictionary):
    tyi:x
    
x=y()
x.tyi="Something"