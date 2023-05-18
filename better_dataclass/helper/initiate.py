
import enum
from typing import Any, Literal, Union, Optional, Tuple, List, Set, Dict, Type, get_origin, get_args

# TODO: handle Union, Optional, Dict, anySequence
def initialize(annot: Type) -> Any:
    
    # handling Union
    if get_origin(annot)== Optional or type(None) in get_args(annot):
        return None
    
    if get_origin(annot) == Union:
        return initialize(get_args(annot)[0])
    
    elif get_origin(annot) in (List,list):
        return []
    
    elif get_origin(annot) in (Dict,dict):
        return {}
    
    elif get_origin(annot) in (Set,set):
        return set()
    
    elif get_origin(annot) in (Tuple,tuple):
        return ()

    elif Literal in (get_origin(annot), annot):
        return next(iter(get_args(annot)))

    elif isinstance(annot,type) and issubclass(annot, enum.Enum):
        return next(iter(annot))

    elif annot is Any:
        return None
    try:
        return annot()
    except TypeError as e:
        raise ValueError(f"Unable to initialize value for annot: {annot}") from e


# Test Cases

