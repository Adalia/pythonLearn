#coding:utf-8

'''
需求；
对请求的参数进行ascill排序
排序后，对请求的参数进行md5加密
'''

# def data(**kwargs):
#     data = dict(sorted(kwargs.items(),key=lambda item:item[0]))
#     return data
#
# dict1={'name':'haihui','age':18,'address':'beijing'}
# print(data(dict1))

# '''匿名函数：lambda'''
# def add(a,b):
#     return a+b
# per = lambda a,b:a+b
#
# print('true') if age>5 else print('false')

#函数全套
def outer():
    def inner():
        print("hello python")
    return inner #返回的是这个函数本身

outer()()  #调用outer()中返回的内部函数
print(outer())

# '''动态参数学习'''
# def f1(*args,**kwargs):
#     print(args,kwargs)
#
#
# f1([1,2,3])
# f1('a')
# f1(name="haihui")
# f1(dic={'name':'haihui'})
#
#
# '''
# 输出：
# ([1, 2, 3],) {}
# ('a',) {}
# () {'name': 'haihui'}
# () {'dic': {'name': 'haihui'}}
# '''

