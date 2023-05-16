import enum
import typing
from collections.abc import Iterable
def validate(annot:typing.Type,value):

    # Check Union
    if type(value)==annot: 
        return True
    if typing.get_origin(annot) in (typing.Union, typing.Optional):
        
        isValid=list()
        
        for args in typing.get_args(annot):
            isValid.append(validate(args,value))
        return any(isValid)
    
    # Check List
    elif typing.get_origin(annot) in (typing.List,list) :
        listValid=list()
        if type(value)!=list:
            return False
        for each in value:
            # Check each data and if any of the data doesn't comply with annotations
            listValid.append(isinstance(each,typing.get_args(annot)))       
    
        return all(listValid)
    
    # Check Final
    elif typing.get_origin(annot) == typing.Final:
        return False
    # check Literal
    elif typing.Literal in (typing.get_origin(annot),annot):
        return value in typing.get_args(annot)
    elif issubclass(annot,enum.Enum):
        return isinstance(value, annot) or value in [member.value for member in annot]


# Case 1: Basic type checking
print(validate(int, 42))          # Expected: True
print(validate(str, "Hello"))    # Expected: True
print(validate(bool, True))      # Expected: True
print(validate(float, 3.14))     # Expected: True
print()
# Case 2: Union type checking
print(validate(typing.Union[int, str], 42))        # Expected: True
print(validate(typing.Union[int, str], "Hello"))   # Expected: True
print(validate(typing.Union[int, str], 3.14))      # Expected: False
print()
# ---------------------------------

# Case 3: List type checking
print(validate(typing.List[int], [1, 2, 3]))      # Expected: True
print(validate(typing.List[str], ["a", "b", "c"])) # Expected: True
print(validate(typing.List[int], [1, 2, "three"])) # Expected: False
print()

# Case 4: Final type checking
print(validate(typing.Final[int], 42))    # Expected: False
print(validate(typing.Final[str], "Hello")) # Expected: False
print()

# Case 5: Literal type checking
print(validate(typing.Literal[1, 2, 3], 1)) # Expected: True
print(validate(typing.Literal[1, 2, 3], 4)) # Expected: False
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
print(validate(Color, Color.RED))      # Expected: True
print(validate(Color, Cor.YELLOW))   # Expected: False
print()

# Case 7: Optional type checking
print(validate(typing.Optional[int], None))   # Expected: True
print(validate(typing.Optional[int], 42))     # Expected: True
print()

# Case 8: Complex Union type checking
print(validate(typing.Union[int, typing.Optional[str]], 42))        # Expected: True
print(validate(typing.Union[int, typing.Optional[str]], "Hello"))   # Expected: True
print(validate(typing.Union[int, typing.Optional[str]], 3.14))      # Expected: False
print()

# Case 9: Complex List type checking
print(validate(typing.List[typing.Union[int, str]], [1, "two", 3]))  # Expected: True
print(validate(typing.List[typing.Union[int, str]], [1, 2, 3]))      # Expected: True
print()

# Case 10: Mixed type checking
print(validate(typing.Union[int, typing.List[str]], 42))             # Expected: True
print(validate(typing.Union[int, typing.List[str]], ["a", "b", "c"])) # Expected: True
print(validate(typing.Union[int, typing.List[str]], ["a", 2, "c"]))   # Expected: False
                                
print("done")