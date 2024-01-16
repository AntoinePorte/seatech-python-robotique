import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
    __speed = 0
    __charging = False
    
    
    # getter name
    @property
    def name(self):
        return self.__name
      
    # setter name
    @name.setter
    def name(self, name):
      self.__name = name
    
    # getter states
    @property
    def states(self):
        return self.__states

    # setter state
    @states.setter
    def states(self):
      return self.__states[self.__power]
    

    def __init__(self, name, power = 'False'):
      self.name = name
      self.__power = power
      
    def power (self, power:bool):
      self.__power = power

    
    def recharge(self): 

      
    def stop(self):
      __speed = 0
    
    """
      Give your best code here ( •̀ ω •́ )✧
    """

if __name__ == "__main__":
  