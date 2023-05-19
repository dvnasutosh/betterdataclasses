class StrictList(list):
    """
    """
    def __init__(self,*data) -> None:
        for i in data:
            if not self.restriction(i):
                raise ValueError(f"Data does not follow restrictions set for {self.__class__}")
            elif type(i) != any and type(i) not in self.types:
                raise TypeError(f'value {i} is not of type {self.types}. It\'s of type {type(i)} ')
            super().__init__(data)
    
    def __init_subclass__(cls):
        if 'types' not in cls.__dict__.keys():
            cls.types=any
        elif any(type(i) != type(int) for i in cls.__dict__['types']):
            raise ValueError('the types must only contain `type` objects. ')

        cls.types= cls.__dict__['types']
        super().__init_subclass__()

    def restriction(self,i): 
        return True
        # OverWrite this to add Restriction
    
