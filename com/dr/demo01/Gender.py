
class Test:
    '这是一个测试类'

    def __int__(self):
        self.__ivalue=5

    def getValue(self):
        return self.__ivalue

class demo01:
    'demo 01 认识Python  基本数据类型'

def testType():
    "测试方法"
    age=18
    weight=62.51
    name="Tony"
    print("age:",age)
    print("weight:",weight)
    print("name:",name)

    age=name
    print("age",age)

    a=b=c=5

    print("a:",a,"b:",b,"c:",c)

    print("id(a):",id(a),"id(b):",id(b),"id(c)",id(c))


# testType()


def testArray():
    '测试集合'
    list=['Thosmon',78,12.56,"Sunny",180.2,34]
    tinyList=[123,'tony']
    print('list:',list)
    print('list[0]',list[0])
    print('list[1:3]',list[1:3])
    print(tinyList*5)

    print(list+tinyList)
    print(tinyList+list)

    list[1]=10000
    print("list:",list)

    list.append("jsjjdsjdsjjds")

    list.reverse()
    print(list)

    list.remove("Sunny")
    print(list)

    list.clear()
    print(list)


# testArray()


def testTuple():
    '测试元组，相当于Java中的final C++中的const'
    tuple=('Thosmon',78,12.56,"Sunny",180.2,34)
    tupleTiny=(123,'tony')
    print('tuple:',tuple)
    print('tuple[0]',tuple[0])
    print('tuple[1:3]',tuple[1:3])
    print(tupleTiny*5)

    print(tuple+tupleTiny)
    print(tupleTiny+tuple)

# 非法操作
    # tuple[1]=10000
    # print("tuple:",tuple)

    # tuple.append("jsjjdsjdsjjds")

    # tuple.reverse()
    # print(tuple)

    # tuple.remove("Sunny")
    # print(tuple)

    # tuple.clear()
    # print(tuple)
#非法操作

# testTuple()


def testDictionary():
    '测试字典'
    dict={}
    dict['one']="This is one "
    dict[3]="this is two"
    dict[2]=50
    print("dict[one]:",dict['one'])
    print("dict:",dict)

    dictTiny={"1":"jdjjdjd","2":"99999","3":6666}
    print(dictTiny.keys())
    print(dictTiny.values())

    print(dictTiny)


# testDictionary()





