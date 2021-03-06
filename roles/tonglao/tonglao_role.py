"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
希望各位同学在此基础上可以添加自己的“freestyle”哦
"""
# 定义一个天山童姥类
class TongLao:
    # 属性有血量，武力值（通过传入的参数得到）
    def __init__(self, tlhp, tlpower):
        self.tlhp = tlhp
        self.tlpower = tlpower

    # 定义see_people方法 ,传入一个name参数
    def see_people(self, name):
        # 如果传入”WYZ”（无崖子）
        if name == "WYZ":
            # 打印，“师弟！！！！”
            print("师弟！！！！")
        # 如果传入“李秋水”
        elif name == "李秋水":
            # 打印“呸，贱人”
            print("呸，贱人")
        # 如果传入“丁春秋”
        elif name =="丁春秋":
            # 打印“叛徒！我杀了你”
            print("叛徒！我杀了你")
        else:
            # 抛出异常
            raise Exception ("查无此人")

    # 定义fight_zms方法，传入敌人的hp，power
    def fight_zms(self, hp, power):
        # 武力值提升10倍，血量缩减2倍
        self.tlpower = self.tlpower * 10
        self.tlhp = self.tlhp / 2
        # 分别算出tl剩余的血量和敌人剩余的血量
        final_tlhp = self.tlhp - power
        final_hp = hp - self.tlpower
        # 判断谁的血量多，谁就获胜
        if final_tlhp > final_hp:
            print("天上童姥获胜")
        elif final_tlhp < final_hp:
            print("敌人获胜")
        else:
            print("打平，两败俱伤")

