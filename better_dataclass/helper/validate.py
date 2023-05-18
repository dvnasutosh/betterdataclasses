import enum
from typing import Any, Final, Literal, Union, Optional, Tuple, List, Set, Type, get_origin, get_args


def validate(annot:Type,value):  # sourcery skip: low-code-quality
    if type(value) in (annot,get_origin(annot)) : 

        return True
    if annot==Any or get_origin(annot)==Any:
        return True

    # Check Union
    if get_origin(annot) in (Union, Optional):
        return any(validate(args,value) for args in get_args(annot))


    sequentialList=[List,Tuple,Set]
    
  
    if annot in sequentialList or get_origin(annot) in [get_origin(sq) for sq in sequentialList]:
        if type(value) not in (
            get_origin(annot),
            get_origin(get_origin(annot)),
        ):
            return False
        
        listValid = [validate(get_args(annot)[0],each) for each in value]
        return all(listValid)
    
    if get_origin(annot) == Final:
        return False

    if Literal in (get_origin(annot),annot):
        return value in get_args(annot)

    if isinstance(annot,type) and issubclass(annot,enum.Enum):
        return isinstance(value, annot) or value in [member.value for member in annot]

    if dict in (get_origin(annot),get_origin(get_origin(annot))):
        decision=isinstance(value,dict)
        if get_args(annot).__len__() != 2 and decision:
            return decision
        for k,v in dict.items(value):
            if not validate(get_args(annot)[0],k):
                return False
            if not validate(get_args(annot)[1],v):
                return False