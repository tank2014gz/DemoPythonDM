from com.dr.demo02.Observer import Observer


class WashingMode(Observer):
    "该模式用于洗澡用"
def update(self, waterHeater):
    temperature = waterHeater.getTemperature()
    if temperature >= 50 and temperature <= 70:
        print("水已经烧好，温度正好！可以用来洗澡了。")
