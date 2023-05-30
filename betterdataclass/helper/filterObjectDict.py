
def filterDict(data:dict):
    return {
            k: data[k]
            for k in data
            if not (len(k) > 1 and k[0] == k[1] == '_')
        }