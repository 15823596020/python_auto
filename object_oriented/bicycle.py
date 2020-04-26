"""
面向对象之开小车
写一个Bicycle（自行车）类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）：
再写一个电动自行车类EBicycle继承自Bicycle，添加电池电量valume属性通过，参数传入，同时有两个方法：
1、fill_charge(vol)用来充电，vol为电量
2、run（km）方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""

# 定义一个自行车类
class Bicycle:
    # 定义一个run方法
    def run(self, km):
        # 调用run方法时，显示骑行里程km
        # print("自行车骑的里程数为：{}".format(km))
        # 调用run方法时，显示骑行里程km,这样子写也可以
        print(f"自行车骑的里程数为：{km}")

# # 实例化一辆自行车
# bicycle = Bicycle()
# # 调用Bicycle类的run方法，并传入骑行里程
# bicycle.run(100)

# 定义一个电瓶车类，并继承自行车类
class EBicycle(Bicycle):
    # 占位符，不起任何作用
    # pass
    # 定义电池电量valume属性，参数传入
    def __init__(self, valume):
        # 实例变量
        self.valume = valume

    # 定义一个获取电量的方法
    def get_valume(self):
        # 这里是调用自身类的自由变量，需要加上self.变量名
        print("当前电量为", self.valume)

    # 定义一个充电方法，参数传入电量
    def fill_charges(self, vol):
        print("充电电量为：", vol)

    # 定义一个电瓶车的骑行方法,传入要骑行的里程数
    def run(self, km):
        # 电瓶车当前电量能骑行的里程数
        ebkm = self.valume * 10
        # 传入的需要骑行的总的里程数-电频车当前电量能骑行的里程数
        dkm = km - ebkm
        # 判断，如果dkm>0，则表示电瓶车的电量不够，需要用脚蹬，否则表示电瓶车的电量刚好能支撑到骑完全程
        if dkm > 0:
            # 打印电瓶车骑的里程数
            print(f"电瓶车骑的里程数为：{ebkm}")
            # 调用父类的run方法,并传入自行车需要骑行的里程数，需要加super()，不加的话就表示调用自身类的run方法
            super().run(dkm)
            # 打印当电量用完之后，脚蹬的里程数
        else:
            # 打印电瓶车骑的里程数
            print(f"电瓶车骑的里程数为：{km}")

# 实例化一电瓶车，并传入电瓶车当前电量，这个参数是传给EBicycle类的__init__方法
ebicycle = EBicycle(10)
# 调用电瓶车的run方法，传入需要骑行的总的里程数，这个参数是传给EBicycle类的run方法
ebicycle.run(131)
