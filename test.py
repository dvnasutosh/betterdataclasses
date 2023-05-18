from ast import Tuple
from enum import Enum, EnumCheck
from typing import Final, Literal,  List, Sequence, TypedDict, Union, get_origin,Optional

from better_dataclass.StrictDictionary import StrictDictionary

class SD(StrictDictionary):
    a: int
    b: int
    c: str

class NestedSD(StrictDictionary):
    name: str
    values: List

class Data(StrictDictionary):
    d1:Union[int,float]
    d2:Optional[int]
    d3:Union[List[List[int]],Tuple]
    d4:Literal['Hey','Fine']
    d5:Final[int]=10
class ComplexSD(StrictDictionary):
    x=99.0
    y: float
    Un:Union[str,List]
    nested: NestedSD
    d:Data

# check if Union> get args > get args  

class XX(Enum):
    Data=2
    Data2=3
    Data3="3"
class X:
    s:Union[str,int]
    t:XX



s=ComplexSD()
print(s.__raw__())
s.nested.name='323'
s.nested.values=['323']







# SECTION
class Testing(StrictDictionary):
    Integer:int
    IntList:List[int]
    IFList:List[Union[int,float]]
    UFInt:Union[int,float]
    Union2:Union[int,List[float]]
    Optional:Optional[int]

x={
    "Integer":0,
    "IntList":[0],
    "IFList":[0,0.0],
    "UFList":0,
    "Union":0
}

"""
    UnionList                
"""

class s(Enum):
    a=1
    b=2
class B:
    s:Enum
# print(get_args(dict))
# print(type({"4":"d",5:"ffd"})==typing.Dict[int,str])

# from better_dataclass.helper.initiate import initialize
class T2(StrictDictionary):
    a:int
    b:float

ob1=T2()
# ob1.c=34.8
print(ob1)
