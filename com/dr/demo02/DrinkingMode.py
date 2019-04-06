from com.dr.demo02.Observer import Observer


class DrinkingMode(Observer):
    '该模式用于饮用水'

def update(self,waterHeater):
  temperature=waterHeater.getTemperature()
  if(temperature>=100):
    print("水已经烧开！可以用来饮用了。")