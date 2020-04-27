# 导入TongLao包和XuZhu包
from roles.tonglao.tonglao_role import TongLao
from roles.xuzhu.xuzhu_role import XuZhu

# 实例化童姥，并传入tlhp和tlpower
tonglao = TongLao(1000, 200)
# 调用TongLao类的see_people方法，传入李秋水
tonglao.see_people("十分士大夫")
# 调用TongLao类的fight_zms方法，给敌人传入hp和power
tonglao.fight_zms(1000, 200)

# 父类init方法的属性需参数传入；子类继承父类；子类没有单独的init方法；那么实例化子类的时候，也需要传入父类的参数
# 实例化虚竹
xuzhu = XuZhu(100, 2)
# 实例化子类调用父类的fight_zms方法
# xuzhu.fight_zms(1000,200)
# 实例化子类调用父类的see_people方法
# xuzhu.see_people("WYZ")
# 调用XuZhu类的read方法
xuzhu.read()