import typing
import enum

def initialize(annot: typing.Type) -> typing.Any:
    if typing.get_origin(annot) in (typing.Union, typing.Optional):
        for args in typing.get_args(annot):
            try:
                return initialize(args)
            except ValueError:
                continue
        raise ValueError(f"Unable to initialize value for annot: {annot}")

    
    # handling Union
    elif typing.get_origin(annot) == typing.Union:
        return initialize(typing.get_args(annot)[0])
    
 
    elif typing.get_origin(annot) == typing.Dict:
        key_type, value_type = typing.get_args(annot)
        return {initialize(key_type):initialize(value_type)}

    elif typing.get_origin(annot) == typing.Set:
        inner_type = typing.get_args(annot)[0]
        return set(initialize(inner_type))

    elif typing.get_origin(annot) == typing.Tuple:
        inner_types = typing.get_args(annot)
        return tuple(initialize(arg) for arg in inner_types)


    elif typing.get_origin(annot) == typing.TypeVar:
        raise ValueError(f"Unable to initialize value for annot: {annot}")

    elif typing.get_origin(annot) == typing.Final:
        raise ValueError(f"Unable to initialize value for annot: {annot}")

    elif typing.Literal in (typing.get_origin(annot), annot):
        return next(iter(typing.get_args(annot)))

    elif isinstance(annot,type) and issubclass(annot, enum.Enum):
        return next(iter(annot))

    elif annot is typing.Any:
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
print(initialize(typing.Union[int, str]))         # Expected: 0
print(initialize(typing.Union[str, bool]))        # Expected: ''
print(initialize(typing.Union[float, int, bool])) # Expected: 0.0

# Case 3: List initialization
print(initialize(typing.List[int]))        # Expected: []
print(initialize(typing.List[str]))        # Expected: []
print(initialize(typing.List[bool]))       # Expected: []

# Case 4: Dict initialization
print(initialize(typing.Dict[str, int]))   # Expected: {}
print(initialize(typing.Dict[int, bool]))  # Expected: {}

# Case 5: Set initialization
print(initialize(typing.Set[str]))         # Expected: set()
print(initialize(typing.Set[int]))         # Expected: set()

# Case 6: Tuple initialization
print(initialize(typing.Tuple[int, str]))  # Expected: (0, '')
print(initialize(typing.Tuple[str, int]))  # Expected: ('', 0)

# Case 7: Literal initialization
print(initialize(typing.Literal[1, 2, 3]))  # Expected: 1

# Case 8: Enum initialization
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(initialize(Color))                    # Expected: Color.RED

# Case 9: Any initialization
print(initialize(typing.Any))                # Expected: None


