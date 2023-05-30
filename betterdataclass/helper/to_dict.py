from enum import Enum

from betterdataclass.helper.filterObjectDict import filterDict


from ..StrictDictionary import StrictDictionary


def to_raw_dict(obj: object):
    if isinstance(obj, dict):
        out = {}
        for key, value in obj.items():
            if value is None:
                out[key] = value
            elif isinstance(value, dict):
                out[key] = to_raw_dict(value)
            elif isinstance(value, Enum):
                out[key] = [str(value), value.value]
            elif isinstance(value, (list, tuple, set)):
                out[key] = to_raw_dict(value)
            elif isinstance(value, (int, float, bool, complex, str)):
                out[key] = value
            # elif isinstance(value,StrictDictionary):
            #     out[key] = to_raw_dict(value.__dict__, processed)
            elif isinstance(value, object):
                out[key] = to_raw_dict(filterDict(value.__dict__))
            else:
                out[key] = str(value)
        return out
    elif obj is None:
        return obj
    elif isinstance(obj, (list, tuple, set)):
        return [to_raw_dict(item) for item in obj]
    elif isinstance(obj, (int, float, bool, complex, str)):
        return obj
    elif isinstance(obj, Enum):
        return [str(obj), obj.value]

    elif isinstance(obj, object):
        return to_raw_dict(filterDict(obj.__dict__))
    else:
        return str(obj)
