from enum import Enum


from ..StrictDictionary import StrictDictionary

def to_raw_dict(obj: object):
    # if processed is None:
    #     processed = set()
    # if id(obj) in processed:
    #     return "<circular reference>"
    # processed.add(id(obj))

    if isinstance(obj, dict):
        out = {}

        for key, value in obj.items():

            if isinstance(value, dict):
                out[key] = to_raw_dict(value)

            elif isinstance(value, Enum):
                out[key] = [str(value), value.value]

            elif isinstance(value, (list, tuple, set)):

                out[key] = to_raw_dict(value)

            elif isinstance(value, (int, float, bool, complex, str)):
                out[key] = value

            elif isinstance(value, StrictDictionary):
                out[key] = to_raw_dict(value.__data__)

            elif isinstance(value, object):

                out[key] = to_raw_dict(value.__dict__)

            else:
                out[key] = str(value)
        return out

    elif isinstance(obj, (list, tuple, set)):
        return [to_raw_dict(item) for item in obj]

    elif isinstance(obj, (int, float, bool, complex, str)):
        return obj

    elif isinstance(obj, Enum):
        return [str(value), value.value]
    elif isinstance(obj, StrictDictionary):
        return to_raw_dict(obj.__data__)
    elif obj is None:
        return None
    elif isinstance(obj, object):
        return to_raw_dict(obj.__dict__)
    else:
        return str(obj)




# def to_raw_dict(obj: object, processed=None):
#     # if processed is None:
#     #     processed = set()
#     # if id(obj) in processed:
#     #     return "<circular reference>"
#     # processed.add(id(obj))

#     if isinstance(obj, dict):
#         out = {}

#         for key, value in obj.items():

#             if isinstance(value, dict):
#                 out[key] = to_raw_dict(value, processed)

#             elif isinstance(value, Enum):
#                 out[key] = [str(value), value.value]

#             elif isinstance(value, (list, tuple, set)):
#                 for i in value:
#                     print(i)
#                 out[key] = to_raw_dict(value, processed)

#             elif isinstance(value, (int, float, bool, complex, str)):
#                 out[key] = value

#             elif isinstance(value, StrictDictionary):
#                 out[key] = to_raw_dict(value.__data__,processed)

#             elif isinstance(value, object):
#                 print(value,type(value))
#                 out[key] = to_raw_dict(value.__dict__, processed)

#             else:
#                 out[key] = str(value)
#         return out

#     elif isinstance(obj, (list, tuple, set)):
#         for i in obj:       
#             print(i)
#         return [to_raw_dict(item, processed) for item in obj]

#     elif isinstance(obj, (int, float, bool, complex, str)):
#         return obj

#     elif isinstance(obj, Enum):
#         return [str(value), value.value]
#     elif isinstance(obj, StrictDictionary):
#         print(obj.__data__)
#         return to_raw_dict(obj.__data__,processed)
#     elif obj is None:
#         return None
#     elif isinstance(obj, object):
#         return to_raw_dict(obj.__dict__, processed)
#     else:
#         return str(obj)
