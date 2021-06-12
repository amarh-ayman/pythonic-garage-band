from abc import ABC, abstractmethod

class Band:

  instances=[]
  def __init__(self,name,members):
    """
    initializtion for name, member and append list (self)
    self is the return value of str ^-^
    """
    self.name=name
    self.members=members
    Band.instances.append(self)
  
  def play_solos(self):
    '''
    each value in members is a name of band(class)
    '''
    return [instance.play_solo() for instance in self.members]
  
  @classmethod  
  def to_list(cls):
    '''
    for make the values synch , in each calling
    '''
    return cls.instances
 
  def __str__(self):
    return f"Band Class str"
  
  def __repr__(self):
    '''
    dont have any real job in test file
    '''
    return f"Band Class"
  


class Musician(ABC):
  def __init__(self,name,instrument):
    self.name=name
    self.instrument=instrument
  
  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument.lower()}"
  
  def __repr__(self):
    '''
    self.__class__.__name__ ==> for give me the of the child who make the calling
    '''
    return f"{self.__class__.__name__} instance. Name = {self.name}"
  
  # @staticmethod
  def get_instrument(self):
    return f'{self.instrument.lower()}'

  @abstractmethod
  def play_solo(self): 
    pass 



class Guitarist(Musician):
  def __init__(self,name):
    super().__init__(name,'Guitar')

  def play_solo(self): 
    return 'face melting guitar solo'   


class Bassist(Musician):
  def __init__(self,name):
    super().__init__(name,'Bass')
  
  def play_solo(self): 
    return 'bom bom buh bom' 


class Drummer(Musician):
  def __init__(self,name):
    super().__init__(name,'Drums')

  def play_solo(self): 
    return 'rattle boom crash'   
