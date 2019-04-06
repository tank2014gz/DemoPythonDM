from com.dr.demo01.Person import Person
from com.dr.demo01.Teacher import Teacher


class TestPerson:
    '测试父类-子类继承关系'

def testPerson():
    '测试方法'
    tony = Person("Tony", 25, 1.77)
    tony.showInfo()
    print("00000000")

    jenny = Teacher("Jenny", 22, 1.70)
    jenny.setTitle("语文老师")
    jenny.showInfo()

    testPerson()