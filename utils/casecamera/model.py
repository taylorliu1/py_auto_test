import enum

class OSEnum(enum.Enum):
    LINUX = 1 
    WINDOWS = 2
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return False


class ARRAYEnum(enum.Enum):
    POWERSTORE = 1
    POWERFLEX = 2
    POWERMAX = 3
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return False