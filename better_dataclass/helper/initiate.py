import typing
import enum
from typing import Any, Literal, Union, Optional, Tuple, List, Set, Dict, Type, get_origin, get_args

# TODO: handle Union, Optional, Dict, anySequence
def initialize(annot: Type) -> Any:
    
    # handling Union
    if get_origin(annot) == Union:
        return initialize(get_args(annot)[0])
    elif get_origin(annot)== Optional:
        return None
    
    elif get_origin(annot) in (List,list):
        return []
    
    elif get_origin(annot) in (Dict,dict):
        return {}
    
    elif get_origin(annot) in (Set,set):
        return set()
    
    elif get_origin(annot) in (Tuple,tuple):
        return tuple()

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

# Case 1: Basic initialization
print(initialize(int))              # Expected: 0
print(initialize(str))              # Expected: ''
print(initialize(bool))             # Expected: False
print(initialize(float))            # Expected: 0.0

# Case 2: Union initialization
print(initialize(Union[int, str]))         # Expected: 0
print(initialize(Union[str, bool]))        # Expected: ''
print(initialize(Union[float, int, bool])) # Expected: 0.0

# Case 3: List initialization
print(initialize(List[int]))        # Expected: []
print(initialize(List[str]))        # Expected: []
print(initialize(List[bool]))       # Expected: []

# Case 4: Dict initialization
print(initialize(Dict[str, int]))   # Expected: {}
print(initialize(Dict[int, bool]))  # Expected: {}

# Case 5: Set initialization
print(initialize(Set[str]))         # Expected: set()
print(initialize(Set[int]))         # Expected: set()

# Case 6: Tuple initialization
print(initialize(Tuple[int, str]))  # Expected: (0, '')
print(initialize(Tuple[str, int]))  # Expected: ('', 0)

# Case 7: Literal initialization
print(initialize(Literal[1, 2, 3]))  # Expected: 1

# Case 8: Enum initialization
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(initialize(Color))                    # Expected: Color.RED

# Case 9: Any initialization
print(initialize(Any))                # Expected: None


