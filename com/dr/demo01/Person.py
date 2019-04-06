class Person:
    '基类，人'
    visited = 0

    def __int__(self, name, age, height):
        self.__name = name
        self._age = age
        self.height = height

    def getName(self):
        return self.__name

    def getAge(self):
        return self._age

    def showInfo(self):
        print("name:", self.__name)
        print("age:", self._age)
        print("height:", self.height)
        print("visited:", self.visited)
        Person.visited = Person.visited + 1





