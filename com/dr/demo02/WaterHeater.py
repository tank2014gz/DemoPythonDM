
class WaterHeater:
    "热水器：战胜寒冬的有利武器"

def __init__(self):
   self.__observers=[]
   self.__temperature=25

def getTemperature(self):
   return self.__temperature

def setTemperature(self,temperature):
  self.__temperature=temperature
  print("current temperature is:",self.__temperature)
  self.notfies()

def addObserver(self,observer):
  self.__observers.append(observer)

def notifies(self):
  for o in  self.__observers:
    o.update(self)
