
from typing import get_args, get_args, get_args, Final, Final, Final, Any,get_origin

import json
# from .helper.to_dict import to_raw_dict
from .helper.validate import validate
from .helper.initiate import initialize

class Dictionary(object):
    """
    A class that can be used to create a dictionary-like object with arbitrary key-value pairs.
    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the object with the given keyword arguments.
        If no arguments are given, the attributes are set to `None`.
        """
        # Iterate over the class annotations and set the attributes
        # based on the given keyword arguments
        for i,j in self.__annotations__.items():
            try:
                self.__data__= getattr(self,i)
            except AttributeError:
                self.__data__[i]=None
        kwargs = kwargs or {}

        for i, j in kwargs.items():
            self.__data__[i] = j
        
    def __repr__(self) -> str:
        """
        Returns a string representation of the object's dictionary.
        """
        return str(self.__raw__())
    
    def __call__(self,raw:bool=False) -> dict:
        return self.__raw__() if raw else self.__data__
    
    def __str__(self):
        return str(self.__raw__())

    def __json__(self):
        return json.dumps(self.__raw__())
    
    def __raw__(self):
        # print(type(self.__data__['nested']))
        from .helper.to_dict import to_raw_dict
        return to_raw_dict(self.__data__)

    def __setitem__(self, name, value) -> None:
        """
        Provides indexing and assignment functionality to the object.
        """
        self.__data__[name]=value
        

    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__data__[__name]=__value
    
    def __getattribute__(self, __name: str) -> Any:
        if __name in super().__getattribute__("__data__").keys():
            return super().__getattribute__('__data__')[__name]
        else:
            return super().__getattribute__(__name)
    

    def __getitem__(self, name) -> Any:
        """
        Provides indexing and retrieval functionality to the object.
        """
        return self.__data__[name]

class StrictDictionary(Dictionary):
    """
    A subclass of `Dictionary` that enforces strict typing of the values based on the annotations of the class attributes.
    precaution: dont use Enum. Cant be converted into JSON 
    """
    def __init__(self, **kwargs) -> None:
        """
        Initialize any given data to be stored. The default datas are stored regardless 
        """
        # Adding default values
        for i,j in self.__data__.items():
            super().__setitem__(i,j)
        if kwargs:
            # if kwargs exists adding all the given values using super class
            
            for i,j in kwargs.items():
                
                #SECTION: validation logic 
                if not validate(self.__annotations__[i],j):
                    raise TypeError(
                        f'{i} key has a value {j} which is of type {type(j)}. {self.__annotations__[i]} expected.')
                #!SECTION
                
                super().__setitem__(i,j)
                # NOTE: If it is in data AND NOT IN annot than 
    
    def __init_subclass__(cls) -> None:
        cls.__data__= {}
        
        for k,v in cls.__dict__.items():
            if len(k)>=2 and k[0]!='_' and k[1]!='_':
                # Handling when it is present in dict but not in annot.(It will default to What is provided)
                if k not in cls.__annotations__:
                    pass
                elif Final == cls.__annotations__[k]:
                    pass         
                elif Final == get_origin(cls.__annotations__[k]):
                    if not validate(get_args(cls.__annotations__[k])[0],v):
                        raise ValueError(f"{v} is not of type {get_args(cls.__annotations__[k])[0]}")
                cls.__data__[k] = v

        for k,v in cls.__annotations__.items():
            if k not in cls.__data__:
                cls.__data__[k]=initialize(v)
                
        
    def __setattr__(self, name: str, value: Any) -> None:
        """
        Overrides the superclass `__setattr__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
    
        # Raise error if the given value is not of the expected type
        if name in self.__data__ and name not in self.__annotations__:
            pass
        elif not validate(self.__annotations__[name],value):
            raise TypeError(
                f'{name} key has a value {value} which is of type {type(value)}. {self.__annotations__[name]} expected.')

        super().__setitem__(name, value)

    def __setitem__(self, name, value) -> None:
        """
        Overrides the superclass `__setitem__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        if name in self.__data__ and name not in self.__annotations__:
            pass
        elif not validate(self.__annotations__[name],value):
            raise TypeError(
                f'{name} key has a value {value} which is of type {type(value)}. {self.__annotations__[name]} expected.')

        super().__setitem__(name, value)
