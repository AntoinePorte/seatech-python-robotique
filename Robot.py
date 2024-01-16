import time

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']
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
    

    # getter current_speed
    @property
    def current_speed(self):
        return self.__current_speed
      
    # setter current_speed
    @current_speed.setter
    def current_speed(self, current_speed):
      self.__current_speed= current_speed



    def __init__(self, name, power = 'False'):
      self.name = name
      self.__power = power
      
    def power (self, power:bool):
      self.__power = power

    
    def charge(self): 
      pass

    def status(self):
       print("status")
      
    def stop(self):
      self.__current_speed = 0
    
    """
      Give your best code here ( •̀ ω •́ )✧
    """

if __name__ == "__main__":

  print("test")