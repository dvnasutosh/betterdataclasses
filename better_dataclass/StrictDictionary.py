from typing import List, List, List, Any,get_origin
import typing
import json
from enum import Enum
from better_dataclass.helper.to_dict import to_raw_dict

class Dictionary:
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
        kwargs=kwargs if kwargs else dict() # nothing much just assigning empty dict to kwargs if kwargs has no value
        
        for i, j in kwargs.items():
            self.__data__[i] = j
        
    
    # def __init_subclass__(cls) -> None:
    #     cls.__data__=dict()
    #     for k,v in cls.__dict__.items():
            
    #         # Checking if the key is an internal key than skip the value
    #         if len(k)>1:
    #             if k[0]=='_':
    #                 if[1]=='_':
    #                     continue;
            
    #         cls.__data__[k]=v
            
    def __repr__(self) -> str:
        """
        Returns a string representation of the object's dictionary.
        """
        return str(self.__raw__())
    
    def __call__(self,raw:bool=False) -> dict:
        return self.__data__ if not raw else self.__raw__()
    
    def __str__(self):
        return str(self.__raw__())

    def __json__(self):
        return json.dumps(self.__raw__())
    
    def __raw__(self):
        # print(type(self.__data__['nested']))
        print(self.__dict__)
        return (self.__data__)



    def __setitem__(self, __name, __value) -> None:
        """
        Provides indexing and assignment functionality to the object.
        """
        self.__data__[__name]=__value
        setattr(self,__name,__value)
    
    

    def __getitem__(self, __name) -> Any:
        """
        Provides indexing and retrieval functionality to the object.
        """
        return self.__data__[__name]

class StrictDictionary(Dictionary):
    """
    A subclass of `Dictionary` that enforces strict typing of the values based on the annotations of the class attributes.
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
                expected_type=self.__annotations__[i] if not get_origin(self.__annotations__[i]) else get_origin(self.__annotations__[i])
                
                if not isinstance(j,expected_type):
                    raise TypeError(
                        f'{i} key has a value {j} which is of type {type(j)}. {expected_type} expected.')
                #!SECTION
                
                super().__setitem__(i,j)
                
    def __init_subclass__(cls) -> None:
        cls.__data__=dict()
        if not cls.__annotations__:
            raise AttributeError('You need to add type hintings for now. Will be solved in future versions. partial annotation is accepted but is not allowed as a part of the data')
        for i, j in cls.__annotations__.items():
            if i in cls.__dict__.keys():
                
                #   validation logic
                #   Checking if expected_type is of Typing Class than converting it into it's base class
                
                expected_type=j if not get_origin(j) else get_origin(j)        
                #   Raise error if the given value is not of the expected type
                if not isinstance(cls.__dict__[i],expected_type):
                    raise TypeError(
                        f'{i} key has a value {cls.__dict__[i]} which is of type {type(cls.__dict__[i])}. {expected_type} expected.')
                
                cls.__data__[i]=cls.__dict__[i]
            else:
                if type(get_origin(j)) == type(Enum) or type(j)== type(Enum):
                    
                    #   Checking if default exists as a param
                    if 'default' not in j.__members__.keys():

                        raise AttributeError(f'You need default to be set as a enum member. of {j}. Current {j._member_names_}')
                    
                    cls.__data__[i]=j.__members__['default']
                elif type(j) is type:
                    cls.__data__[i] = j()
                    
                    
                elif get_origin(j):
                    cls.__data__[i] = j.__origin__()
                else:
                    raise ValueError(f"can't assign {type(j)} data. Illegal Value.")

    def vaidate(self,__name,__value):
        expected_type=self.__annotations__[__name] 
        
        # Checking if expected_type is of Typing Class than converting it into it's base class
        if get_origin(expected_type):
            expected_type=get_origin(expected_type)
        elif self.__annotations__[__name]==Any:
            return True
        
        # Raise error if the given value is not of the expected type
        if not isinstance(__value,expected_type):
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {expected_type} expected.')
        return True
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Overrides the superclass `__setattr__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        expected_type=self.__annotations__[__name] 
        
        # Checking if expected_type is of Typing Class than converting it into it's base class
        if get_origin(expected_type):
            expected_type=get_origin(expected_type)
            
        # Raise error if the given value is not of the expected type
        if not isinstance(__value,expected_type):
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {expected_type} expected.')
        
        super().__setattr__(__name, __value)


    def __setitem__(self, __name, __value) -> None:
        """
        Overrides the superclass `__setitem__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        expected_type=self.__annotations__[__name]

        # verifying for Typing types
        if get_origin(expected_type):
            expected_type=expected_type.__origin__

        if not isinstance(__value,expected_type):
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {self.__annotations__[__name]} expected.')
        else:
            super().__setitem__(__name, __value)

        """
        Overrides the superclass `__setitem__` method to perform type checking before assignment.
        If the value to be assigned is not of the expected type, a `TypeError` is raised.
        """
        expected_type=self.__annotations__[__name]

        # verifying for Typing types
        if get_origin(expected_type):
            expected_type=expected_type.__origin__

        if not isinstance(__value,expected_type):
            raise TypeError(
                f'{__name} key has a value {__value} which is of type {type(__value)}. {self.__annotations__[__name]} expected.')
        else:
            super().__setitem__(__name, __value)