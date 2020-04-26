"""
作业0
冒泡排序每一行加注释说明
"""
# 使用类改造冒泡排序

# 定义一个BubbleSort类
class BubbleSort:
    # 定义一个bubble_sort方法

    def bubble_sort(self, list_test):
        # 第i次排序
        for i in range(len(list_test) - 1):
            # 每次排序，比较的次数为j次
            for j in range(len(list_test) - 1 - i):
                # 比较相邻两个数的大小
                if list_test[j] > list_test[j + 1]:
                    # 如果前一个数大于后一个数，就交换两个数的位置
                    list_test[j], list_test[j + 1] = list_test[j + 1], list_test[j]

        # 返回排序后的列表
        return list_test


# 定义一个列表list_test1
list_test1 = [1, 2, 56, 3, 8, 45, 78, 89]
# list_test2 = ["f", "h", "g", "d", "c", "e", "b", "a"]
# list_test3 = ["F", "H", "g", "D", "c", "e", "h", "A"]

# 实例化一个bubble1对象
bubble1 = BubbleSort()

# 实例化对象bubble1调用BubbleSort的bubble_sort方法，并传入参数为list_test1列表
print(bubble1.bubble_sort(list_test1))
# print(bubble1.bubble_sort(list_test2))
