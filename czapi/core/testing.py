__all__ = []

from abc import ABC, abstractmethod, abstractproperty

class TagBase(ABC):
    @abstractmethod
    def find_all(self,name:str)->None:
        pass

    @abstractproperty
    def attrs(self)->dict:
        pass
    @abstractproperty
    def a(self):
        pass
    @abstractproperty
    def b(self):
        pass
    @abstractproperty
    def string(self)->str:
        pass

    @abstractmethod
    def __getitem__(self,key):
        pass

    @abstractproperty
    def href(self)->str:
        pass

class TagLike(TagBase):
    def __init__(self,children:dict=None,attrs:dict=None,a=None,b=None,string=None,href=None)->None:
        if attrs is None:
            self.attrs = {}
        else:
            self.attrs = attrs
        if children is None:
            self.children = {}
        else:
            self.children = children

        self.a = a
        self.b = b
        self.string = string
        self.href = href

    def find_all(self,name:str)->None:
        return self.children.get(name,[])

    def attrs(self)->dict:
        return self.attrs

    def a(self):
        return self.a

    def b(self):
        return self.b

    def string(self):
        return self.string

    def href(self)->str:
        return self.href

    def __getitem__(self,key):
        try:
            return getattr(self,key)
        except AttributeError:
            return AttributeError('This attribute does not exist.')
