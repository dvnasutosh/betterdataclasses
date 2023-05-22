from collections.abc import Iterable
from typing_extensions import SupportsIndex
from typing import Any

from .helper.validate import validate

class StrictList(list):
    """
    """
    def __init__(self,*data) -> None:
        for each in data:
            if not self.restriction(each):
                raise ValueError(f"Data does not follow restrictions set for {self.__class__}")

            if any(not validate(annot=t, value=each) for t in self.types):
                raise TypeError(f'value {each} is not of type {self.types}. It\'s of type {type(each)} ')
            super().__init__(data)
    
    def __init_subclass__(cls):
        if 'types' not in cls.__dict__.keys():
            cls.types=[Any]
        elif any(type(i) != type(int) for i in cls.__dict__['types']):
            raise ValueError('the types must only contain `type` objects. ')
        else:
            cls.types= cls.__dict__['types']
        super().__init_subclass__()

    def restriction(self,i): 
        # OverWrite this to add Restriction
        return True
    def validate(self,data):
        '''
            Validates if the data follows all required criteria
        '''
        if not self.restriction(data):
            raise ValueError(f"The {data} data doesn't follow our provided restrictions")
        if not any(validate(annot=t, value=data) for t in self.types):
            raise TypeError(f'value {data} is not of type {self.types}. It\'s of type {type(data)} ')
    def append(self, __object: Any) -> None:
        
        self.validate(__object)
        return super().append(__object)
    
    def extend(self, __iterable: Iterable) -> None:
        for each in __iterable:    
            self.validate(each)
        
        return super().extend(__iterable)
    
    def insert(self, __index: SupportsIndex, __object: Any) -> None:
        
        self.validate(__object)
        
        return super().insert(__index, __object)
