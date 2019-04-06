from com.dr.demo02.DrinkingMode import DrinkingMode
from com.dr.demo02.WashingMode import WashingMode
from com.dr.demo02.WaterHeater import WaterHeater


class TestWaterHeater:
    '测试热水器类'

def testWaterHeater():
    heater=WaterHeater()
    drinkingMode=DrinkingMode()
    washingMode=WashingMode()
    heater.addObserver(drinkingMode)
    heater.addObserver(washingMode)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(110)




    testWaterHeater()