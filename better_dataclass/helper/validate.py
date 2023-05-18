import enum

from collections.abc import Iterable
from typing import Any, Final, Literal, Union, Optional, Tuple, List, Set, Dict, Type, get_origin, get_args


def validate(annot:Type,value):  # sourcery skip: low-code-quality
    if type(value)==annot: 

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
    
                
        
# Case 1: Basic type checking
print(validate(int, 42), (int, 42))          # Expected: True
print(validate(str, "Hello"), (str, "Hello"))    # Expected: True
print(validate(bool, True),(bool, True))      # Expected: True
print(validate(float, 3.14),(float, 3.14))     # Expected: True
print("ww")
# Case 2: Union type checking
print(validate(Union[int, str], 42),(Union[int, str], 42))        # Expected: True
print(validate(Union[int, str], "Hello"),(Union[int, str], "Hello"))   # Expected: True
print(validate(Union[int, str], 3.14),(Union[int, str], 3.14))      # Expected: False
print()
# ---------------------------------

# Case 3: List type checking
print(validate(List[int], [1, 2, 3]),(List[int], [1, 2, 3]))      # Expected: True
print(validate(List[str], ["a", "b", "c"]),(List[str], ["a", "b", "c"])) # Expected: True
print(validate(List[int], [1, 2, "three"]),(List[int], [1, 2, "three"])) # Expected: False
print()

# Case 4: Final type checking
print(validate(Final[int], 42),(Final[int], 42))    # Expected: False
print(validate(Final[str], "Hello"),(Final[str], "Hello")) # Expected: False
print()

# Case 5: Literal type checking
print(validate(Literal[1, 2, 3], 1),(Literal[1, 2, 3], 1)) # Expected: True
print(validate(Literal[1, 2, 3], 4),(Literal[1, 2, 3], 4)) # Expected: False
print()

# Case 6: Enum type checking
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
class Cor(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW=0
print(validate(Color, Color.RED),(Color, Color.RED))      # Expected: True
print(validate(Color, Cor.YELLOW),(Color, Cor.YELLOW))   # Expected: False
print()

# Case 7: Optional type checking
print(validate(Optional[int], None),(Optional[int], None))   # Expected: True
print(validate(Optional[int], 42),(Optional[int], 42))     # Expected: True
print()

# Case 8: Complex Union type checking
print(validate(Union[int, Optional[str]], 42), (Union[int, Optional[str]], 42))        # Expected: True
print(validate(Union[int, Optional[str]], "Hello"), (Union[int, Optional[str]], "Hello"))   # Expected: True
print(validate(Union[int, Optional[str]], 3.14), (Union[int, Optional[str]], 3.14))      # Expected: False
print()

# Case 9: Complex List type checking
print(validate(List[Union[int, str]], [1, "two", 3]), (List[Union[int, str]], [1, "two", 3]))  # Expected: True
print(validate(List[Union[int, str]], [1, 2, 3]), (List[Union[int, str]], [1, 2, 3]))      # Expected: True
print()

# Case 10: Mixed type checking
print(validate(Union[int, List[str]], 42),(Union[int, List[str]], 42))             # Expected: True
print(validate(Union[int, List[str]], ["a", "b", "c"]),(Union[int, List[str]], ["a", "b", "c"])) # Expected: True
print(validate(Union[int, List[str]], ["a", 2, "c"]),(Union[int, List[str]], ["a", 2, "c"]))   # Expected: False
                                
print("done")
print(validate(Dict[int,str],{"4":"d",5:"ffd"}))
print()