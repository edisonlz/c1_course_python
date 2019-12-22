装饰器
import functools

外层方法():
    before 方法
    方法()     
    after 方法



1. 函数装饰器无参数
def login_required(method):

    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        # 执行函数前
        if not kwargs.get('current_user_id'):
            return "无权限"

        print("before:current_user:%s" %  kwargs.get('current_user_id'))
        #执行函数
        data = method(*args, **kwargs)

        #执行函数后
        print("after:method done")
        return data
    return wrapper


@login_required
def get_balanace(*args, **kwargs):
    print("in get_balanace ,balanace is:%s" % 10000)
    return 10000

get_balanace()
get_balanace(current_user_id=1)



2. 函数装饰器有参数
def login_required(is_admin):
    def func(method):

        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            if not kwargs.get('current_user_id'):
                return "无权限"
            if is_admin:
                 if kwargs.get('admin') != 1:
                    return "无权限"

            print("before:current_user:%s" %  kwargs.get('current_user_id'))
            data =  method(*args, **kwargs)
            print("after:method done")
            return data

        return wrapper
    return func


@login_required(is_admin=True)
def get_balanace(*args, **kwargs):
    print("in get_balanace ,balanace is:%s" % 10000)
    return 10000

get_balanace(current_user_id=1)
get_balanace(current_user_id=1,admin=1)


总结：

*装饰器分为两层
第一层为方法名称
第二层为方法参数

*装饰器分为三层
第一层为参数
第二层为方法名称
第三层为方法参数