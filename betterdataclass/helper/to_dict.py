from ast import Str
from enum import Enum

from betterdataclass import StrictDictionary


def to_raw_dict(obj: object, processed=None):
    if processed is None:
        processed = set()
    if id(obj) in processed:
        return "<circular reference>"
    processed.add(id(obj))
    if isinstance(obj, dict):
        out = {}
        for key, value in obj.items():
            if value is None:
                out[key] = value
            elif isinstance(value, dict):
                out[key] = to_raw_dict(value, processed)
            elif isinstance(value, Enum):
                out[key] = [str(value), value.value]
            elif isinstance(value, (list, tuple, set)):
                out[key] = to_raw_dict(value, processed)
            elif isinstance(value, (int, float, bool, complex, str)):
                out[key] = value
            elif isinstance(value,StrictDictionary.StrictDictionary):
                out[key] = to_raw_dict(value.__data__, processed)
            elif isinstance(value, object):
                out[key] = to_raw_dict(value.__dict__, processed)
            else:
                out[key] = str(value)
        return out
    elif isinstance(obj, (list, tuple, set)):
        return [to_raw_dict(item, processed) for item in obj]
    elif isinstance(obj, (int, float, bool, complex, str)):
        return obj
    elif isinstance(obj, Enum):
        return [str(value), value.value]
    elif isinstance(value,StrictDictionary.StrictDictionary):
        out[key] = to_raw_dict(value.__data__, processed)
    elif isinstance(obj, object):
        return to_raw_dict(obj.__dict__, processed)
    else:
        return str(obj)
