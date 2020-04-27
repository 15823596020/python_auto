"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
希望各位同学在此基础上可以添加自己的“freestyle”哦
"""
# 导入TongLao包
from roles.tonglao.tonglao_role import TongLao

# 定义一个XuZhu类，继承于童姥
class XuZhu(TongLao):
    # 定义一个read方法
    def read(self):
        print("罪过罪过")

# # 实例化童姥，并传入tlhp和tlpower
# tonglao = TongLao(1000, 200)
# # 调用TongLao类的fight_zms方法，给敌人传入hp和power
# tonglao.fight_zms(1000, 200)
#
# # 父类init方法的属性需参数传入；子类继承父类；子类没有单独的init方法；那么实例化子类的时候，也需要传入父类的参数
# # 实例化虚竹
# xuzhu = XuZhu(1000, 200)
# # 调用XuZhu类的read方法
# xuzhu.read()