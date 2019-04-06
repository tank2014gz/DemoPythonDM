from com.dr.demo01.Person import Person


class Teacher(Person):
    '老师'

    def __init__(self, name, age, height):
        super().__int__(name, age, height)
        self.__title = None

    def getTitle(self, title):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def showInfo(self):
        print("title:", self.__title)
        super().showInfo()
