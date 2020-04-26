"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
print("=============================================第一个类：猫类=====================================================")
#类1：定义一个猫类
class Cat:
    #猫有颜色、尾巴、腿、鼻子属性，其中颜色通过参数传入
    def __init__(self,colour):
        self.colour=colour
        self.tail=1
        self.leg=4
        self.nose=1
    #定义一个catch_mouse方法
    def catch_mouse(self):
        print(f"一只{self.colour}的猫，正在抓老鼠")
#实例化为一只黄色的猫
cat1=Cat("黄色")
#调用Cat类的tail属性，并打印
print(cat1.tail)
#调用catch_mouse方法
cat1.catch_mouse()

print("============================================第二个类：飞机类====================================================")
#类2：定义一个AirPlane类
class AirPlane:
    #飞机有航班信息、机型、起降时间、起抵机场四个属性，这四个属性都通过参数传入
    def __init__(self,airline,model,takeoff_landing_time,arrive_at_the_airport):
        self.airline=airline
        self.model=model
        self.takeoff_landing_time=takeoff_landing_time
        self.arrive_at_the_airport=arrive_at_the_airport

    #定义一个flight方法
    def flight(self):
        print(f"{self.airline},{self.model},{self.takeoff_landing_time},{self.arrive_at_the_airport} 已正常起飞")
    #定义一个arrival方法
    def arrival(self):
        print(f"{self.airline},{self.model},{self.takeoff_landing_time},{self.arrive_at_the_airport} 已安全抵达")


#实例化飞机
airplane1=AirPlane("中国国航CA1865","中型机 320","2020-4-25 17:05——2020-4-25 19:40","浦东机场T2——白云国际机场T1")
#调用AirPlane类的airline属性，并打印
print(airplane1.airline)
#调用flight方法
airplane1.flight()
#调用arrival方法
airplane1.arrival()

print("============================================第三个类：电脑类====================================================")
#类3：定义一个电脑类
class Computer:
    #电脑有品牌、系统两个属性，这两个属性都通过参数传入
    def __init__(self,brand,system):
        self.brand=brand
        self.system=system

    #定义一个write_code方法
    def write_code(self):
        print(f"我用{self.brand}品牌的装有{self.system}系统的电脑编写代码")

#实例化我的电脑
mycomputer=Computer("ThinkPad","win10")
#调用system属性，并打印
print(mycomputer.system)
#调用write_code方法
mycomputer.write_code()

print("============================================第四个类：冰箱类====================================================")
#类4：定义一个冰箱类
class IceBox():
    #冰箱有门、冷藏室、冷冻室三个属性，这三个属性都通过参数传入
    def __init__(self,door,cold_room,freezer):
        self.door=door
        self.cold_room=cold_room
        self.freezer=freezer

    def freezing(self):
        print(f"我家的{self.door}冰箱的{self.freezer}有冷冻功能")

#实例化我的冰箱
myicebox=IceBox("双开门","冷藏室","冷冻室")
#调用cold_room属性，并打印
print(myicebox.cold_room)
#调用freezing方法
myicebox.freezing()

print("===========================================第五个类：三角形类===================================================")
#类5：三角形类
class Triangle:
    # 三角形有三条边，这三个属性都通过参数传入
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

    #定义一个等腰三角方法
    def dengyao(self):
        print(f"三条边依次为{self.side1}、{self.side2}、{self.side3}，是等腰三角形")

    # 定义一个等边三角方法
    def dengbian(self):
        print(f"三条边依次为{self.side1}、{self.side2}、{self.side3}，是等边三角形")

    # 定义一个直角三角方法
    def zhijiao(self):
        print(f"三条边依次为{self.side1}、{self.side2}、{self.side3}，是直角三角形")

    # 定义一个一般三角方法
    def yiban(self):
        print(f"三条边依次为{self.side1}、{self.side2}、{self.side3}，是一般三角形")

#实例化三角形
zhijiao1=Triangle(3,4,5)
#调用zhijiao方法
zhijiao1.zhijiao()

